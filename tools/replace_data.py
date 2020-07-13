# coding :utf8
'''
@Time    : 2020/7/8 18:46
@Author  : MaKaiQiang
@File    : replace_data.py
'''
from tools.write_excel import WriteExcel
from tools.get_excel_case import GetExcelCase
from tools.log import Logger
import re


class ReplaceData():
    def __init__(self, old_excel_data, write_file_name, write_sheet_name):
        self.write_excel = WriteExcel(file_name=write_file_name, sheet_name=write_sheet_name)
        self.log = Logger()
        self.old_excel_data = old_excel_data

    def replace_data(self, row, uuid=None):
        self.log.logger.debug(f'replace_row:{row}')
        # 因为old_excel_data是一个列表是从0开始取数据所以-1
        replace_col = eval(self.old_excel_data[row - 1].get('replace'))
        self.log.logger.debug(f'replace_col:{replace_col}')
        key_list = [key[0] for key in replace_col.items()]
        if "json" in key_list:
            compile_ = re.compile('[0-9a-z]{32}')
            # 获取须替换行
            col = replace_col.get('json')
            for i in col:
                old_body = self.old_excel_data[i - 2]['json']
                self.log.logger.debug(f'old_body:{old_body}')
                compile_text = compile_.search(old_body).group(0)
                new_body = old_body.replace(compile_text, eval(str(uuid))[0])
                self.write_excel.write(i, 6, new_body)
        if "url" in key_list:
            compile_ = re.compile('[0-9a-z]{32}')
            col = replace_col.get('url')
            for i in col:
                old_body = self.old_excel_data[i - 2]['url']
                self.log.logger.debug(f'old_body:{old_body}')
                # 获取末尾的uuid
                compile_text = compile_.findall(old_body)[-1]
                new_body = old_body.replace(compile_text, eval(str(uuid))[0])
                self.log.logger.debug(f'new_body:{new_body}')
                self.write_excel.write(i, 3, new_body)
        if "paramas" in key_list:
            compile_ = re.compile('[0-9a-z]{32}')
            # 获取须替换行
            col = replace_col.get('paramas')
            for i in col:
                old_body = self.old_excel_data[i - 2]['paramas']
                self.log.logger.debug(f'old_body:{old_body}')
                compile_text = compile_.search(old_body).group(0)
                new_body = old_body.replace(compile_text, eval(str(uuid))[0])
                self.write_excel.write(i, 4, new_body)

    def replace_data_sheet(self, uid_sheet):
        for case in self.old_excel_data:
            if case.get('replace'):
                replace_data = eval(case.get('replace'))
                self.log.logger.debug(f'replace_data:{replace_data}')
                key_list = [key[0] for key in replace_data.items()]
                if "json" in key_list:
                    json_uid_col = replace_data.get('json_uid_col')
                    json_uuid = eval(uid_sheet[json_uid_col - 2].get('uuid'))
                    self.log.logger.debug(f'uuid:{json_uuid}')
                    compile_ = re.compile('[0-9a-z]{32}')
                    old_json_data = case.get('json')
                    self.log.logger.debug(f'old_body:{old_json_data}')
                    compile_text = compile_.search(old_json_data).group(0)
                    new_json_data = old_json_data.replace(compile_text, json_uuid[0])
                    self.log.logger.debug(f'new_json_data:{new_json_data}')
                    self.write_excel.write(case.get('row') + 1, 6, new_json_data)
                    self.log.logger.debug('写入成功')
                if "url" in key_list:
                    url_uid_col = replace_data.get('url_uid_col')
                    self.log.logger.debug(f'uuid:{url_uid_col}')
                    url_uuid = eval(uid_sheet[url_uid_col - 2].get('uuid'))
                    self.log.logger.debug(f'uuid:{url_uuid}')
                    compile_ = re.compile('[0-9a-z]{32}')
                    old_url_data = case.get('url')
                    compile_text = compile_.findall(old_url_data)[-1]
                    new_url_data = old_url_data.replace(compile_text, url_uuid[0])
                    self.log.logger.debug(f'new_url_data:{new_url_data}')
                    self.log.logger.debug(f'replace_row:{case.get("row")}')
                    self.write_excel.write(case.get('row') + 1, 3, new_url_data)
                    self.log.logger.debug('写入成功')
                if "paramas" in key_list:
                    paramas_uid_col = replace_data.get('paramas_uid_col')
                    paramas_uid = eval(uid_sheet[paramas_uid_col - 2].get('uuid'))
                    self.log.logger.debug(f'uuid:{paramas_uid}')
                    compile_ = re.compile('[0-9a-z]{32}')
                    # 获取须替换行
                    old_paramas_data = case.get('paramas')
                    compile_text = compile_.search(old_paramas_data).group(0)
                    new_paramas_data = old_paramas_data.replace(compile_text, paramas_uid[0])
                    self.write_excel.write(case.get('row') + 1, 4, new_paramas_data)
                    self.log.logger.debug('写入成功')


if __name__ == '__main__':
    old_data = GetExcelCase(fileName=r'E:\Auto-interface\data\unit_management\unit_management_case.xlsx', sheetName='单位管理新增').get_dict_data
    uid_sheet = GetExcelCase(fileName=r'E:\Auto-interface\data\infrastructure\infrastructure_uuid.xlsx', sheetName='楼栋房屋').get_dict_data
    r = ReplaceData(old_data, write_file_name=r'E:\Auto-interface\data\unit_management\unit_management_case.xlsx', write_sheet_name='单位管理新增')
    r.replace_data_sheet(uid_sheet=uid_sheet)
