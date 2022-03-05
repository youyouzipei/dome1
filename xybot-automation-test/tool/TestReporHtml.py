import json


class TestReporHtml():
    def __init__(self,file_name2='new_test_configuration'):
        self.file_name1 = './test_configuration.html'
        self.file_name2 =   '../data/'+ file_name2+".html"
        with open('%s'%(self.file_name1),'r',encoding='utf-8') as f:
            self.str_data = f.read()
            # print(str_data)
            self.data={
                        "testResult":
                            [
                                # {
                                #     "caseid":"test_login_001", #用例编号
                                #     "caseModule":"login", #用例模块
                                #     "testData":"123",#测试数据
                                #     "description":"11",#用例描述
                                #     "spendTime":0.0, #测试耗时
                                #     "status":"跳过", #测试结果
                                #     "log":["去去去"]#详细信息
                                # }
                            ],
                        "testPass":2, #通过数
                        "testName":"", #测试项目
                        "testAll":2,#用例总数
                        "testFail":0,#失败数
                        "beginTime":"2020-09-16 12:57:24", #开始时间
                        "totalTime":"0h 00min 01s",#运行时间
                        "testSkip":0,#跳过数
                        "testError":0
                    }
            self.empyt()
    def empyt(self):#清空数据
        self.data['testAll']=0#用例总数
        self.data['testPass']=0#通过数
        self.data['testSkip']=0#跳过数
        self.data['testFail']=0#失败数
        self.data['beginTime']=''#开始时间
        self.data['totalTime']=''#运行时间
        self.data['testName']=''#测试项目
        self.data['testError']=''#

    def new_strop_data(self,caseid,caseModule,testData,description,spendTime,status,log):
        ls = {
                "caseid":caseid, #用例编号
                "caseModule":caseModule, #用例模块
                "testData":testData,#测试数据
                "description":description,#用例描述
                "spendTime":spendTime, #测试耗时
                "status":status, #测试结果
                "log":["%s"%(log)]#详细信息
            }

        self.data["testResult"].append(ls)
        # print(self.data)

    def implement_htlm(self,testAll,testPass,testSkip,testFail,beginTime,totalTime,testName,testError):#执行用例
        self.data['testAll']=testAll#用例总数
        self.data['testPass']=testPass#通过数
        self.data['testSkip']=testSkip#跳过数
        self.data['testFail']=testFail#失败数
        self.data['beginTime']=beginTime#开始时间
        self.data['totalTime']=totalTime#运行时间
        self.data['testName']=testName#测试项目
        self.data['testError']=testError#

        self.str_data = self.str_data.replace('$test_data','影刀接口测试')
        # print(type(self.data))
        print(str(self.data).replace("'","\""))
        self.str_data = self.str_data.replace('&data_dt','%s'%(str(self.data)))
        # print(self.str_data)

    def savehtml(self):
        with open("%s"%(self.file_name2),'w',encoding='utf8') as fp:
            fp.write(self.str_data)

if __name__ == '__main__':
    trh = TestReporHtml()
    for i in range(5):
        trh.new_strop_data("text001","登录",['test1',0,0,'admin=1'],"账号密码正常，登录成功",'0.01','成功',"None")
        trh.implement_htlm(1,1,0,0,'2019','20',"影刀接口测试",2)
    trh.savehtml()
