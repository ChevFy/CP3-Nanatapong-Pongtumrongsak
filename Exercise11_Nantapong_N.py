"""
ิ  *   เคาะ 2
 ***  เคาะ 1
***** เคาะ 0
"""

number = int(input())

for i in range(number) :
    blank = " " * (number-(i+1))
    star = "*"*(i*2+1)
    print(blank + star)