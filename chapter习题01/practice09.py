# filename: practice09.py
# coding=utf-8

origin_amount = float(input("请输入购买金额:"))
if origin_amount < 0:
	print("购买金额必须大于0！")
elif origin_amount < 50:
	print("折扣为:{0},最终价格为:{1}".format(0,origin_amount))
elif origin_amount <= 100:
	final_amount = origin_amount * (1-10/100)
	print("折扣为:{0},最终价格为:{1}".format("10%",final_amount))
else:
	final_amount = origin_amount * (1-20/100)
	print("折扣为:{0},最终价格为:{1}".format("20%",final_amount))
