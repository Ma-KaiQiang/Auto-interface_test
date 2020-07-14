# coding:utf8
from public.requests_func import RequestsFunc
from tools.log import Logger
from tools.response_fileter_uuid import ResponseFilter
import time
import json


class ResponseFunc():
    def __init__(self):
        self.requests_func = RequestsFunc()
        self.res_filter = ResponseFilter()
        self.log = Logger()

    def method(self, text=False, **kwargs):
        self.log.logger.debug(f'请求参数：{kwargs}')
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
                return [json.loads(res.text), res.elapsed.total_seconds(), res.status_code]
            else:
                return False
        elif requests_type == 'post':
            res = self.requests_func.post(url=url, params=params, headers=headers, body=body, json=json_)
            self.log.logger.debug(f'返回响应字串:{res.text}')
            if res:
                return [json.loads(res.text), res.elapsed.total_seconds(), res.status_code]
            else:
                return False
        elif requests_type == 'put':
            res = self.requests_func.put(url=url, params=params, headers=headers, body=body, json=json_)
            if res:
                self.log.logger.debug('返回响应字串')
                return [json.loads(res.text), res.elapsed.total_seconds(), res.status_code]
            else:
                return False
        elif requests_type == 'delete':
            time.sleep(2)
            res = self.requests_func.delete(url=url, params=params, headers=headers, body=body, json=json_)
            self.log.logger.debug('返回响应字串')
            if res:

                return [json.loads(res.text), res.elapsed.total_seconds(), res.status_code]
            else:
                return [False, res.elapsed.total_seconds(), res.status_code]


if __name__ == '__main__':
    body = '{"areaName":"汤臣一品","infrastructureUri":"汤臣一品","building":true,"floor":true,"phase":true,"unit":true,"phaseCount":1}'
    headers = '{"projectUuid":"090c24d6fcd248af8b8e76c4ef8b2c74","User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36","Authorization":"bearer dc690308-4012-4408-986c-7dddc8efe203","Content-Type":"application/json"}'
    url = 'http://192.168.9.238:15000/basedata-v1/project/090c24d6fcd248af8b8e76c4ef8b2c74/initArea'

    r = ResponseFunc()
    res = r.method(url=url, body=body, headers=headers)
    print(res)
#     assert (res['msg'] == '操作成功')
