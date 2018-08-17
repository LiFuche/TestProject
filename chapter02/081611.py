"""11.给定一个n位（不超过10）的整数，将该数按位逆置，例如给定12345变成54321，12320变成02321."""


#  逆序整数
def func(num):
    if num.isdigit():
        if int(num) > 0 and int(num) < 10**10:
            print("逆序输出:", num[::-1])
        else:
            print("请输入10位以内的数字")
    else:
        print("请输入数字")


num = input("please input a number:")
func(num)
