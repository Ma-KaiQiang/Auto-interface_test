# coding:utf8
import unittest
import ddt
import HTMLTestRunner_Chart
from tools.get_excel_case import GetExcelCase
from tools.log import Logger
from tools.write_conf import WriteConf
from busniess.InfrastructrueBusniess.infrastructrue_busniess import InfrastructureBusniess

# 此处后续还需使用其他复杂度更低的方式进行,比如获取工作表的有效行数造成迭代器放入ddt.data()
add_excel_data = GetExcelCase(fileName=r'E:\Auto-interface\data\infrastructure\infrastructure_case.xlsx', sheetName='楼栋房屋新增').get_dict_data
query_excel_data = GetExcelCase(fileName=r'E:\Auto-interface\data\infrastructure\infrastructure_case.xlsx', sheetName='楼栋房屋查询').get_dict_data

num = 0


@ddt.ddt
class InfrastructureCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.log = Logger()
        cls.infrastructrue_b = InfrastructureBusniess()

    @ddt.data(*add_excel_data)
    @ddt.unpack

    def test_infrastructure_add(self, **kwargs):
        self.log.logger.debug(kwargs)
        try:
            self.log.logger.debug(f"kwrow:{kwargs['row']}")
            excel_data_1 = GetExcelCase(fileName=r'E:\Auto-interface\data\infrastructure\infrastructure_case.xlsx', sheetName='楼栋房屋新增').get_dict_data[num]
            self.log.logger.debug(f'获取的测试数据：{excel_data_1}')
            actual_result = self.infrastructrue_b.infrastructure_add_busniess(add_excel_data, **excel_data_1)
            self.assertEqual(excel_data_1.get('expected_result'), actual_result, msg=f'"{excel_data_1.get("case")}" 用例执行失败')
        except Exception as e:
            self.log.logger.info(e)
            raise e
        else:
            self.log.logger.info(f'"{excel_data_1.get("case")}"用例执行通过')

    @ddt.data(*query_excel_data)
    @ddt.unpack
    @unittest.skip
    def test_infrastructure_query(self, **kwargs):
        self.log.logger.debug(kwargs)
        try:
            excel_data_1 = GetExcelCase(fileName=r'E:\Auto-interface\data\infrastructure\infrastructure_case.xlsx', sheetName='楼栋房屋查询').get_dict_data[num]
            self.log.logger.debug(f'获取的测试数据：{excel_data_1}')
            actual_result = self.infrastructrue_b.infrastructure_query_busniess(query_excel_data, **excel_data_1)
            self.assertTrue(actual_result, '请求失败')
            self.assertEqual(excel_data_1.get('expected_result'), actual_result, msg=f'{excel_data_1.get("case")}用例执行失败')
        except Exception as e:
            self.log.logger.info(e)
            raise e
        else:
            self.log.logger.info(f'"{excel_data_1.get("case")}"用例执行通过')

    def tearDown(self) -> None:
        global num
        num += 1


if __name__ == '__main__':
    suite = unittest.makeSuite(InfrastructureCase, 'test_infrastructure_add')
    with open(r'E:\Auto-interface\report\test_report.html', 'wb') as fp:
        runner = HTMLTestRunner_Chart.HTMLTestRunner(
            stream=fp,
            title='My unit test',
            verbosity=2,
            description='This demonstrates the report output by HTMLTestRunner.',
        )
        runner.run(suite)
        fp.close()
