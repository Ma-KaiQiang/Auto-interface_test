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
        self.res_filter = ResponseFilter()
        self.write_excel = WriteExcel(r'E:\Auto-interface\data\case.xlsx', '单位管理')
        self.get_case_data = GetExcelCase(r'E:\Auto-interface\data\case.xlsx', '单位管理')
        self.get_uuid = GetExcelCase(r'E:\Auto-interface\data\test_data.xlsx', '楼栋房屋')
        self.replace_data = ReplaceData(self.get_case_data.get_dict_data, r'E:\Auto-interface\data\case.xlsx', '单位管理')

    def update_new_data(self):
        data = self.get_uuid.get_dict_data
        parent_uuid1 = (data[1]['uuid'])
        parent_uuid2 = (data[2]['uuid'])
        self.replace_data.replace_data(0, parent_uuid1, 6)
        self.replace_data.replace_data(1, parent_uuid2, 6)

    def unit_management_busniess(self, **kwargs):
        response = self.res.method(**kwargs)
        self.res_filter.data_filter(str(response), uuid='Uuid', group=0)
        return response.get('msg')


if __name__ == '__main__':
    u = UnitManagementBusniess()
    u.get_new_data()
