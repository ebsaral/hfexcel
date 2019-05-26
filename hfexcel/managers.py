from hf_excel.utils import HFExcelWorkbook


class HFExcel:
    __slots__ = []

    @staticmethod
    def workbook(filename=None, set_default_styles=False):
        workbook = HFExcelWorkbook(filename=filename,
                                   set_default_styles=set_default_styles)
        return workbook
