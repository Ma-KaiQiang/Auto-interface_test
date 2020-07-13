# coding:utf8
'''
@Time    : 2020/7/8 10:15
@Author  : MaKaiQiang
@File    : unit_management_busniess.py
'''
from tools.log import Logger
from tools.write_conf import WriteConf
from tools.response_fileter_uuid import ResponseFilter
from tools.write_excel import WriteExcel, copy_excel
from public.response_func import ResponseFunc
from tools.get_excel_case import GetExcelCase
from tools.replace_data import ReplaceData


class UnitManagementBusniess():
    def __init__(self):
        self.log = Logger()
        self.res = ResponseFunc()

    def unit_add_busniess(self, **kwargs):
        response = self.res.method(**kwargs)
        if response:
            return response
        else:
            return False

    def unit_modify_busniess(self, **kwargs):
        pass

    def unit_delete_busniess(self, **kwargs):
        pass

    def unit_query_busniess(self, **kwargs):
        pass
