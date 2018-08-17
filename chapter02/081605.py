"""5.计算从1到1000以内所有能被3或者17整除的数的和并输出"""
result = 0
print("1到1000以内所有能被3或者17整除的数:")
for i in range(1, 1001):
    if i % 3 == 0 and i % 17 == 0:
        result += i
        print(i, end=",")
print("\n1到1000以内所有能被3或者17整除的数的和:", result)
