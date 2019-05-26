from .models import HFExcelWorkbook


class HFExcel:
    __slots__ = []

    @staticmethod
    def hf_workbook(filename=None, set_default_styles=False):
        return HFExcelWorkbook(filename=filename,
                               set_default_styles=set_default_styles)
