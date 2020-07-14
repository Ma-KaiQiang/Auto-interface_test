# coding:utf8
'''
@Time    : 2020/7/12 6:30
@Author  : MaKaiQiang
@File    : test03_unit_management_modify.py
'''

import unittest
import ddt
from tools.get_excel_case import GetExcelCase
from tools.log import Logger
from busniess.UnitMagementBusniess.unit_magement_busniess import UnitManagementBusniess
from tools.replace_data import ReplaceData
from tools.read_conf import ReadConf
import HTMLTestRunner_Chart, time

unit_case_file = ReadConf().get_conf('UNITMANAGEMENT').get('unit_management')
unit_uuid_file = ReadConf().get_conf('UNITMANAGEMENTUUID').get('unit_management_uuid')
# 加载uuid
unit_uuid_data = GetExcelCase(unit_uuid_file, '单位管理').get_dict_data
# 加载测试数据
unit_modify_data = GetExcelCase(unit_case_file, '单位管理修改').get_dict_data


@ddt.ddt
class UnitManangementModify(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.log = Logger()
        cls.unit_management_b = UnitManagementBusniess()

    def setUp(self) -> None:
        time.sleep(1)

    @ddt.data(*unit_modify_data)
    @ddt.unpack
    # @unittest.skip
    def test_unit_management_modify(self, **kwargs):
        self.log.logger.debug(kwargs)
        try:
            actual_result = self.unit_management_b.unit_modify_busniess(**kwargs)
            self.log.logger.debug(f'actucal_result:{actual_result}')
            self.assertTrue(actual_result, f'{kwargs.get("case")}请求失败')
            self.assertEqual(kwargs.get('expected_result'), actual_result.get("msg"), msg=f'失败用例：{kwargs.get("case")}\n服务器返回内容：{actual_result}')
        except Exception as e:
            self.log.logger.info(e)
            raise e
        else:
            self.log.logger.info(f'"{kwargs.get("case")}"用例执行通过')


if __name__ == '__main__':
    suite = unittest.makeSuite(Test2UnitManangementQuery, 'test_unit_management_query')

    with open(r'E:\Auto-interface\report\test_report.html', 'wb') as fp:
        runner = HTMLTestRunner_Chart.HTMLTestRunner(
            stream=fp,
            title='My unit test',
            verbosity=2,
            description='This demonstrates the report output by HTMLTestRunner.',

        )
        runner.run(suite)
        fp.close()
