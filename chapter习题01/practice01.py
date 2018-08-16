# coding=utf-8

ascii_num = int(input("please input a num(1~127):"))
if (ascii_num < 1) or (ascii_num > 127):
	print("num not in 1~127!")
else:
	print("%s--->%s" % (ascii_num,chr(ascii_num)))