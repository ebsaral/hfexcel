# hfexcel
human friendly excel creation in python

# example

```python
from hfexcel import HFExcel

excel_data = {
    "sheets": [
        {
            "key": "sheet1",
            "name": "Example Sheet 1",
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
        {
            "name": "headline",
            "style": {
                "bold": 1,
                "font_size": 14,
                "font": "Arial",
                "align": "center"
            }
        }
    ]
}

hf_workbook = HFExcel.hf_workbook('example.xlsx', set_default_styles=False)
hf_workbook.helper.populate_with_json(excel_data)
hf_workbook.save()
```

or 

```python
from hfexcel import HFExcel

hf_workbook = HFExcel.hf_workbook('example.xlsx', set_default_styles=False)

hf_workbook.add_style(
    "headline", 
    {
        "bold": 1,
        "font_size": 14,
        "font": "Arial",
        "align": "center"
    }
)

sheet1 = hf_workbook.add_sheet("sheet1", name="Example Sheet 1")

column1 = sheet1.add_column('headline', name='Column 1', width=2)
column1.add_row(data='Column 1 Row 1')
column1.add_row(data='Column 1 Row 2')

column2 = sheet1.add_column(name='Column 2')
column2.add_row(data='Column 2 Row 1')
column2.add_row(data='Column 2 Row 2')


column3 = sheet1.add_column(name='Column 3')
column3.add_row(data='Column 3 Row 1')
column3.add_row(data='Column 3 Row 2')

hf_workbook.save()
```


Based on XlsxWriter https://github.com/jmcnamara/XlsxWriter to have a human readable object-oriented design on writing Excel documents.
