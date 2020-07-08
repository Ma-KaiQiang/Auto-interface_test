# coding:utf8
'''
@Time    : 2020/7/8 14:42
@Author  : MaKaiQiang
@File    : infrastructure_case.py
'''
from tools.log import Logger
from tools.write_conf import WriteConf
from tools.response_fileter_uuid import ResponseFilter
from tools.write_excel import WriteExcel, copy_excel
from public.response_func import ResponseFunc
from tools.replace_data import ReplaceData


class InfrastructureBusniess():
    def __init__(self):
        self.log = Logger()
        self.res = ResponseFunc()
        self.write_c = WriteConf()
        self.res_filter = ResponseFilter()
        self.write_excel = WriteExcel(r'E:\Auto-interface\data\test_data.xlsx', '楼栋房屋')
        self.replace = ReplaceData()
        self.num = 2

    def infrastructure_busniess(self, **kwargs):
        response = self.res.method(**kwargs)
        if response:
            if kwargs.get('requests_type') == 'post':
                uuid = self.res_filter.data_filter(text=str(response), uuid='uuid', group=1)
                self.log.logger.debug(f'uuid:{uuid} num:{self.num}')
                self.write_excel.write(self.num, 1, str(uuid))
                self.replace.replace_data(self.num, uuid)
                self.num += 1

        return response.get('msg')
