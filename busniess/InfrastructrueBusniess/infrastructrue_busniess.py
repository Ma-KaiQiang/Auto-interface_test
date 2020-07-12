# coding:utf8
'''
@Time    : 2020/7/8 14:42
@Author  : MaKaiQiang
@File    : infrastructure_case.py
'''
from tools.log import Logger
from tools.response_fileter_uuid import ResponseFilter
from tools.write_excel import WriteExcel
from public.response_func import ResponseFunc
from tools.replace_data import ReplaceData
from tools.get_excel_case import GetExcelCase


class InfrastructureBusniess():
    def __init__(self):
        self.log = Logger()
        self.res = ResponseFunc()
        self.res_filter = ResponseFilter()
        self.write_excel = WriteExcel(r'E:\Auto-interface\data\infrastructure\infrastructure_uuid.xlsx', '楼栋房屋')

    def infrastructure_add_busniess(self, old_excel_data, **kwargs):

        response = self.res.method(**kwargs)
        # 获取行数
        uuid = self.res_filter.data_filter(text=str(response), uuid='uuid', group=1)
        num = kwargs.get('row')
        if kwargs.get('replace'):
            replace = ReplaceData(old_excel_data, write_file_name=r'E:\Auto-interface\data\infrastructure\infrastructure_case.xlsx', write_sheet_name='楼栋房屋新增')
            replace.replace_data(num, uuid)
            self.log.logger.debug(f'uuid:{uuid} num:{num}')
        if response:
            # 将uuid写入到excel中
            self.write_excel.write(num + 1, 1, str(uuid))
            return response.get('msg')
        else:
            return False

    def infrastructure_query_busniess(self, old_excel_data, **kwargs):
        get_excel_uid = GetExcelCase(r'E:\Auto-interface\data\infrastructure\infrastructure_uuid.xlsx', '楼栋房屋')
        replace = ReplaceData(old_excel_data, write_file_name=r'E:\Auto-interface\data\infrastructure\infrastructure_case.xlsx', write_sheet_name='楼栋房屋查询')
        response = self.res.method(**kwargs)
        if response:
            uuid = get_excel_uid.get_dict_data[0]['uuid']
            num = kwargs.get('row')
            if kwargs.get('replace'):
                replace.replace_data(num, uuid)
            return response.get('msg')
        else:
            return False

    def infrastructure_modify_busniess(self, num1, old_excel_data, **kwargs):
        get_excel_uid = GetExcelCase(r'E:\Auto-interface\data\infrastructure\infrastructure_uuid.xlsx', '楼栋房屋')
        uuid = get_excel_uid.get_dict_data[num1]['uuid']
        num = kwargs.get('row')
        if kwargs.get('replace'):
            replace = ReplaceData(old_excel_data, write_file_name=r'E:\Auto-interface\data\infrastructure\infrastructure_case.xlsx', write_sheet_name='楼栋房屋修改')
            replace.replace_data(num, uuid)
        excel_data = GetExcelCase(fileName=r'E:\Auto-interface\data\infrastructure\infrastructure_case.xlsx', sheetName='楼栋房屋修改').get_dict_data[num1]
        self.log.logger.debug(f'获取的测试数据：{excel_data}')
        response = self.res.method(**excel_data)
        if response:

            return response.get('msg')
        else:
            return False

    def infrastructure_delete_busniess(self, num1, old_excel_data, **kwargs):
        get_excel_uid = GetExcelCase(r'E:\Auto-interface\data\infrastructure\infrastructure_uuid.xlsx', '楼栋房屋')
        uuid = get_excel_uid.get_dict_data[::-1][num1]['uuid']
        self.log.logger.debug(f'delete_uuid:{uuid}')
        num = kwargs.get('row')
        if kwargs.get('replace'):
            replace = ReplaceData(old_excel_data, write_file_name=r'E:\Auto-interface\data\infrastructure\infrastructure_case.xlsx', write_sheet_name='楼栋房屋删除')
            replace.replace_data(num, uuid)
        excel_data = GetExcelCase(fileName=r'E:\Auto-interface\data\infrastructure\infrastructure_case.xlsx', sheetName='楼栋房屋删除').get_dict_data[num1]
        self.log.logger.debug(f'获取的测试数据：{excel_data}')
        response = self.res.method(**excel_data)
        if response:

            return response.get('msg')
        else:
            return False
