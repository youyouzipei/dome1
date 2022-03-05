import requests
import json

cont_n = 0
cont_y = 0

def request_data(params,method="get",url="http://dev-api.winrobot360.com:8079/api/v1/sys/client/checkVersion"):
    session = requests.request(method=method,url=url,params=params)
    return session.content.decode("utf8")

def assertion(data_test,data_dic,ls):
    global cont_n
    dic_da = json.loads(data_test)
    try:
        if dic_da["data"]["latestVersion"] != "4.6.8":
            print(data_dic["userUuid"],ls[1])

            cont_n+=1
        else:
            global cont_y
            cont_y+=1
    except:
        cont_n+=1
        print(data_dic["userUuid"],ls[1])



if __name__ == '__main__':

    ls = [["0bb9df7e-7545-47c9-b8f1-fbb2a1cf5224","ceshi34@csqy1-未灰度企业"],
          ["bf684d26-11dd-4073-8dd0-8283688fca67","ceshi1@csqy9-灰度企业"],
          ["684508ff-1d0c-4bff-92ae-149e7b32d463", "njwfx-70付费用户"],
          ["eda62c29-45e9-4a28-8c74-6a2ed8670e17","刚起床的男人-200灰度用户"],
          ["e25ecd96-e15b-4033-93c1-9be13bb9b603","zzh-02"],
          ["442a024d-42bc-4bce-bf2f-57c60dfa88ac","赵海峰-10"],
          ["aec2a231-b880-4825-b833-f1ec7be7a8bc","18612341232-23"],
          ["922dc8bc-360f-41aa-ba72-9a1c2b1e782b","测试4-30"],
          ["ee6f3da8-27f5-4de6-bed6-7233f4cadff2","23-40"],
          ["4779a9c6-512d-4bb2-93cd-4444720ca34e","测试-49"],
          ["ce672282-e5d6-4041-83a9-78ee091b9fc8","c680785288f8a71e-50"],#百分之20
          ["516b2267-1313-4944-ad02-402540b58592","c6c1751a6003f3bf-51"],
          ["5bb9c35c-ba39-4b4a-9b1e-b79344096815","汪凡欣-60"],
          ["72501e80-255d-4f35-b2c7-b2be5fb35463","nazuhi326-70"],
          ["b0e2f689-d1f1-44df-8170-4caf8e0a581d","4ecc1816a0462e41-81"],
          ["e071dc23-d981-4c8c-856f-06c97bd5ad65","b89a532cb1823503-90"],
          ["0d89c854-8db1-44c4-ae7d-d0431498d037","李海涛-99"],
          ["9e606f80-8f40-4f78-be17-eec1b79b7384","子佩子佩子佩子佩子佩子佩子佩子佩子佩子佩子佩子佩子佩子佩子佩-100"],#百分之40
          ["3d27a4fb-a070-43e5-8e59-75ed3d600b04","58ee840695c69884-101"],
          ["188f956d-53a9-483c-bbc5-a315ba4f8422","xingyun-118"],
          ["2996d636-e5cf-41c4-afd3-dd013b920c86","ass1123-149"],
          ["070c7415-988c-43e6-8360-6413cbd1fcf6","13112348866-150"],#百分之60
          ["1770c569-1a29-463b-b504-cae5791c4348","oooo-151"],
          ["8cfd1c44-5f5c-405b-9c7e-8dc66e6cb3c6","severus-164"],
          ["668bd483-e736-4d72-919b-b2b399b24678","刘一帆-199"],
          ["69cee46e-91e0-47d4-80b7-f57d7e5f1f17","66cac6522736e782-200"],#百分之80
          ["eaeafd58-5fd0-4157-93ce-cfef593099f5","zz-201"],
          ["261c70b8-8530-4e41-aba0-b91e9c2d4af0","水手怕水-256"]
          ]
    for i in range(len(ls)):
        data_dic={"version":"4.5.19","userUuid":ls[i][0]}

        data_test = request_data(data_dic)
        assertion(data_test,data_dic,ls[i])

    print("cont_n:%s,cont_y:%s"%(cont_n,cont_y))