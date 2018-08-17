# coding:utf-8

# filename:081501.py
"""1.求10以内所有数字平方之和"""
result = 0
for i in range(1, 11):
    result += i**2
print("10以内所有数字平方之和为:", result)
