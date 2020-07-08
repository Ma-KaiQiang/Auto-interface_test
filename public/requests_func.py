# coding:utf8
from tools.get_excel_case import GetExcelCase
from tools.log import Logger
import requests
import json


class RequestsFunc():
    def __init__(self):
        self.log = Logger()

    def get(self, **kwargs):
        params = kwargs.get('params')
        headers = kwargs.get('headers')
        url = kwargs.get('url')
        try:
            response = requests.get(url=url, params=params, headers=headers, timeout=10)
            self.log.logger.info('当前请求方式：get 返回值：response')
            return response
        except Exception as e:
            self.log.logger.error(e)
            return False

    def post(self, **kwargs):

        params = kwargs.get('params')
        headers = kwargs.get('headers')
        url = kwargs.get('url')
        body = kwargs.get('body')
        json_ = kwargs.get('json')
        self.log.logger.debug(kwargs)
        try:
            response = requests.post(url=url, params=params, headers=headers, data=body, json=json_, timeout=10)
            self.log.logger.info(f'当前请求方式：post 返回值：response {response.text}')
            return response
        except Exception as e:
            self.log.logger.error(e)
            return False

    def put(self, **kwargs):
        params = kwargs.get('params')
        headers = kwargs.get('headers')
        url = kwargs.get('url')
        body = kwargs.get('body')
        json_ = kwargs.get('json')
        try:
            response = requests.put(url=url, params=params, headers=headers, data=body, json=json_, timeout=10)
            self.log.logger.info('当前请求方式：put 返回值：response')
            return response
        except Exception as e:
            self.log.logger.error(e)
            return False

    def delete(self, **kwargs):
        params = kwargs.get('params')
        headers = kwargs.get('headers')
        url = kwargs.get('url')
        body = kwargs.get('body')
        json_ = kwargs.get('json')
        try:
            response = requests.delete(url=url, params=params, headers=headers, data=body, json=json_, timeout=10)
            self.log.logger.info('当前请求方式：delete 返回值：response')
            self.log.logger.info(f'response:{response.text}')
            return response
        except Exception as e:
            self.log.logger.error(e)
            return False


if __name__ == '__main__':
    g = GetExcelCase()
    d = g.get_dict_data
    r = RequestsFunc()
    res = r.post(**d[0])
    a = json.loads(res.text)
