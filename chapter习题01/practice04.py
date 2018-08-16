# filename:practice04.py
# coding=utf-8

total_pay = 35.27 * (1+15 / 100)
average_pay = total_pay / 3
print("每个人需要付%s美元" % round(average_pay, 2))
print("每个人需要付%.2f美元" % average_pay)
print("每个人需要付{:.2f}美元".format(average_pay))