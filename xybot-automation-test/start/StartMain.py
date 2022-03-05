
import time

from tool.ExceListProcess import ExceListProcess
from pubic.Requst import Requset
from tool.DeployAnalysis import *
from tool.TestReportExcel import TestReportExcel
from tool.ExceAnalysis import ExceRead
from tool.Log import Log
from pubic.Assertion import Assertion
import json



class StartMain():
    def __init__(self):
        pass

    def startmain(self):
        long_pass = 0
        long_failed = 0
        elp = ExceListProcess()#调用源数据处理模块类
        rqt = Requset()#调用请求类
        da = DeploAnalysis()#调用配置文件类



        # trh = TestReporHtml("影刀接口测试报告")
        tre = TestReportExcel()

        start_time = time.strftime("%Y-%m-%d %H-%M-%S")
        log = Log(start_time)#调用日志类

        ea = ExceRead()
        sheet_list = ea.obtain_sheet()
        # print(sheet_list)
        #解析配置
        str_url = da.readtext("../tool/ConfigurationDeploy.ini")
        data_user = da.readtext("../tool/ConfigurationUser.ini")
        # print(str_url,data_user)
        for i in range(len(sheet_list)):#根据sheet表遍历
            # rf = Reflex()
            at = Assertion()
            skip = 0  # 跳过数
            sheetnum = i#记录表下标
            data_list = ea.start(sheet_list[i])
            data_list_process = elp.start(data_list)
            # print(data_list_process)


            list_excel = data_list_process

            for i in range(1,len(list_excel)):
                ab_jud = 1#用于判断是否出现异常，1非异常，0异常，默认非异常
                print("编号：%s 用例：%s\n"%(list_excel[i][0],list_excel[i][8]))
                log.log("编号：%s 用例：%s\n"%(list_excel[i][0],list_excel[i][8]))
                if list_excel[i][13] == "Y" or list_excel[i][13] == "yes":#判断是否需要跳过
                    print("")
                    # log.log("\n")
                    print("跳过该行用例")
                    log.log("跳过该行用例\n")
                    skip +=1
                    print("")
                    log.log("\n")
                    continue
                else:
                    if list_excel[i][14] == "Y" or list_excel[i][13] == "yes":#判断是否需要cookies
                        print("获取cookies")
                        log.log(" 获取cookies\n")
                        method = "post"
                        strtoke_url = str_url["环境"] + "oauth/token"
                        headers = {'Authorization': 'Basic Y2xpZW50Ok5ZSTRDRk9HUVZkOE5adWs='}

                        data = data_user
                        data_json,ab_jud = rqt.call_interface(method=method,url=strtoke_url,headers=headers,data=data)#调用登录函数获取cookies
                        # print(data_json,ab_jud)
                        log.log("  cookies获取-->:\n    返回值：%s\n    返回状态：%s\n"%(data_json,ab_jud))
                        if ab_jud == 1:#判断是否出现异常
                            try:
                                data_dic = json.loads(data_json)
                                headers_token = "Bearer %s"%(data_dic["access_token"])#将token组合成heraders需要的格式
                                list_excel[i][5] = {"authorization":headers_token }#将cookies加入响应头，
                                # print("开始")
                                print("请求头数据：",list_excel[i][5])
                                # print("结束")
                            except:
                                text1 = data_json
                        else:
                            text1 = data_json

                        pass
                    if ab_jud == 1:
                        list_excel[i][4] =str_url["环境"]+list_excel[i][4]#获取配置文件的url和excel位置进行拼接为新url
                        # print("----接口参数---","请求类型：",list_excel[i][2],"请求地址：",list_excel[i][4],"请求头：",list_excel[i][5],"请求数据：",list_excel[i][7],"地址参数",list_excel[i][6],"-------")
                        # print(list_excel[i])
                        if '[' in list_excel[i][7] or '{' in list_excel[i][7]:#判断参数是否是json类型的字符串
                            list_excel[i][7] = json.loads(list_excel[i][7])
                            # print("类型：",type(list_excel[i][7]),list_excel[i][7])
                        log.log(" 传送数据：{\n  请求方法：%s\n  请求地址：%s\n  请求头：%s\n  请求参数：%s\n  地址参数：%s\n  }\n" % (list_excel[i][2],list_excel[i][4],list_excel[i][5],list_excel[i][7],list_excel[i][6]))
                        text1,ab_jud= rqt.call_interface(list_excel[i][2],list_excel[i][4],list_excel[i][5],list_excel[i][7],list_excel[i][6])#调用接口返回调用后的结果，以及是否是异常结果
                        # print("最后结果",text1,ab_jud)
                        if ab_jud == 1:#判断接口调用是否异常
                            if text1 != "":
                                text1 = json.loads(text1)#将返回的字符串通过json转换成字典。



                    # actual,try_data,result = rf.start(list_excel[i][1],text1,ab_jud,list_excel[i][8])

                    # if hasattr(rf,list_excel[i][1]):#反射
                    #     # print(getattr(Reflex,list_excel[i][1]))
                    #     # print(Reflex.token)
                    #     # actual,try_data,result = getattr(rf,list_excel[i][1])(text1,ab_jud,list_excel[i][8])
                    #

                    print("  断言前-->:\n","   模块：%s\n    接口返回：%s\n    异常状态：%s\n    预期结果：%s"%(list_excel[i][1], text1, ab_jud, list_excel[i][9]))
                    log.log("  断言前-->:\n    模块：%s\n    接口返回：%s\n    异常状态：%s\n    预期结果：%s\n"%(list_excel[i][1], text1, ab_jud, list_excel[i][9]))
                    actual, try_data, result = at.start(list_excel[i][1], text1, ab_jud, list_excel[i][9])
                    print("  回填值-->:\n", "   是否通过:%s\n    实际结果：%s\n    异常：%s"%(result, actual, try_data))
                    log.log("  回填值-->:\n    是否通过:%s\n    实际结果：%s\n    异常：%s\n"%(result, actual, try_data))



                    #回写数据，生成excel测试报告
                    #结果回填
                    print("sheet页：%s"%(sheetnum))

                    tre.add_copy_excel(i, 10, actual, sheetnum)
                    tre.add_copy_excel(i,11,result,sheetnum)
                    tre.add_copy_excel(i, 12,try_data,sheetnum)

                    print("")
                    log.log("\n")


                    # print(actual,try_data,result)
                    # if str1 == list_excel[i][9]:
            print("本次执行共计：%s条用例，其中成功%s条，跳过%s条，失败%s条"%(skip+at.adopt+at.fail,at.adopt,skip,at.fail))
            tre.add_copy_excel(len(list_excel)+3,4,"本次执行共计：%s条用例，其中成功%s条，跳过%s条，失败%s条"%(skip+at.adopt+at.fail,at.adopt,skip,at.fail),sheetnum)
            tre.save_excel()#保存测试报告
            print("-----------------------------------------------")
            log.log("-----------------------------------------------\n")
            # return list_excel
                # print(text)



if __name__ == '__main__':
    sm = StartMain()
    start_time = time.strftime("%Y-%m-%d %H-%M-%S")

    sm.startmain()
    end_time = time.strftime("%Y-%m-%d %H-%M-%S")
    print(start_time,end_time)
    