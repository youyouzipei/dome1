'''
获取用户信息断言模块
接口：api/v1/user/info/rich
入参：
    空
出参


'''

class Rich():
    adopt = 0  # 通过次数
    fail = 0  # 失败次数
    def __init__(self):
        pass

    def case(self,dic):
        """
        断言方法
        :param dic:调用接口返回的数据或者异常
        :return:实际结果，异常详情，
        """
        actual = None
        try_data = None
        # print(dic["code"],dic["data"]['userBenefit']['userUuid'])
        if dic["code"] ==  200 and dic["data"]["userUuid"] == "2d782fde-c14c-4b56-a511-f82496427fba":
            actual = "获取成功"
        else:
            actual = "获取失败"
            try_data = "返回值数据与预期不匹配"


        return actual,try_data