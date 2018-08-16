#practice14.py
max_oil = int(input("你车的油箱的最大容量是(L)："))
oil_percentage = float(input("目前油箱还剩几成油(百分比)："))
per_kw = int(input("你车每升油可以走多远(km)："))

remain_oil = max_oil * oil_percentage
remain_km = (remain_oil - 5) * per_kw / 200

if remain_km < 1:
    print("你剩余油量不能开到下一个加油站了，需要现在加油！")
else:
        print("你可在接下来第%d个加油站加油！" % int(remain_km))