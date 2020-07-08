# coding:utf8
from tools.get_excel_case import GetExcelCase
from public.requests_func import RequestsFunc
from tools.log import Logger
from tools.response_fileter_uuid import ResponseFilter
import time
import json


class ResponseFunc():
    def __init__(self):
        self.get_excel = GetExcelCase()
        self.requests_func = RequestsFunc()
        self.res_filter = ResponseFilter()
        self.log = Logger()

    def method(self, text=False, **kwargs):
        case_node = kwargs.get('case')
        requests_type = kwargs.get('requests_type')
        url = kwargs.get('url')
        params = kwargs.get('paramas')
        headers = eval(kwargs.get('headers'))
        if kwargs.get('json'):
            json_ = eval(kwargs.get('json'))
        else:
            json_ = None
        if kwargs.get('body'):
            body = eval(kwargs.get('body'))
        else:
            body = None
        if requests_type == 'get':
            res = self.requests_func.get(url=url, params=params, headers=headers)
            self.log.logger.debug(f'返回响应字串:{res.text}')
            if res:
                return json.loads(res.text)
            else:
                return False
        elif requests_type == 'post':
            res = self.requests_func.post(url=url, params=params, headers=headers, body=body, json=json_)
            self.log.logger.debug(f'返回响应字串:{res}')
            if res:

                return json.loads(res.text)
            else:
                return False
        elif requests_type == 'put':
            res = self.requests_func.put(url=url, params=params, headers=headers, body=body, json=json_)
            if res:
                self.log.logger.debug('返回响应字串')
                return json.loads(res.text)
            else:

                return False
        elif requests_type == 'delete':
            time.sleep(2)
            res = self.requests_func.delete(url=url, params=params, headers=headers, body=body, json=json_)
            self.log.logger.debug('返回响应字串')
            if res:

                return json.loads(res.text)
            else:
                return False


if __name__ == '__main__':
    g = GetExcelCase()
    d = g.get_dict_data[0]
    r = ResponseFunc()
    res = r.method(**d)
    assert (res['msg'] == '操作成功')
