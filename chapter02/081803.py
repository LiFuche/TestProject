# filename:081503.py
"""﻿3.输出9行内容，第1行输出1，第2行输出12，第3行输出123，以此类推，第9行输出123456789"""
for i in range(1,10):
    for j in range(i):
        print(j+1, end="")
    print()
