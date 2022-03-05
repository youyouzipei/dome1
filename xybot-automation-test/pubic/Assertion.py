"""
断言方法：

"""

import json
import sys

from pubic.Reflex import Reflex

class Assertion():
    adopt = 0  # 通过次数
    fail = 0  # 失败次数


    def __init__(self):

        pass


    def start(self,function,dic,ab_jud,expect):#优化
        """
        断言方法
        :param function：模块
        :param dic:调用接口返回的数据或者异常
        :param ab_jud:调用接口返回的状态码：1正常，0异常
        :param expect:预期结果
        :return:实际结果，异常详情，是否通过

        """

        # 动态加载模块
        __import__(r"case.%s"%(function))
        demol = sys.modules[r"case.%s"%(function)]#获取需要的模块
        print(demol)


        rf = Reflex()
        if ab_jud == 1:
            try:
                # print(dic["code"],dic["success"])

                try_data = None
                actual = None
                # print(ls1[i], dic, ab_jud, expect)
                if hasattr(rf,function):
                    # print(True)
                    # actual,try_data = getattr(demol,function)(dic)
                    actual,try_data=getattr(rf,function)(dic)#反射
                    # print(actual,try_data)
            except:
                if type(dic) == dict:
                    data_dic = json.dumps(dic, ensure_ascii=False)  # ensure_ascii=False不会使用ASCII编码,中文可以正常显示
                else:
                    data_dic = dic
                if "登录已过期" in data_dic:
                    actual = "登录失败"
                else:
                    actual = "数据错误"
                    try_data = dic

        else:
            actual = "异常"
            try_data = dic

        if expect == actual:  # 判断用例是否通过
            result = "是"
            self.adopt = self.adopt + 1

        else:
            result = "否"
            self.fail = self.fail + 1

        if type(try_data) == dict:
            try_data = json.dumps(try_data, ensure_ascii=False)  # ensure_ascii=False不会使用ASCII编码,中文可以正常显示
        if ab_jud == 1 and result == "是":  # 判断没有异常，且用例通过，返回异常为空
            try_data = None

            # print("结果",actual,try_data,result)
        return actual, try_data, result


    # def token(self,dic,ab_jud,expect):
    #     print("正在断言token","正确用例：%s,错误用例%s"%(self.adopt,self.fail))
    #     tk = Token()
    #     actual,try_data,result=tk.case(dic,ab_jud,expect)
    #
    #     if result == "是":
    #         self.adopt = self.adopt + 1
    #     else:
    #         self.fail = self.fail + 1
    #
    #     print("token:",result,expect,actual,try_data)
    #     return actual,try_data,result
    #
    #
    # def rich(self,dic,ab_jud,expect):
    #     print("正在断言rich","正确用例：%s,错误用例%s"%(self.adopt,self.fail))
    #     rc = Rich()
    #     actual, try_data, result = rc.case(dic, ab_jud, expect)
    #
    #
    #     if result == "是":
    #         self.adopt = self.adopt + 1
    #     else:
    #         self.fail = self.fail + 1
    #
    #     print("token:",result,expect,actual,try_data)
    #     return actual,try_data,result


if __name__ == '__main__':
    ls1 = ["token1","rich1","token1"]
    dic = {"code":"200","success":True}
    ab_jud = 1
    expect = "登录成功"
    for i in range(len(ls1)):

        Assertion().start(ls1[i],dic,ab_jud,expect)