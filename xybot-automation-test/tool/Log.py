"""
日志类：
"""

class Log():
    def __init__(self,time):
        self.time = time
        pass


    def log(self,data):
        try:
            with open("../data/log/%s.txt"%(self.time),"a",encoding="utf8") as f:
                f.write(data)
        except:
            with open("../data/log/%s"%(self.time),"w",encoding="utf8") as f:
                f.write(data)

if __name__ == '__main__':
    lg = Log("2020-5-3")
    lg.log("开始----11111\n222222\n333333\n")