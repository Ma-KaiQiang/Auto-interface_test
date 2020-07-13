# coding:utf8
'''
@Time    : 2020/7/13 11:25
@Author  : MaKaiQiang
@Site    :
@File    : read_conf.py
@Software: PyCharm
'''
import configparser


class ReadConf(object):
    def __init__(self, ):
        self.cf = configparser.ConfigParser()
        self.file_path = r'E:\Auto-interface\conf\case_path.ini'

    def get_conf(self, section):
        self.cf.read(self.file_path)
        return dict(self.cf.items(section))


if __name__ == '__main__':
    r=ReadConf()
    a=r.get_conf('UNITMANAGEMENT').get('unit_management')
    print(type(a))