'''
获取
'''

class queryByKe_user():
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
        if dic["code"] ==  200 and dic["data"]['userBenefit']['userUuid'] ==  "6772d4d3-3778-4a24-b4c3-a6b9a88c808c" and dic["data"]["name"]=="ceshi2@ydcs" and dic["data"]["userBenefit"]["userGrade"]=="enterprise":
            actual = "获取成功"
        else:
            actual = "获取失败"
            try_data = "返回值数据与预期不匹配"


        return actual,try_data