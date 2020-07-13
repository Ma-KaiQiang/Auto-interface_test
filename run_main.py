# coding:utf8
'''
@Time    : 2020/7/8 13:30
@Author  : MaKaiQiang
@File    : run_main.py
'''
from tools.send_email import SentEmail
import HTMLTestRunner_Chart
import unittest


def run_all():
    discover = unittest.defaultTestLoader.discover(start_dir=r'E:\Auto-interface\TestCase\Infrastructure', pattern='test*.py')
    return discover


if __name__ == '__main__':
    with open(r'E:\Auto-interface\report\test_report.html', 'wb') as fp:
        runner = HTMLTestRunner_Chart.HTMLTestRunner(stream=fp, verbosity=2, title='接口自动化测试报告', description='浏览器：Chrom/平台：windows')
        runner.run(run_all())
    # SentEmail().sent_email()
