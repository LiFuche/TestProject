def find_player(sex,age):
	if isinstance(age,int):
		if sex =='f' and (10 <= age <= 12):
			return 1
		else:
			print("抱歉，你不满足加入球队的条件~")
	else:
		print("年龄输入错误")

def count_player(n):
	count = i = 0
	while i < n:
		sex = input("第{0}次输入，你的性别：".format(i+1))
		age = int(input("请输入你的年龄："))
		i += 1
		#print(find_player(sex,age))
		if find_player(sex,age):
			print("恭喜你，可以加入球队~")
			count += 1
	return count

print("满足条件的总人数为：", count_player(10))