"""10.给定一个整数n，判断是否是质数（质数是只能被1和它自身整除的数）"""
import math


def is_prime(n):
    # 对1，2，3的处理
    if n == 1:
        return False
    elif n == 2 or n == 3:
        return True
    # 不在6的倍数两侧，一定不是素数
    elif n % 6 != 1 and n % 6 != 5:
        return False
    # 在6的倍数两侧，也不一定就是素数
    for i in range(5, int(math.sqrt(n))+1, 6):
        if n % i == 0 or n % (i+2) == 0:
            return False
    # 其他的都是素数
    return True


n = int(input("please input n:"))
print("%s是素数:%s" % (n, is_prime(n)))

