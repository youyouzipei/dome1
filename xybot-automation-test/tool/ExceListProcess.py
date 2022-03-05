'''

对源数据进行处理：将excel取出来的数据，按照接口所需要的方式传送
'''

from tool.DataProcess import *
import copy

class ExceListProcess():
    def __init__(self):
        pass

    def start(self,data_list):

        data_list = data_list
        data_list_j = copy.deepcopy(data_list)


        dp = DataProcess()

        for i in range(1,len(data_list_j)):
            # lis_new=[]
            # lis_new1 = []
            # print(data_list_j[i])
            for j in range(len(data_list_j[i])):
                dic_j={}
                if '[' in data_list_j[i][j] or '{' in data_list_j[i][j]:#如果数据包含了[]{}就不进行切割处理
                    pass
                else:
                    if "\n" in data_list_j[i][j]:
                        lis_c_j = dp.data_split("\n",data_list_j[i][j])
                        # print(lis_c_j)
                        for x in range(len(lis_c_j)):
                            if ":"in lis_c_j[x]:
                                lis_data_c = dp.data_split(':', lis_c_j[x])
                                dic_j.setdefault(lis_data_c[0], lis_data_c[1])
                    if ":" in data_list_j[i][j]:
                        lis_data_c = dp.data_split(':', data_list_j[i][j])
                        dic_j.setdefault(lis_data_c[0], lis_data_c[1])

                    if len(dic_j) != 0:
                        data_list_j[i][j] = dic_j

        return data_list_j
        # print(data_list_j)
        # print(data_list)
        #
        # for i in range(1,len(data_list)):
        #     # lis_new=[]
        #     # lis_new1 = []
        #
        #     #对数据处理，将请求头，请求参数转换成接口传参所需要的字典格式
        #     lis_c = dp.data_split('\n',data_list[i][5])#将数据安装\n切割
        #     #编列切割后的数据
        #     dic={}#将每一组数据添加到该字典
        #
        #     for j in lis_c:
        #         if ":" in j:
        #             lis_data_c = dp.data_split(':',j)
        #             dic.setdefault(lis_data_c[0],lis_data_c[1])
        #             # lis_new.append(dic)
        #     data_list[i][5] = dic
        #
        #
        #     lisc_c1 = dp.data_split("\n",data_list[i][6])
        #     dic1 = {}
        #     for x in lisc_c1:
        #         if ":" in x:
        #             lis_data_c1 = dp.data_split(":",x)
        #             dic1.setdefault(lis_data_c1[0],lis_data_c1[1])
        #             # lis_new1.append(dic1)
        #     data_list[i][6] = dic1

        return data_list

if __name__ == '__main__':
    elp = ExceListProcess()
    ls = [['用例编号', '模块', '请求方式', '预置条件', '请求地址', '请求头', '地址参数', '参数', '用例', '预期结果', '实际结果', '是否通过', '异常', '是否跳过', '是否保持cookies'], ['begin_token_001', 'token', 'post', '', 'oauth/token', 'Authorization:Basic Y2xpZW50Ok5ZSTRDRk9HUVZkOE5adWs=', '', 'username:ceshi2@ydcs@@enterprise\npassword:Cs123456\ngrant_type:password\nclientVersion:4.2.0\nscope:all\nlogin_type:remind\nhostname:DESKTOP-KMLBQJP\nwindowsAccount:DESKTOP-KMLBQJP\\悠悠子佩', '用户名正确、密码正确，登录成功', '登录成功', '', '', '', 'Y', ''], ['begin_token_002', 'token', 'post', '', 'oauth/token', 'Authorization:Basic Y2xpZW50Ok5ZSTRDRk9HUVZkOE5adWs=123', '', 'username:ceshi21@ydcs@@enterprise\npassword:Cs123456\ngrant_type:password\nclientVersion:4.2.0\nscope:all\nlogin_type:remind\nhostname:DESKTOP-KMLBQJP\nwindowsAccount:DESKTOP-KMLBQJP\\悠悠子佩', '用户名错误、密码正确，登录失败', '登录失败', '', '', '', 'Y', ''], ['begin_token_003', 'token', 'post', '', 'oauth/token1231', 'Authorization:Basic Y2xpZW50Ok5ZSTRDRk9HUVZkOE5adWs=', '', 'username:ceshi2@ydcs@@enterprise\npassword:Cs1234561\ngrant_type:password\nclientVersion:4.2.0\nscope:all\nlogin_type:remind\nhostname:DESKTOP-KMLBQJP\nwindowsAccount:DESKTOP-KMLBQJP\\悠悠子佩', '用户名正确、密码错误，登录失败', '登录失败', '', '', '', 'Y', ''], ['begin_token_004', 'token', 'get', '', 'oauth/token', 'Authorization:Basic Y2xpZW50Ok5ZSTRDRk9HUVZkOE5adWs=', '', 'username:ceshi21@ydcs@@enterprise\npassword:Cs1234561\ngrant_type:password\nclientVersion:4.2.0\nscope:all\nlogin_type:remind\nhostname:DESKTOP-KMLBQJP\nwindowsAccount:DESKTOP-KMLBQJP\\悠悠子佩', '用户名错误、密码正确，登录失败', '登录失败', '', '', '', 'Y', ''], ['begin_token_005', 'token', 'post', '', 'oauth/token', 'Authorization:Basic Y2xpZW50Ok5ZSTRDRk9HUVZkOE5adWs=', '', 'username:ceshi2@ydcs@@enterprise\npassword:Cs123456\ngrant_type:password\nclientVersion:4.2.0\nscope:all\nlogin_type:remind\nhostname:DESKTOP-KMLBQJP\nwindowsAccount:DESKTOP-KMLBQJP\\悠悠子佩', '用户名错误、密码正确，登录失败', '登录失败', '', '', '', 'Y', ''], ['begin_rich_001', 'rich', 'get', '', 'api/v1/user/info/rich', '', '', '', '登录，获取客户信息', '获取成功', '', '', '', 'Y', 'Y'], ['begin_rich_002', 'rich', 'get', '', 'api/v1/user/info/rich', '', '', '', '未登录，获取客户信息', '获取失败', '', '', '', 'Y', ''], ['begin_querybykey_user_001', 'queryByKey_user', 'get', '', 'api/v1/user/config/queryByKey', '', 'configKey:user_settings', '', '获取用户产品相关配置', '获取成功', '', '', '', 'Y', 'Y'], ['begin_queryByKey_my_001', 'queryByKey_my', 'get', '', 'api/v1/user/config/queryByKey', '', 'configKey:my_favorite_activities', '', '', '获取成功', '', '', '', 'Y', 'Y'], ['begin_queryByKey_general_001', 'queryByKey_general', 'get', '', 'api/v1/user/config/queryByKey', '', 'configKey:general_error_handling_rules', '', '获取用户配置错误信息', '获取成功', '', '', '', 'Y', 'Y'], ['begin_queryByKey_quick_001', 'queryByKey_quick', 'get', '', 'api/v1/user/config/queryByKey', '', 'configKey:quick_plates', '', '获取、轮盘信息', '获取成功', '', '', '', 'Y', 'Y'], ['begj_list_001', 'list', 'post', '', '/api/v1/robot/quick/plate/list', '', '{"taskCodeList":["invite_win_plant_level1","invite_win_plant_level2","send_vip_invite_register"],"userActiviyStatus":""}', '', '', '', '', '', '', '', '']]

    print(elp.start(ls))
