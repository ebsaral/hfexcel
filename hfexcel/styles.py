class HFExcelStyle:
    __slots__ = [
        'workbook',
        'styles',
    ]

    def __init__(self, workbook):
        self.workbook = workbook
        self.styles = {}

    def add(self, name, style):
        self.styles[name] = self.workbook.add_format(style)

    def __getattr__(self, name):
        return self.styles.get(name)

    def set_defaults(self):
        grey_color = '#E0E0E0'
        orange_color = '#FFB266'

        decimal_format = '#,##0.00'
        no_decimal_format = '#,##0'

        self.add('headline', {
            'bold': 1,
            'font_size': 12,
            'font': 'Arial',
            'align': 'center'
        })

        self.add('bold', {
            'font': 'Arial',
            'bold': 1
        })

        self.add('center_bold', {
            'font': 'Arial',
            'bold': 1,
            'align': 'center'
        })

        self.add('grey', {
            'font': 'Arial',
            'bg_color': grey_color,
        })

        self.add('grey_bold', {
            'font': 'Arial',
            'bg_color': grey_color,
            'bold': 1
        })

        self.add('grey_bold_decimals', {
            'font': 'Arial',
            'bg_color': grey_color,
            'bold': 1,
            'num_format': decimal_format
        })

        self.add('grey_bold_no_decimals', {
            'font': 'Arial',
            'bg_color': grey_color,
            'bold': 1,
            'num_format': no_decimal_format
        })

        self.add('grey_center', {
            'font': 'Arial',
            'bg_color': grey_color,
            'align': 'center',
            'valign': 'vcenter',
        })

        self.add('grey_center_decimals', {
            'font': 'Arial',
            'bg_color': grey_color,
            'align': 'center',
            'num_format': decimal_format
        })

        self.add('grey_center_no_decimals', {
            'font': 'Arial',
            'bg_color': grey_color,
            'align': 'center',
            'num_format': no_decimal_format
        })

        self.add('grey_center_bold', {
            'font': 'Arial',
            'bg_color': grey_color,
            'align': 'center',
            'bold': 1,
            'valign': 'vcenter'
        })

        self.add('grey_center_percentage', {
            'font': 'Arial',
            'bg_color': grey_color,
            'align': 'center',
            'num_format': '0.00"%"'
        })

        self.add('no_decimal_format', {
            'font': 'Arial',
            'num_format': no_decimal_format
        })

        self.add('decimal_format', {
            'font': 'Arial',
            'num_format': decimal_format
        })

        self.add('arial', {
            'font': 'Arial'
        })

        self.add('align_right', {
            'font': 'Arial',
            'align': 'right'
        })

        self.add('align_left', {
            'font': 'Arial',
            'align': 'left'
        })

        self.add('align_right_bold', {
            'font': 'Arial',
            'align': 'right',
            'bold': 1
        })

        self.add('align_left_bold', {
            'font': 'Arial',
            'align': 'left',
            'bold': 1
        })

        self.add('align_date_left', {
            'font': 'Arial',
            'align': 'left',
            'num_format': self.date_format_excel
        })

        self.add('orange', {
            'bg_color': orange_color,
            'font_color': 'white',
            'bold': 1,
            'font': 'Arial',
            'align': 'center'
        })
