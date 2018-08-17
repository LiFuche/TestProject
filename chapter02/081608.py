"""﻿8.计算1到100以内能被7整除但不是偶数的数的个数。"""
count = 0
for i in range(1, 101):
    if i % 7 == 0 and i % 2 == 1:
        count += 1
print("1到100以内能被7整除但不是偶数的数的个数:", count)
