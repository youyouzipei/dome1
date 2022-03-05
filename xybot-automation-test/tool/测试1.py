import sys
import json
import re


# __import__(r"case.List_")
#
# di = sys.modules
# print(di)
#
# domol = sys.modules[r"case.List_"]
# print(domol)
# sys.path.append(domol)
# actual,try_data = getattr(domol,"List_")(1)
# dp = json.dumps(di)
# print()p

# d = {'s':'you','d':'are'}   #给一个字典
# j = json.dumps(d)
# print(type(j))

str1  = """
NDA协议即保密协议。
保密协议释义1755928560@qq.com
这是购卖双方开始谈生意时的第一步。根据保护对象的不同分两种：单向NDA(One-way NDA)和双向NDA(Two-way NDA)。单向保密协定只保护采购方的利益。例如你给英特尔（或其他大公司）做科研项目，就要求签定此类保密协定。双向保密协定保护双方利益，一般条款对等。
当然，如果信息的保密程度很高，那透露方可能要求在基本保密协定的基础上签订更严格的协定。例如供应商在考虑产权变更，采购方有意兼并该供应商。
那供应商就可能要求采购方签定更严格的保密协定，因为在并购谈判过程中，供应商的关键机密信息都得透露，例如利润率、主要客户、新产品开发等。这些信息完全可能被接受者用于别的用途
"""
rugen = re.search(r"[a-z]{0,1}\d{1,8}@",str1)
str2 = rugen.group()
print(str2)