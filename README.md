# hfexcel
human friendly excel creation in python

# example

```python
excel_data = {
    "sheets": [
        {
            "key": "sheet1",
            "name" : "Example Sheet 1",
            "columns": [
                {
                    "name": "Column 1",
                    "width": 2,
                    "args": [
                        "headline"
                    ],
                    "rows": [
                        {
                            "data": "Column 1 Row 1" 

                        },
                        {
                            "data": "Column 1 Row 2"
                        }
                    ]
                },
                {
                    "name": "Column 2",
                    "rows": [
                        {
                            "data": "Column 2 Row 1",
                        },
                        {
                            "data": "Column 2 Row 2",
                        }
                    ]
                },
                {
                    "name": "Column 3",
                    "rows": [
                        {
                            "data": "Column 3 Row 1"
                        },
                        {
                            "data": "Column 3 Row 2"
                        }
                    ]
                }
            ]
        }
    ],
    "styles": [
        "name": "headline",
        "style": {
            "bold": 1,
            "font_size": 14,
            "font": "Arial",
            "align": "center"
        }
    ]
}


import hf_excel
hf_workbook = hf_excel.HFExcel.workbook('example.xlsx', set_default_styles=False)
helper = hf_excel.HFWorkbookHelper(hf_workbook)
helper.populate_with_json(excel_data)
workbook = hf_workbook.save()

```
