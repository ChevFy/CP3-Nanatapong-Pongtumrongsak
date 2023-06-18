number = int(input())
text = ""

for i in range(number) :
    text = " "*(number-i)
    print(text , "*" * (i*2+1))


