from jsonschema import validate

from xlsxwriter.utility import xl_rowcol_to_cell

from .schemas import DEFAULT_SCHEMA


def get_coor_name(from_row, from_col, to_row, to_col):
    start = xl_rowcol_to_cell(from_row, from_col)
    end = xl_rowcol_to_cell(to_row, to_col)
    return f"{start}:{end}"


class HFWorkbookFilter:
    __slots__ = ['bp_workbook']

    def __init__(self, bp_workbook):
        self.bp_workbook = bp_workbook

    def _raise_error(self, text):
        raise ValueError(text)

    def _populate_sheets_with_json(self, sheets):
        for sheet_json in sheets:
            sheet = self.bp_workbook.add_sheet(
                sheet_json.get('key'),
                name=sheet_json.get('name'),
                page_width=sheet_json.get('page_width'),
                page_height=sheet_json.get('page_height'))

            self._populate_columns_with_json(sheet,
                                             sheet_json.get('columns',
                                                            []))

    def _populate_columns_with_json(self, sheet, columns):
        for column_json in columns:
            width = int(column_json.get('width', 0)) or None
            column_name = column_json.get('name') or self._raise_error(
                'column name is missing')
            cell_format = column_json.get('cell_format')
            options = column_json.get('options')
            args = column_json.get('args', ())
            column, _ = sheet.add_column(*args,
                                         name=column_name,
                                         width=width,
                                         cell_format=cell_format,
                                         options=options)

            self._populate_rows_with_json(column,
                                          column_json.get('rows', []))

    def _populate_rows_with_json(self, column, rows):
        for row_json in rows:
            data = row_json.get('data') or self._raise_error(
                'row data is missing')
            args = row_json.get('args', ())
            width = int(row_json.get('width', 0)) or None
            row, _ = column.add_row(*args, data=data, width=width)

    def _populate_styles_with_json(self, styles):
        for style_json in styles:
            self.bp_workbook.add_style(style_json.get('name'),
                                       style_json.get('style'))

    def populate_with_json(self, workbook_data):
        validate(instance=workbook_data, schema=DEFAULT_SCHEMA)
        self._populate_sheets_with_json(workbook_data.get('sheets', []))
        self._populate_styles_with_json(workbook_data.get('styles', []))
        return self
