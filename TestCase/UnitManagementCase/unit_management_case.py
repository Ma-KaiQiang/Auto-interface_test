# coding:utf8
'''
@Time    : 2020/7/7 9:30
@Author  : MaKaiQiang
@File    : unit_management_case.py
'''

import unittest
import ddt
from tools.get_excel_case import GetExcelCase
from tools.log import Logger
from busniess.UnitMagementBusniess.unit_magement_busniess import UnitManagementBusniess
from tools.replace_data import ReplaceData
from tools.read_conf import ReadConf
import HTMLTestRunner_Chart

unit_case_file = ReadConf().get_conf('UNITMANAGEMENT').get('unit_management')
uuid_file = ReadConf().get_conf('INFRASTRUCTUREUUID').get('infrastructure_uuid')
unit_add_data = GetExcelCase(unit_case_file, '单位管理新增').get_dict_data
# unit_delete_data = GetExcelCase(unit_case_file, '单位管理删除').get_dict_data
# unit_modify_data = GetExcelCase(unit_case_file, '单位管理修改').get_dict_data
# unit_query_data = GetExcelCase(unit_case_file, '单位管理查找').get_dict_data
uuid_data = GetExcelCase(uuid_file, '楼栋房屋').get_dict_data
replace_unit_add = ReplaceData(unit_add_data, unit_case_file, '单位管理新增')
# replace_unit_delete = ReplaceData(unit_delete_data, unit_case_file, '单位管理删除')
# replace_unit_modify = ReplaceData(unit_modify_data, unit_case_file, '单位管理修改')
# replace_unit_query = ReplaceData(unit_query_data, unit_case_file, '单位管理查找')
replace_unit_add.replace_data_sheet(uuid_data)
# replace_unit_delete.replace_data_sheet(uuid_data)
# replace_unit_modify.replace_data_sheet(uuid_data)
# replace_unit_query.replace_data_sheet(uuid_data)
new_unit_add_data = GetExcelCase(unit_case_file, '单位管理新增').get_dict_data
# new_unit_delete_data = GetExcelCase(unit_case_file, '单位管理删除').get_dict_data
# new_unit_modify_data = GetExcelCase(unit_case_file, '单位管理修改').get_dict_data
# new_unit_query_data = GetExcelCase(unit_case_file, '单位管理查找').get_dict_data


@ddt.ddt
class UnitManangeTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.log = Logger()
        cls.unit_management_b = UnitManagementBusniess()

    @ddt.data(*new_unit_add_data)
    @ddt.unpack
    def test_1_unit_management_add(self, **kwargs):
        self.log.logger.debug(kwargs)
        try:
            actual_result = self.unit_management_b.unit_add_busniess(**kwargs)
            self.assertEqual(kwargs.get('expected_result'), actual_result.get("msg"), msg=f'"{kwargs.get("case")}" 用例执行失败')

        except Exception as e:
            self.log.logger.info(e)
            raise e
        else:
            self.log.logger.info(f'"{kwargs.get("case")}"用例执行通过')


if __name__ == '__main__':
    suite = unittest.makeSuite(UnitManangeTestCase, 'test_1_unit_management_add')

    with open(r'E:\Auto-interface\report\test_report.html', 'wb') as fp:
        runner = HTMLTestRunner_Chart.HTMLTestRunner(
            stream=fp,
            title='My unit test',
            verbosity=2,
            description='This demonstrates the report output by HTMLTestRunner.',

        )
        runner.run(suite)
        fp.close()
