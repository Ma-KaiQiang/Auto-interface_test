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
    def __init__(self,old_excel_data):
        self.log = Logger()
        self.res = ResponseFunc()
        self.write_c = WriteConf()
        self.res_filter = ResponseFilter()
        self.write_excel = WriteExcel(r'E:\Auto-interface\data\test_data.xlsx', '楼栋房屋')
        self.replace = ReplaceData(old_excel_data)
        self.num = 2

    def infrastructure_busniess(self, **kwargs):
        response = self.res.method(**kwargs)
        if response:
            if kwargs.get('requests_type') == 'post':
                uuid = self.res_filter.data_filter(text=str(response), uuid='uuid', group=1)
                self.log.logger.debug(f'uuid:{uuid} num:{self.num}')
                self.write_excel.write(self.num + 1, 1, str(uuid))
                if self.num <= 7:
                    self.replace.replace_data(self.num, uuid)
                elif 7 < self.num <= 9:
                    self.replace.replace_data(self.num, uuid, col=3)
                # elif 9 < self.num <= 12:
                #     self.replace.replace_data(self.num, col=4)

                self.num += 1

        return response.get('msg')
