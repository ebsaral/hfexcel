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