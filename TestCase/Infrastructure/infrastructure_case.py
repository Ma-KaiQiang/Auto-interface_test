# coding:utf8
import unittest
import ddt
import HTMLTestRunnerCN
from tools.get_excel_case import GetExcelCase
from tools.log import Logger
from tools.write_conf import WriteConf
from busniess.InfrastructrueBusniess.infrastructrue_busniess import InfrastructureBusniess


@ddt.ddt
class InfrastructureCase(unittest.TestCase):
    excel_data = GetExcelCase(sheetName='楼栋房屋').get_dict_data

    @classmethod
    def setUpClass(cls) -> None:
        cls.log = Logger()
        cls.infrastructrue_b = InfrastructureBusniess()

    @ddt.data(*excel_data)
    @ddt.unpack
    def test_01(self, **kwargs):
        self.log.logger.debug(kwargs)
        try:
            response = self.infrastructrue_b.infrastructure_busniess(**kwargs)

            self.assertEqual(kwargs.get('result'), response, msg=f'"{kwargs.get("case")}" 用例执行失败')

        except Exception as e:
            self.log.logger.info(e)
            raise e
        else:
            self.log.logger.info(f'"{kwargs.get("case")}"用例执行通过')


if __name__ == '__main__':
    suite = unittest.makeSuite(InfrastructureCase,'test_01')

    with open(r'E:\Auto-interface\report\test_report.html', 'wb') as fp:
        runner = HTMLTestRunnerCN.HTMLTestRunner(
            stream=fp,
            title='My unit test',
            verbosity=2,
            description='This demonstrates the report output by HTMLTestRunner.',
            tester='makaiqiang'
        )
        runner.run(suite)
        fp.close()
