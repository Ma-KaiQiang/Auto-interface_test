# coding:utf8
# '''
# @Time    : 2020/7/8 14:42
# @Author  : MaKaiQiang
# @File    : test02_infrastructure_query_case.py
# '''
import unittest
import ddt
from busniess.InfrastructrueBusniess.infrastructrue_busniess import InfrastructureBusniess
from tools.get_excel_case import GetExcelCase
from tools.log import Logger
from tools.read_conf import ReadConf
from tools.replace_data import ReplaceData
import HTMLTestRunner_Chart
import time

uuid_file = ReadConf().get_conf('INFRASTRUCTUREUUID').get('infrastructure_uuid')
infrastructure_case_file = ReadConf().get_conf('INFRASTRUCTURE').get('infrastructure')
query_excel_data = GetExcelCase(infrastructure_case_file, sheetName='楼栋房屋查询').get_dict_data


@ddt.ddt
class InfrastructureQueryCase(unittest.TestCase):
    # time.sleep(20)

    @classmethod
    def setUpClass(cls) -> None:
        cls.log = Logger()
        cls.infrastructrue_b = InfrastructureBusniess()
        cls.uuid_data = GetExcelCase(uuid_file, '楼栋房屋').get_dict_data
        cls.replace_infrastructure_query = ReplaceData(query_excel_data, infrastructure_case_file, '楼栋房屋查询')
        cls.replace_infrastructure_query.replace_data_sheet(cls.uuid_data)
        cls.new_infrastructure_query_data = GetExcelCase(infrastructure_case_file, '楼栋房屋查询').get_dict_data

    @ddt.data(*query_excel_data)
    @ddt.unpack
    # @unittest.skip
    def test_infrastructure_query(self, **kwargs):
        try:
            query_data = self.new_infrastructure_query_data[kwargs.get('row') - 1]
            actual_result = self.infrastructrue_b.infrastructure_query_busniess(**query_data)
            if actual_result:
                self.log.logger.debug(f'actual_result:{actual_result}')
                self.assertEqual(kwargs.get('expected_result'), actual_result[0]['data']['list'][0]['address'], msg=f'失败用例：{kwargs.get("case")}\n服务器返回内容：'
                                                                                                          f'{actual_result[0]}\n响应时间：{actual_result[1]}\n状态码{actual_result[2]}')
            else:
                raise
        except Exception as e:
            self.log.logger.info(e)
            raise e
        else:
            self.log.logger.info(f'"{kwargs.get("case")}"用例执行通过,响应时间：{actual_result[1]},状态码{actual_result[2]}')


if __name__ == '__main__':
    suite = unittest.makeSuite(InfrastructureCase2, 'test_2_infrastructure_query')
    with open(r'E:\Auto-interface\report\test_report.html', 'wb') as fp:
        runner = HTMLTestRunner_Chart.HTMLTestRunner(
            stream=fp,
            title='My unit test',
            verbosity=2,
            description='This demonstrates the report output by HTMLTestRunner.',
        )
        runner.run(suite)
        fp.close()
