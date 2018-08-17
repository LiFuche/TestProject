# ﻿4.计算2的20次方。不允许用**和pow()
result = 1
for i in range(1, 21):
    result *= 2

print(result)
print(result == 2**20)

