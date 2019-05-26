from io import BytesIO

import xlsxwriter

from .helpers import get_coor_name, HFWorkbookFilter
from .styles import HFExcelStyle


class HFExcelWorkbook:
    __slots__ = [
        'filename',
        'output',
        '_sheets',
        '_set_default_styles',
        '_style',
        '_workbook',
    ]

    def __init__(self, filename=None, set_default_styles=True):
        self._sheets = []
        self._workbook = None
        self._style = None
        self.filename = filename
        self._set_default_styles = set_default_styles
        self._init_workbook(filename, set_default_styles)


    def filter(self):
        return HFWorkbookFilter(self)

    def _init_workbook(self, filename, set_default_styles):
        if filename and isinstance(filename, str):
            _workbook = xlsxwriter.Workbook(filename)
            self.output = None
        else:
            self.output = BytesIO()
            _workbook = xlsxwriter.Workbook(self.output)

        del self._workbook
        del self._style

        self._workbook = _workbook

        self._style = HFExcelStyle(self.workbook)
        if set_default_styles:
            self.set_default_styles()

    @property
    def workbook(self):
        return self._workbook

    @property
    def style(self):
        return self._style

    @property
    def hf_sheets(self):
        return self._sheets

    def add_style(self, name, style):
        self.style.add(name, style)

    def set_default_styles(self):
        return self.style.set_defaults()

    def add_sheet(self, key, name=None, columns=None, page_width=None,
                  page_height=None):
        for s in self._sheets:
            if s.key == key:
                return None
        sheet = HFExcelSheet(self,
                             key=key,
                             name=name,
                             columns=columns,
                             page_width=page_width,
                             page_height=page_height)
        self.hf_sheets.append(sheet)
        return sheet

    def hf_sheet(self, key):
        for s in self.hf_sheets:
            if s.key == key:
                return s
        return None

    def clean(self, filename=None, set_default_styles=None):
        self._sheets = []
        new_filename = filename or self.filename
        new_default_styles = (set_default_styles
                              or self._set_default_styles)
        self._init_workbook(new_filename, new_default_styles)

    def _save_sheets(self):
        next_col_index = 0
        for hf_sheet in self.hf_sheets:
            hf_sheet.sheet.print_area(0, 0,
                                      hf_sheet.height,
                                      hf_sheet.width)
            hf_sheet.sheet.fit_to_pages(hf_sheet.page_width,
                                        hf_sheet.page_height)
            next_col_index = hf_sheet.save(next_col_index)
        return True

    def save(self, close=True):
        self._save_sheets()
        if close:
            self.workbook.close()
        return self.workbook


class HFExcelSheet:
    __slots__ = [
        'key',
        'name',
        'page_height',
        'page_width',
        '_workbook',
        '_sheet',
        '_columns',
        '_curr_column_pos',
        '_curr_row_height',
    ]

    def __init__(self, workbook, key, name=None, columns=None, page_width=None,
                 page_height=None):
        self._workbook = workbook
        self.key = key
        self.name = name if name else key
        self._columns = columns or []
        self._curr_column_pos = 0
        self._curr_row_height = 0
        self._sheet = self.workbook.add_worksheet()
        self.page_width = int(page_width or 1)
        self.page_height = int(page_height or 0)

    def __getitem__(self, key):
        return self.columns[key]

    @property
    def workbook(self):
        return self.hf_workbook.workbook

    @property
    def hf_workbook(self):
        return self._workbook

    @property
    def sheet(self):
        return self._sheet

    @property
    def width(self):
        return self._curr_column_pos

    @property
    def height(self):
        return self._curr_row_height

    @property
    def row_height(self):
        return self._curr_row_height

    @property
    def next_row(self):
        return self.row_height + 1

    @property
    def next_col(self):
        return self._curr_column_pos

    @property
    def columns(self):
        return self._columns

    def add_column(self,
                   *args,
                   name='',
                   width=None,
                   cell_format=None,
                   options=None,
                   hide_header=False):

        width = width or 1
        if width <= 0:
            raise ValueError('Column width cannot be equal or less than 0')

        self._curr_column_pos = self._curr_column_pos + width

        column = HFExcelColumn(self,
                               *args,
                               name=name,
                               width=width,
                               cell_format=cell_format,
                               options=options,
                               hide_header=hide_header)

        self._columns.append(column)
        return column, len(self.columns) - 1

    def add_row(self, column_index, *args, data='', width=None):
        column = self.columns[column_index]
        row = column.add_row(*args, data=data, width=None)
        self._curr_row_height = max(
            column.hf_sheet.next_row - 1,
            len(column.rows)
        )
        return row

    def save(self, reference_index):
        next_col_index = reference_index
        next_row_index_max = 0
        for column in self.columns:
            next_col_index, next_row_index = column.save(next_col_index)
            next_row_index_max = max(next_row_index, next_row_index_max)
        return next_col_index, next_row_index_max


