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
infrastructure_uuid_file = ReadConf().get_conf('INFRASTRUCTUREUUID').get('infrastructure_uuid')
unit_uuid_file = ReadConf().get_conf('UNITMANAGEMENTUUID').get('unit_management_uuid')
# 加载uuid
infrastructure_uuid_data = GetExcelCase(infrastructure_uuid_file, '楼栋房屋').get_dict_data
unit_uuid_data = GetExcelCase(unit_uuid_file, '单位管理').get_dict_data
# 加载测试数据
unit_add_data = GetExcelCase(unit_case_file, '单位管理新增').get_dict_data
unit_delete_data = GetExcelCase(unit_case_file, '单位管理删除').get_dict_data
unit_query_data = GetExcelCase(unit_case_file, '单位管理查找').get_dict_data
unit_modify_data = GetExcelCase(unit_case_file, '单位管理修改').get_dict_data
# 替换uuid
replace_unit_add = ReplaceData(unit_add_data, unit_case_file, '单位管理新增')
replace_unit_add.replace_data_sheet(infrastructure_uuid_data)
# 获取最新测试数据
new_unit_add_data = GetExcelCase(unit_case_file, '单位管理新增').get_dict_data


@ddt.ddt
class Test1UnitManangementAdd(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.log = Logger()
        cls.unit_management_b = UnitManagementBusniess()

    @ddt.data(*new_unit_add_data)
    @ddt.unpack
    @unittest.skip
    def test_unit_management_add(self, **kwargs):
        self.log.logger.debug(kwargs)
        try:
            actual_result = self.unit_management_b.unit_add_busniess(**kwargs)
            self.assertEqual(kwargs.get('expected_result'), actual_result.get("msg"), msg=f'"{kwargs.get("case")}" 用例执行失败')

        except Exception as e:
            self.log.logger.info(e)
            raise e
        else:
            self.log.logger.info(f'"{kwargs.get("case")}"用例执行通过')


@ddt.ddt
class Test2UnitManangementQuery(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.log = Logger()
        cls.unit_management_b = UnitManagementBusniess()
        cls.replace_unit_query = ReplaceData(unit_query_data, unit_case_file, '单位管理查找')
        cls.replace_unit_query.replace_data_sheet(unit_uuid_data)
        cls.new_unit_query_data = GetExcelCase(unit_case_file, '单位管理查找').get_dict_data

    @ddt.data(*unit_query_data)
    @ddt.unpack
    # @unittest.skip
    def test_unit_management_query(self, **kwargs):
        self.log.logger.debug(kwargs)
        try:
            new_kwargs = self.new_unit_query_data[kwargs.get('row') - 1]
            actual_result = self.unit_management_b.unit_query_busniess(**new_kwargs)
            self.log.logger.debug(f'actucal_result:{actual_result}')
            self.assertEqual(kwargs.get('expected_result'), actual_result.get("msg"), msg=f'"{kwargs.get("case")}" 用例执行失败')
        except Exception as e:
            self.log.logger.info(e)
            raise e
        else:
            self.log.logger.info(f'"{kwargs.get("case")}"用例执行通过')


@ddt.ddt
class Test3UnitManangementModify(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.log = Logger()
        cls.unit_management_b = UnitManagementBusniess()

    @ddt.data(*unit_modify_data)
    @ddt.unpack
    @unittest.skip
    def test_unit_management_modify(self, **kwargs):
        self.log.logger.debug(kwargs)
        try:
            actual_result = self.unit_management_b.unit_modify_busniess(**kwargs)
            self.log.logger.debug(f'actucal_result:{actual_result}')
            self.assertEqual(kwargs.get('expected_result'), actual_result.get("msg"), msg=f'"{kwargs.get("case")}" 用例执行失败')
        except Exception as e:
            self.log.logger.info(e)
            raise e
        else:
            self.log.logger.info(f'"{kwargs.get("case")}"用例执行通过')


@ddt.ddt
class Test4UnitManangementDelete(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.log = Logger()
        cls.unit_management_b = UnitManagementBusniess()
        cls.replace_unit_delete = ReplaceData(unit_delete_data, unit_case_file, '单位管理删除')
        cls.replace_unit_delete.replace_data_sheet(unit_uuid_data)
        cls.new_unit_delete_data = GetExcelCase(unit_case_file, '单位管理查找').get_dict_data

    @ddt.data(*unit_delete_data)
    @ddt.unpack
    def test_unit_management_delete(self, **kwargs):
        self.log.logger.debug(kwargs)
        try:
            new_kwargs = self.new_unit_delete_data[kwargs['row'] - 1]
            actual_result = self.unit_management_b.unit_delete_busniess(**kwargs)
            self.log.logger.debug(f'actucal_result:{actual_result}')
            self.assertEqual(kwargs.get('expected_result'), actual_result.get("msg"), msg=f'"{kwargs.get("case")}" 用例执行失败')
        except Exception as e:
            self.log.logger.info(e)
            raise e
        else:
            self.log.logger.info(f'"{kwargs.get("case")}"用例执行通过')


if __name__ == '__main__':
    suite = unittest.makeSuite(Test2UnitManangementQuery, 'test_1_unit_management_add')

    with open(r'E:\Auto-interface\report\test_report.html', 'wb') as fp:
        runner = HTMLTestRunner_Chart.HTMLTestRunner(
            stream=fp,
            title='My unit test',
            verbosity=2,
            description='This demonstrates the report output by HTMLTestRunner.',

        )
        runner.run(suite)
        fp.close()
