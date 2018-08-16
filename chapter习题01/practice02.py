num = []
for i in range(4):
	num.append(int(input("please input number:")))
result = num[0] + num[1] -num[2] * num[3]
print("%d + %d - %d * %d = %d" % (num[0], num[1], num[2], num[3], result))