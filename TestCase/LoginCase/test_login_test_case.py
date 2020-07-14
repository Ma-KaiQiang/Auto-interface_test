# coding:utf8
'''
@Time    : 2020/7/7 9:30
@Author  : MaKaiQiang
@File    : test_login_test_case.py
'''
from public.response_func import ResponseFunc
from tools.get_excel_case import GetExcelCase
from tools.write_conf import WriteConf
from tools.log import Logger
import unittest
import ddt

import HTMLTestRunner_Chart

excel_data = GetExcelCase(fileName=r'E:\Auto-interface\data\login\login_case.xlsx', sheetName='云平台登录').get_dict_data


@ddt.ddt
class LoginTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.log = Logger()
        cls.res = ResponseFunc()
        cls.write_c = WriteConf()

    @ddt.data(*excel_data)
    @ddt.unpack
    def test_login(self, **kwargs):
        try:
            res = self.res.method(**kwargs)
            if res:
                self.log.logger.debug(res)
                self.assertEqual(kwargs.get('expected_result'), res[0].get('msg'), msg=f'\n失败用例：{kwargs.get("case")}\n服务器返回内容：{res[0]}\n响应时间：{res[1]}\n状态码：{res[2]}')
                if res[0].get('msg') == '操作成功':
                    self.log.logger.info('登录成功，token信息更新至token.ini文件')
                    self.write_c.write_conf(res[0])
            else:
                raise
        except Exception as e:
            self.log.logger.info(e)
            raise e
        else:
            self.log.logger.info(f'"{kwargs.get("case")}"用例执行通过,响应时间：{res[1]},状态码{res[2]}')


if __name__ == '__main__':
    suite = unittest.makeSuite(LoginTestCase, 'test*')
    with open(r'E:\Auto-interface\report\test_report.html', 'wb') as fp:
        runner = HTMLTestRunner_Chart.HTMLTestRunner(
            stream=fp,
            title='My unit test',
            verbosity=2,
            description='This demonstrates the report output by HTMLTestRunner.',
        )
        runner.run(suite)
        fp.close()
