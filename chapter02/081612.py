"""
12.某电信公司的市内通话费计算标准如下：三分钟内0.2元，三分钟后每增加一分钟增加0.1元，
不足一分钟的按一分钟计算。要求编写程序，给定一个通话时间（单位：秒）计算出应收费金额。
"""
import math


def func(s):
    s = math.ceil(s/60)
    if 0 < s <= 3:
        money = 0.2
    else:
        money = round(0.2 + 0.1 * (s - 3), 2)
    print("通话%s秒，应收费：%s 元" % (s, money))


s = int(input("请输入通话时间："))
func(s)