# hfexcel 0.0.17 [![CircleCI](https://circleci.com/gh/ebsaral/hfexcel.svg?style=svg)](https://circleci.com/gh/ebsaral/hfexcel) [![codecov](https://codecov.io/gh/ebsaral/hfexcel/branch/master/graph/badge.svg)](https://codecov.io/gh/ebsaral/hfexcel)

human friendly excel creation in python

# development versions of dependencies

- Python 3.x
- XlsxWriter==1.1.8
- jsonschema==2.6.0
- pytest
- codecov
- pytest-cov

# install

```
pip install hfexcel
```

# features

- Human readable coding, building
- Object-Obriented based readable models: `HFExcelWorkbook`, `HFExcelSheet`, `HFExcelColumn`, `HFExcelColumn`
- `HFExcelWorkbookFilter`: Helper class to populate Excel from a JSON data (python `dict`) with a pre-defined json schema. (default:`hfexcel.schemas.DEFAULT_SCHEMA`)
- `HFExcelWorkbook.output`: Output creation on `filename (string)` input being null, and created `output` parameter with the type `BytesIO` linked to workbook itself


# playground

- http://www.hfexcel.io/

# example of converting nested objects {sheet>column>row} input from json format into excel format

```python
from hfexcel import HFExcel
from hfexcel.schemas import DEFAULT_SCHEMA


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
hf_workbook.filter().populate_with_json(excel_data, schema=DEFAULT_SCHEMA)
hf_workbook.save()
```

# example of object-oriented python syntax

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

column1, _ = sheet1.add_column('headline', name='Column 1', width=2)
column1.add_row(data='Column 1 Row 1')
column1.add_row(data='Column 1 Row 2')

column2, _ = sheet1.add_column(name='Column 2')
column2.add_row(data='Column 2 Row 1')
column2.add_row(data='Column 2 Row 2')


column3, _ = sheet1.add_column(name='Column 3')
column3.add_row(data='Column 3 Row 1')
column3.add_row(data='Column 3 Row 2')

# In order to get a row with coordinates:
# sheet[column_index][row_index] => row
print(sheet1[1][1].data)
assert(sheet1[1][1].data == 'Column 2 Row 2')

hf_workbook.save()
```

# example of converting inline index-based {sheet>[column:row]} input from json format into excel format


```python
from hfexcel import HFExcel
from hfexcel.extras import InlineInputHelper

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
                    ]
                },
                {
                    "name": "Column 2"
                }
            ],
            "rows": [
                [
                    {
                        "data": "Column 1 Row 1"

                    },
                    {
                        "data": "Column 2 Row 1"
                    }
                ],
                [
                    {
                        "data": "Column 1 Row 2"

                    },
                    {
                        "data": "Column 2 Row 2"
                    }
                ]
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

hf_workbook = HFExcel.hf_workbook(filename, set_default_styles=False)
InlineInputHelper(hf_workbook).populate_with_json(excel_data)
hf_workbook.save()
return True
```

# example output file

- https://github.com/ebsaral/hfexcel/blob/master/example.xlsx

# contributors

- @ebsaral - author
- feel free to contribute

# dependencies

- @jmcnamara: Based on XlsxWriter https://github.com/jmcnamara/XlsxWriter (to have a human readable object-oriented design on writing Excel documents)
- @Julian: JSON Schema Validation, jsonschema https://github.com/Julian/jsonschema

# warning

- Happy path tests are written.
