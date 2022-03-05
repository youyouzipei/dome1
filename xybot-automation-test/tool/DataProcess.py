'''
数据处理：组要对数据进行切割喝添加
'''

import re
class DataProcess():
    def __init__(self):
        pass


    def data_split(self,example,data):
        """
        字符串切割
        :param example: 按什么切割
        :param data: 切割的数据
        :return: 切割后的列表
        """
        datalist = re.split(example,data)
        return datalist

    def dic_add(self,dataone,datatwo):
        """
        将数据添加成字典
        :param dataone: 第一个数据，key
        :param datatow: 第二个数据，value
        :return:字典数据
        """
        dic = {}
        dic.setdefault(dataone,datatwo)
        return dic