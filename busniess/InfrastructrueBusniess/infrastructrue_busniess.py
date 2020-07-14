# coding:utf8
'''
@Time    : 2020/7/8 14:42
@Author  : MaKaiQiang
@File    : infrastructure_busniess.py
'''
from public.response_func import ResponseFunc
from tools.log import Logger
from tools.replace_data import ReplaceData
from tools.response_fileter_uuid import ResponseFilter
from tools.write_excel import WriteExcel


class InfrastructureBusniess():
    def __init__(self):
        self.log = Logger()
        self.res = ResponseFunc()
        self.res_filter = ResponseFilter()
        self.write_excel = WriteExcel(r'E:\Auto-interface\data\infrastructure\infrastructure_uuid.xlsx', '楼栋房屋')

    def infrastructure_add_busniess(self, old_excel_data, **kwargs):

        response = self.res.method(**kwargs)
        # 获取行数
        uuid = self.res_filter.data_filter(text=str(response[0]), uuid='uuid', group=1)
        num = kwargs.get('row')
        if kwargs.get('replace'):
            replace = ReplaceData(old_excel_data, write_file_name=r'E:\Auto-interface\data\infrastructure\infrastructure_case.xlsx', write_sheet_name='楼栋房屋新增')
            replace.replace_data(num, uuid)
            self.log.logger.debug(f'uuid:{uuid} num:{num}')
        if response:
            # 将uuid写入到excel中
            self.write_excel.write(num + 1, 1, str(uuid))
            return response
        else:
            return False

    def infrastructure_query_busniess(self, **kwargs):
        response = self.res.method(**kwargs)
        if response:
            return response
        else:
            return False

    def infrastructure_modify_busniess(self, **kwargs):
        response = self.res.method(**kwargs)
        if response:
            return response
        else:
            return False

    def infrastructure_delete_busniess(self, **kwargs):
        response = self.res.method(**kwargs)
        if response:
            return response
        else:
            return False
