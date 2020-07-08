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


class UnitManagementBusniess():
    def __init__(self):
        self.log = Logger()
        self.res = ResponseFunc()
        self.write_c = WriteConf()
        self.res_filter = ResponseFilter()
        self.write_excel = WriteExcel(r'E:\Auto-interface\data\case.xlsx', '单位管理')

    def unit_management_busniess(self, **kwargs):
        response = self.res.method(**kwargs)
        self.res_filter.data_filter(str(response), uuid='Uuid', group=0)
        return response.get('msg')
