"""
配置文件读取,以及处理
"""
from tool.DataProcess import *

class DeploAnalysis:
    def __init__(self):

        pass

    def readtext(self,position):
        """

        :param position: 文件位置和文件名
        :return:
        """
        dp = DataProcess()
        with open(position,"r",encoding="utf8") as f:
            text_data = f.read()
            text_dic = {}
            if "\n" in text_data:
                text_list = dp.data_split("\n",text_data)
                for i in text_list:
                    if ":" in i:
                        text_data_i = i.split(":",1)
                        text_dic.setdefault(text_data_i[0],text_data_i[1])
                # print(text_dic)
            return text_dic


if __name__ == '__main__':
    da = DeploAnalysis()
    da.readtext("ConfigurationDeploy.ini")