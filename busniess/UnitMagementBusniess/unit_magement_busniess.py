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
        self.write_excel = WriteExcel(r'E:\Auto-interface\data\unit_management\unit_management_uuid.xlsx', '单位管理')

    def unit_add_busniess(self, **kwargs):
        response = self.res.method(**kwargs)
        if response:
            if response.get('data').get('uuid'):
                num = kwargs.get('row')
                compony_uuid = response.get('data').get('uuid')
                self.write_excel.write(num + 1, 1, str(compony_uuid))
            return response
        else:
            return False

    def unit_modify_busniess(self, **kwargs):
        get_unit_uuid = GetExcelCase(r'E:\Auto-interface\data\unit_management\unit_management_uuid.xlsx', '单位管理')
        unit_uuid_data = get_unit_uuid.get_dict_data[0]['uuid']
        get_infrastructure_uuid = GetExcelCase(r'E:\Auto-interface\data\infrastructure\infrastructure_uuid.xlsx', '楼栋房屋')
        self.log.logger.debug(f'unit_uuid:{unit_uuid_data}')
        infrastructure_uuid = eval(get_infrastructure_uuid.get_dict_data[7]['uuid'])[0]
        self.log.logger.debug(f'in_uuid:{infrastructure_uuid}')
        self.log.logger.debug(type(kwargs['json']))
        kwargs1 = eval(str(kwargs).replace(eval(kwargs['json'])['infrastructureUuid'], infrastructure_uuid))
        kwargs2 = eval(str(kwargs1).replace(eval(kwargs1['json'])['companyUuid'], unit_uuid_data))

        self.log.logger.debug(f'kwargs{type(kwargs2)}')
        response = self.res.method(**kwargs2)
        if response:
            return response
        else:
            return False

    def unit_delete_busniess(self, **kwargs):
        response = self.res.method(**kwargs)
        if response:
            return response
        else:
            return False

    def unit_query_busniess(self, **kwargs):
        response = self.res.method(**kwargs)
        if response:
            return response
        else:
            return False
