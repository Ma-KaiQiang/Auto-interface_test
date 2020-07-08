from configparser import ConfigParser
from tools.log import Logger



class WriteConf():
    def __init__(self):
        self.config_parser = ConfigParser
        self.log = Logger()

    def res_json_parsing(self, datas):
        """
        写入配置操作
        :param datas: 需要传入写入的数据
        :param filename: 指定文件名
        :return:
        """
        self.log.logger.debug('开始解析数据')
        sections = {}
        for data in datas.values():
            if isinstance(data, dict):
                self.log.logger.debug(f'{data.keys()}')
                if 'token' in data.keys():
                    sections['TOKEN'] = data['token']
                    self.log.logger.debug(f'{sections["TOKEN"]}')
                for adminUser in data.values():
                    if 'logUuid' in adminUser.keys():
                        sections['LOGUUID'] = {"logUuid": adminUser['logUuid']}
                    if 'useruuid' in adminUser.keys():
                        sections['USERUUID'] = {"useruuid": adminUser['useruuid']}
                    if isinstance(adminUser, dict):
                        for projects in adminUser.values():
                            if isinstance(projects, list):
                                lenth = len(projects) - 1
                                while lenth >= 0:
                                    sections[f'PROJECTUUID{lenth}'] = {'projectUuid': projects[lenth].get('projectUuid')}
                                    lenth -= 1
        return sections

    def write_conf(self, datas, filename=r'E:\Auto-interface\conf\token.ini'):
        config = ConfigParser()  # 1.创建配置解析器---与写入配置操作一致
        sections = self.res_json_parsing(datas)
        for key in sections.keys():
            config[key] = sections[key]  # config 类似于一个空字典
            with open(filename, "w") as file:  # 保存到哪个文件filename=需要指定文件名
                config.write(file)

        self.log.logger.debug('token信息写入到token.ini文件')

# if __name__ == '__main__':
#     w = WriteConf()
#     sec = w.write_conf(filename=r'E:\Auto-interface\conf\token.ini')
#     print(sec)
