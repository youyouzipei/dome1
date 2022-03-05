"""
登录断言模块
接口：oauth/token
入参：
    username:用户名@@enterprise
    password:密码
    grant_type:password
    clientVersion:客户端版本
    scope:all
    login_type:登录类型(force/强制登陆,remind/普通登录)
    hostname:主机名/DESKTOP-KMLBQJP
    windowsAccount:windows账户/DESKTOP-KMLBQJP\悠悠子佩


出参：

"""
# import json
# class Token():
#     adopt = 0#通过次数
#     fail = 0 #失败次数
#     def __init__(self):
#         pass
#
#     def case(self,dic,ab_jud,expect):
#         """
#         断言方法
#         :param dic:调用接口返回的数据或者异常
#         :param ab_jud:调用接口返回的状态码：1正常，0异常
#         :param expect:预期结果
#         :return:实际结果，异常详情，是否通过
#         """
#         actual = ""
#         if ab_jud == 1:
#             try:
#                 # print(dic["code"],dic["success"])
#                 try_data = None
#                 if dic["code"] ==  "2001" and dic.get('success') ==  True:
#                     actual = "登录成功"
#                 else:
#                     actual = "登录失败"
#                     try_data = dic
#             except:
#                 actual = "接口错误"
#                 try_data = "请核对接口"
#
#         else:
#             actual = "异常"
#             try_data = dic
#
#
#         if expect == actual:#判断用例是否通过
#             result = "是"
#
#         else:
#             result = "否"
#
#
#

#
#         if type(try_data) == dict:
#             try_data = json.dumps(try_data,ensure_ascii=False)#ensure_ascii=False不会使用ASCII编码,中文可以正常显示
#         if ab_jud == 1 and result == "是":#判断没有异常，且用例通过，返回异常为空
#             try_data = None
#
#         # print("结果",actual,try_data,result)
#         return actual,try_data,result


class Token():
    adopt = 0#通过次数
    fail = 0 #失败次数
    def __init__(self):
        pass

    def case(self,dic):
        """
        断言方法
        :param dic:调用接口返回的数据或者异常
        :param ab_jud:调用接口返回的状态码：1正常，0异常
        :param expect:预期结果
        :return:实际结果，异常详情，是否通过
        """
        actual = None
        try_data = None
        if dic["code"] ==  "200" and dic.get('success') ==  True:
            actual = "登录成功"
        else:
            actual = "登录失败"
            try_data = dic

        return actual,try_data