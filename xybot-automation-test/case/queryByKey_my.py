"""

"""

class queryByKe_my():
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
        if dic["code"] ==  200 and dic["success"] == True:
            actual = "获取成功"
        else:
            actual = "获取失败"
            try_data = "返回值数据与预期不匹配"


        return actual,try_data