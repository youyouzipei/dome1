"""
公共方法：请求方法
pip install requests -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
"""
import requests

class Login():
    def __init__(self):
        pass

    def call_interface(self,method,url,headers,data,params=None,cookies=None):
        """

        :param method: 请求方式：get,post
        :param headers: 请求头
        :param url: 请求地址
        :param data: 请求参数
        :param params: 地址参数
        :param cookies:

        :return:
        """
        try:
            print(method,url,headers,data)
            session = requests.request(method=method,url=url,data=data,headers=headers,params=params,cookies=cookies)
            text = session.content.decode('utf8')
        except BaseException as abnormal:
            return abnormal,0
        print(text)
        return text,1


if __name__ == '__main__':
    ret = Login()
    headers = {'Authorization': 'Basic Y2xpZW50Ok5ZSTRDRk9HUVZkOE5adWs='}
    data = {'username': 'ceshi2@ydcs@@enterprise', 'password': 'Cs123456', 'grant_type': 'password', 'clientVersion': '4.2.0', 'scope': 'all', 'login_type': 'remind', 'hostname': 'DESKTOP-KMLBQJP', 'windowsAccount': 'DESKTOP-KMLBQJP\\悠悠子佩'}
    tx = ret.call_interface('post','https://api.winrobot360.com/oauth/token',headers=headers,data=data)
    # print(tx)