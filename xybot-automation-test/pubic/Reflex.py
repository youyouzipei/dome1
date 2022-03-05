"""
反射类：用于反射调用
"""


from case.Token import Token
from case.Rich import Rich
from case.queryByKey_user import queryByKe_user
from case.queryByKey_my import queryByKe_my
from case.queryByKey_general import queryByKey_general
from case.queryByKey_quick import queryByKey_quick
from case.List_ import list
class Reflex():
    def __init__(self):
        pass

    def Rich(self,dic):
        ri = Rich()
        actual, try_data = ri.case(dic)
        return actual, try_data
        pass

    def Token(self,dic):
        tk = Token()
        actual, try_data = tk.case(dic)
        return actual, try_data

    def queryByKey_user(self,dic):
        qbku  = queryByKe_user()
        actual, try_data = qbku.case(dic)
        return actual, try_data

    def queryByKey_my(self,dic):
        qbkm = queryByKe_my()
        actual, try_data = qbkm.case(dic)
        return actual, try_data

    def queryByKey_general(self,dic):
        qbkg = queryByKey_general()
        actual, try_data = qbkg.case(dic)
        return actual, try_data

    def queryByKey_quick(self,dic):
        qbkq = queryByKey_quick()
        actual, try_data = qbkq.case(dic)
        return actual, try_data

    def List_(self,dic):
        ls = list()
        actual, try_data = ls.case(dic)
        return actual, try_data