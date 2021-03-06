from hfexcel import HFExcel
from hfexcel.extras import InlineInputHelper


def example(filename='example.xlsx'):
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
            },
            {
                "key": "sheet2",
                "name": "Example Sheet 2",
                "columns": [
                    {
                        "name": "Column 1",
                        "width": 2,
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

    hf_workbook = HFExcel.hf_workbook(filename, set_default_styles=False)
    hf_workbook.filter().populate_with_json(excel_data)
    hf_workbook.save()
    return True

def example2(filename='example2.xlsx'):
    hf_workbook = HFExcel.hf_workbook(filename, set_default_styles=False)

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
    return True


def example3(filename='example3.xlsx'):
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
                    },
                    {
                        "name": "Column 3"
                    }
                ],
                "rows": [
                    [
                        {
                            "data": "Column 1 Row 1"

                        },
                        {
                            "data": "Column 2 Row 1"
                        },
                        {
                            "data": "Column 3 Row 1"
                        }
                    ],
                    [
                        {
                            "data": "Column 1 Row 2"

                        },
                        {
                            "data": "Column 2 Row 2"
                        },
                        {
                            "data": "Column 3 Row 2"
                        }
                    ],
                    [
                        {
                            "data": "Column 1 Row 3"

                        },
                        {
                            "data": "Column 2 Row 3"
                        },
                        {
                            "data": "Column 3 Row 3"
                        }
                    ]
                ]
            },
            {
                "key": "sheet2",
                "name": "Example Sheet 2",
                "columns": [
                    {
                        "name": "Column 1",
                        "width": 2
                    },
                    {
                        "name": "Column 2"
                    },
                    {
                        "name": "Column 3"
                    }
                ],
                "rows": [
                    [
                        {
                            "data": "Column 1 Row 1"

                        },
                        {
                            "data": "Column 2 Row 1"
                        },
                        {
                            "data": "Column 3 Row 1"
                        }
                    ],
                    [
                        {
                            "data": "Column 1 Row 2"

                        },
                        {
                            "data": "Column 2 Row 2"
                        },
                        {
                            "data": "Column 3 Row 2"
                        }
                    ],
                    [
                        {
                            "data": "Column 1 Row 3"

                        },
                        {
                            "data": "Column 2 Row 3"
                        },
                        {
                            "data": "Column 3 Row 3"
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
