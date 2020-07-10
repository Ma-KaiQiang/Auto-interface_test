# coding:utf8
import unittest
import ddt
import HTMLTestRunner_Chart
from tools.get_excel_case import GetExcelCase
from tools.log import Logger
from tools.write_conf import WriteConf
from busniess.InfrastructrueBusniess.infrastructrue_busniess import InfrastructureBusniess

excel_data = GetExcelCase(sheetName='楼栋房屋').get_dict_data

num = 0


@ddt.ddt
class InfrastructureCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.log = Logger()
        cls.infrastructrue_b = InfrastructureBusniess(excel_data)

    @ddt.data(*excel_data)
    @ddt.unpack
    def test_infrastructure_add(self, **kwargs):
        self.log.logger.debug(kwargs)
        try:
            excel_data_1 = GetExcelCase(sheetName='楼栋房屋').get_dict_data[num]
            self.log.logger.debug(f'获取的测试数据：{excel_data_1}')
            response = self.infrastructrue_b.infrastructure_busniess(**excel_data_1)
            self.assertEqual(excel_data_1.get('result'), response, msg=f'"{excel_data_1.get("case")}" 用例执行失败')
        except Exception as e:
            self.log.logger.info(e)
            raise e
        else:
            self.log.logger.info(f'"{kwargs.get("case")}"用例执行通过')

    def tearDown(self) -> None:
        global num
        num += 1


if __name__ == '__main__':
    suite = unittest.makeSuite(InfrastructureCase, 'test*')

    with open(r'E:\Auto-interface\report\test_report.html', 'wb') as fp:
        runner = HTMLTestRunner_Chart.HTMLTestRunner(
            stream=fp,
            title='My unit test',
            verbosity=2,
            description='This demonstrates the report output by HTMLTestRunner.',
        )
        runner.run(suite)
        fp.close()
