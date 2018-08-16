# filename: practice10.py
# coding=utf-8

number = int(input("请输入一个数字:"))

if number % 3 == 0 and number % 5 == 0:
	print("%d能同时被3和5整除" % number)
else:
	print("%d不能同时被3和5整除" % number)