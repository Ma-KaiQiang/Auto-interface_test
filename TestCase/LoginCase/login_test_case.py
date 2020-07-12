# coding:utf8

from public.response_func import ResponseFunc
from tools.get_excel_case import GetExcelCase
from tools.write_conf import WriteConf
from tools.log import Logger
from pprint import pprint
import unittest
import ddt

import HTMLTestRunnerCN


@ddt.ddt
class LoginTestCase(unittest.TestCase):
    excel_data = GetExcelCase(fileName=r'E:\Auto-interface\data\login\login_case.xlsx', sheetName='单位管理新增').get_dict_data

    @classmethod
    def setUpClass(cls) -> None:
        cls.log = Logger()
        cls.res = ResponseFunc()
        cls.write_c = WriteConf()

    # # 后续实现
    # def setUp(self) -> None:
    #     self.log.logger.info('前置条件')

    @ddt.data(*excel_data)
    @ddt.unpack
    def test_01(self, **args):
        try:
            res = self.res.method(**args)
            self.log.logger.debug(res)
            self.assertEqual(args.get('expected_result'), res.get('msg'), msg=f'"{args.get("case")}" 用例执行失败')
            if res.get('msg') == '操作成功':
                self.log.logger.info('登录成功，token信息更新至token.ini文件')
                self.write_c.write_conf(res)
        except Exception as e:
            self.log.logger.info(e)
            raise e
        else:
            self.log.logger.info(f'"{args.get("case")}"用例执行通过')
    # def tearDown(self) -> None:
    #     self.log.logger.info('后置条件执行')


if __name__ == '__main__':
    suite = unittest.makeSuite(LoginTestCase, 'test')
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
