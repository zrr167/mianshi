"""
业务层代码
"""


class Calculate:
    def cal(self, **k):
        res = []
        s=[i for i in k.values()]
        data = [x for x in s if type(x) == int]
        if len(data) == 3:
            if sum(data) != 5:
                return "数据不符合规则"
            elif sum(data) == 5:
                for i in s:
                    if i > 0:
                        res.append(i)
                return res
        elif len(data) != 3:
            return "数据类型错误"



if __name__ == '__main__':
    cc = Calculate()
    k={'a':1,'b':2,'c':3,'d':"changdu"}
    ss = cc.cal(**k)
    print(ss)



