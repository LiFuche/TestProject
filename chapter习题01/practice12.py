# filename: practice12.py
# coding=utf-8

first_num = input("请输入第一个值:")
second_num = input("请输入第二个值:")
print("交换前第一个值为:%s,第二个值为:%s" % (first_num, second_num))
first_num, second_num = second_num, first_num
print("交换后第一个值为:%s,第二个值为:%s" %(first_num, second_num))
