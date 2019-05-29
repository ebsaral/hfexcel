from functools import reduce

from ...helpers import HFWorkbookHelperBase

mult = lambda a, b: len(a) * len(b)

from addict import Dict


def _populate_columns_with_rows(sheet, columns, rows):
    i = 0
    while i < len(columns):
        column = columns[i]
        width = int(column.get("width", 0)) or None
        column_name = column.get("name", "")
        cell_format = column.get("cell_format")
        options = column.get("options")
        args = column.get("args", ())
        bp_column, _ = sheet.add_column(
            *args,
            name=column_name,
            width=width,
            cell_format=cell_format,
            options=options,
        )
        _populate_rows(bp_column, rows, i)
        i += 1


def _populate_rows(bp_column, rows, i):
    for row in rows:
        column_row_json = row[i]
        data = column_row_json.get("data") or ""
        args = column_row_json.get("args", ())
        width = int(column_row_json.get("width", 0)) or None
        row, _ = bp_column.add_row(*args, data=data, width=width)


class DataFrameHelper(HFWorkbookHelperBase):
    def __init__(self, bp_workbook):
        super().__init__(bp_workbook)
        self.data = []

    def hf_sheets(self):
        return self.bp_workbook.hf_sheets

    def hf_sheet_by_index(self, index):
        for sheet in self.bp_workbook.hf_sheets:
            if sheet.index == index:
                return sheet
        return None

    def _set_sheet_data(self, sheets):
        for sheet in sheets:
            sheet_data = Dict()
            sheet_data.exists = {
                "columns": bool(len(sheet.columns)),
                "index": bool(len(sheet.index)),
            }

            sheet_data.len = {
                "index_names": len(sheet.index.names),
                "index_data": len(sheet.index.data),
                "columns_names": len(sheet.columns.names),
                "columns_data": len(sheet.columns.data),
                "row": sheet.index.data and reduce(mult, sheet.index.data),
                "column": sheet.columns.data and reduce(mult, sheet.columns.data),
                "input_data_row": len(sheet.data),
                "input_data_columns": reduce(mult, sheet.data),
            }

            sheet_data.names = {
                "index": sheet.index.names,
                "columns": sheet.columns.names,
            }

            sheet_data.data = (
                {"index": sheet.index.data, "columns": sheet.columns.data},
            )

            sheet_data.left = len(sheet.index.names)
            sheet_data.top = len(sheet.columns.names)

            self.data.append(sheet_data)

    def _validate_data(self):
        pass

    def _set_column(self, sheet_data, left, c_index, width, data):
        name = ""
        # if c_index == left - 1:
        #     if sheet_data['len']['columns']
        #     sheet_data['']

    def _populate_sheets_with_json(self, sheets, validate=True):
        self._set_sheet_data(sheets)
        if validate:
            self._validate_data()

        frame_data = [
            [0.2, 1, "ASDFG", "a1", 0.1, "ACTG"],
            [1.5, 5, "QWERT", "a1", 0.2, "ACTG"],
            [5, 8, "ZXCVB", "b1", 0.4, "ACTG"],
            [9, 8, "ZXCVB", "b1", 0.5, "ACTG"],
            [9, 8, "ZXCVB", "b1", 0.6, "ACTG"],
            [9, 8, "ZXCVB", "b1", 0.8, "ACTG"],
        ]

        i = 0
        for sheet in sheets:
            data = self.data[i]

            d = {
                "key": "sheet1",
                "name": "Sheet 1",
                "index": {
                    "names": ["first", "second"],
                    "data": [["bar", "baz", "foo"], ["one", "two"]],
                },
                "columns": {
                    "names": ["colLevel1", "colLevel2"],
                    "data": [["A", "B"], ["value", "error", "sequence"]],
                },
            }

            width = data.left + data.len.input_data_columns

            for c_index in range(0, width):
                self._set_column(
                    self.data[i], data["left"], c_index, width, sheet["data"]
                )

            i += i

        for sheet_json in sheets:
            rows = sheet_json.get("rows", [])
            columns = sheet_json.get("columns", [])

            length = len(columns)
            if not all(len(row) == length for row in rows):
                raise ValueError("all rows and columns must be same length")

            sheet = self.bp_workbook.add_sheet(
                sheet_json.get("key"),
                name=sheet_json.get("name"),
                page_width=sheet_json.get("page_width"),
                page_height=sheet_json.get("page_height"),
            )

            _populate_columns_with_rows(sheet, columns, rows)

    def _populate_styles_with_json(self, styles):
        for style in styles:
            self.bp_workbook.add_style(style.name, style.style)

    def populate_with_json(self, workbook_data, validate=True):
        frame_data = [
            [0.2, 1, "ASDFG", "a1", 0.1, "ACTG"],
            [1.5, 5, "QWERT", "a1", 0.2, "ACTG"],
            [5, 8, "ZXCVB", "b1", 0.4, "ACTG"],
            [9, 8, "ZXCVB", "b1", 0.5, "ACTG"],
            [9, 8, "ZXCVB", "b1", 0.6, "ACTG"],
            [9, 8, "ZXCVB", "b1", 0.8, "ACTG"],
        ]

        data = {
            "sheets": [
                {
                    "key": "sheet1",
                    "name": "Sheet 1",
                    "index": {
                        "names": ["first", "second"],
                        "data": [["bar", "baz", "foo"], ["one", "two"]],
                    },
                    "columns": {
                        "names": ["colLevel1", "colLevel2"],
                        "data": [["A", "B"], ["value", "error", "sequence"]],
                    },
                    "data": frame_data,
                }
            ],
            "styles": [],
        }

        data = Dict(data)
        self._populate_sheets_with_json(data.sheets, validate=validate)
        self._populate_styles_with_json(data.styles)
        return self
