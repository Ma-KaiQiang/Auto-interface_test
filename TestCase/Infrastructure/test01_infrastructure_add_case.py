# coding:utf8
# '''
# @Time    : 2020/7/8 14:42
# @Author  : MaKaiQiang
# @File    : test01_infrastructure_add_case.py
# '''
import HTMLTestRunner_Chart
import unittest
import ddt
from busniess.InfrastructrueBusniess.infrastructrue_busniess import InfrastructureBusniess
from tools.get_excel_case import GetExcelCase
from tools.log import Logger
from tools.read_conf import ReadConf
from tools.replace_data import ReplaceData
import time
infrastructure_case_file = ReadConf().get_conf('INFRASTRUCTURE').get('infrastructure')
add_excel_data = GetExcelCase(infrastructure_case_file, sheetName='楼栋房屋新增').get_dict_data


@ddt.ddt
class InfrastructureCase1(unittest.TestCase):
    uuid_file = ReadConf().get_conf('INFRASTRUCTUREUUID').get('infrastructure_uuid')

    @classmethod
    def setUpClass(cls) -> None:
        cls.log = Logger()
        cls.infrastructrue_b = InfrastructureBusniess()

    @ddt.data(*add_excel_data)
    @ddt.unpack
    # @unittest.skip
    def test_1_infrastructure_add(self, **kwargs):
        try:
            col_num = kwargs.get('row') - 1
            excel_data_1 = GetExcelCase(fileName=r'E:\Auto-interface\data\infrastructure\infrastructure_case.xlsx', sheetName='楼栋房屋新增').get_dict_data[col_num]
            self.log.logger.debug(f'获取的测试数据：{excel_data_1}')
            actual_result = self.infrastructrue_b.infrastructure_add_busniess(add_excel_data, **excel_data_1)
            self.assertEqual(excel_data_1.get('expected_result'), actual_result, msg=f'"{excel_data_1.get("case")}" 用例执行失败')

        except Exception as e:
            self.log.logger.info(e)
            raise e
        else:
            self.log.logger.info(f'"{excel_data_1.get("case")}"用例执行通过')


if __name__ == '__main__':
    suite = unittest.makeSuite(InfrastructureCase1, 'test_1_infrastructure_add')
    with open(r'E:\Auto-interface\report\test_report.html', 'wb') as fp:
        runner = HTMLTestRunner_Chart.HTMLTestRunner(
            stream=fp,
            title='My unit test',
            verbosity=2,
            description='This demonstrates the report output by HTMLTestRunner.',
        )
        runner.run(suite)
        fp.close()