class HFExcelColumn:
    __slots__ = [
        'args',
        'cell_format',
        'hide_header',
        'name',
        'options',
        '_style',
        '_rows',
        '_sheet',
        '_width',
    ]

    def __init__(self,
                 sheet,
                 *args,
                 name='',
                 width=None,
                 cell_format=None,
                 options=None,
                 hide_header=False):
        self._sheet = sheet
        self._width = width
        self._style = (len(args) and args[0]) or None
        self.args = args and args[1:]
        self.cell_format = cell_format
        self.name = name
        self.options = options
        self.hide_header = hide_header
        self._rows = []

    def __getitem__(self, key):
        return self.rows[key]

    @property
    def required_args(self):
        return (self.name, self.style)

    @property
    def style(self):
        if not self._style:
            return None
        return getattr(self.hf_workbook.style, self._style)


    @property
    def width(self):
        return int(self._width or 1)

    @property
    def hf_sheet(self):
        return self._sheet

    @property
    def hf_workbook(self):
        return self.hf_sheet.hf_workbook

    @property
    def rows(self):
        return self._rows

    def add_row(self, *args, data='', width=None):
        row = HFExcelRow(self, *args, data=data, width=width)
        self.rows.append(row)
        return row, len(self.rows) - 1

    def save(self, reference_index):
        if self.hide_header:
            next_row = 0
            next_row_max = 0
        else:
            self.hf_sheet.sheet.set_column(reference_index,
                                           reference_index + self.width - 1)
            if self.width <= 1:
                new_args = self.required_args + self.args
                self.hf_sheet.sheet.write(0,
                                          reference_index,
                                          *new_args)
            else:
                coor_name = get_coor_name(0, reference_index,
                                          0, reference_index + self.width - 1)
                self.hf_sheet.sheet.merge_range(coor_name, self.name, self.style)
            next_row = 1
            next_row_max = 1
        for row in self.rows:
            _, next_row = row.save(reference_index, next_row)
            next_row_max = max(next_row, next_row_max)
        return reference_index + self.width, next_row_max


class HFExcelRow:
    __slots__ = [
        'args',
        'data',
        '_style',
        '_column',
        '_width',
    ]

    def __init__(self, column, *args, data='', width=None):
        self._column = column
        self.data = data
        self._style = (len(args) and args[0]) or None
        self.args = args and args[1:]
        self._width = width or 1

    @property
    def column(self):
        return self._column

    @property
    def width(self):
        if self._width > self.column.width:
            return self.column.width
        return self._width

    @property
    def hf_sheet(self):
        return self.column.hf_sheet

    @property
    def hf_workbook(self):
        return self.hf_sheet.hf_workbook

    @property
    def style(self):
        if not self._style:
            return None
        return getattr(self.hf_workbook.style, self._style)

    @property
    def required_args(self):
        return (self.data, self.style)

    def save(self, column, row):
        if self.width <= 1:
            new_args = self.required_args + self.args
            self.hf_sheet.sheet.write(row,
                                      column,
                                      *new_args)
        else:
            coor_name = get_coor_name(row, column,
                                      row, column + self.width - 1)
            self.hf_sheet.sheet.merge_range(coor_name, self.data, self.style)
        return column + self.width, row + 1
