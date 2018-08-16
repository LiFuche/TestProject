def factorial(n):
	if n > 1:
		return n * factorial(n-1)
	else:
		return 1

number = int(input("请输入一个整数:"))
print("%d的阶乘是：%s" % (number, factorial(number)))