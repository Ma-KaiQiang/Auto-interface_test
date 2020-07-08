# codin:utf8
'''
@Time    : 2020/7/7 14:41
@Author  : MaKaiQiang
@File    : response_fileter.py
'''
import re
from tools.log import Logger


class ResponseFilter():
    def __init__(self, ):
        self.log = Logger()

    def data_filter(self, text, uuid, name=None, group=0):
        self.log.logger.debug(f'type:{type(text)}text值：{text}')
        if group == 0:
            compile1 = re.compile(f"'[a-z]*{uuid}': '[0-9a-z]*'")
            # compile2 = re.compile(f'"{name}":"[0-9a-z]*"')
        else:
            compile1 = re.compile(f"'[a-z]*{uuid}': '([0-9a-z]*)'")
            # compile2 = re.compile(f'"{name}":"[0-9a-z]*"')

        response_uuid = compile1.findall(text)
        # response_name = compile2.findall(text)
        return response_uuid


# if __name__ == '__main__':
#     text = '{"success":true,"errCode":0,"msg":"操作成功","data":{"total":1,"list":[{"companyUuid":"114fe44eeefe44e8857e3335f066279d","companyName":"abc","companyType":"state_admin","infrastructure":[{"infrastructureUuid":"35bfa57684ae4c0a957f555c57778c6c","infrastructureUri":"测试小区/万科魅力花园","address":null}],"chargePersonName":"112","chargePersonPhone":"113","staffNum":0,"createTime":"2020-07-07 13:55:58","remarks":"","version":0,"picture":""}]}}'
#     r = ResponseFilter(text)
#     a, c = r.data_filter('Uuid', 'companyName', 1)
#     print(a, c)
