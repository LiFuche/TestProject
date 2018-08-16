#filename:practice07.py
import math

# method1
result1 = pow(7,4)
print("method1:7*7*7*7 =", result1)

#method2
result2 = 1
for i in range(4):
	result2 *= 7
print("method2:7*7*7*7 =", result2)

#method3
result3 = i =1
while i <= 4:
	result3 *= 7
	i  += 1
print("method2:7*7*7*7 =", result3)