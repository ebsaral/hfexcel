from ...helpers import HFWorkbookHelperBase


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


class InlineInputHelper(HFWorkbookHelperBase):
    def _populate_sheets_with_json(self, sheets):
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
        for style_json in styles:
            self.bp_workbook.add_style(style_json.get("name"), style_json.get("style"))

    def populate_with_json(self, workbook_data):
        self._populate_sheets_with_json(workbook_data.get("sheets", []))
        self._populate_styles_with_json(workbook_data.get("styles", []))
        return self
