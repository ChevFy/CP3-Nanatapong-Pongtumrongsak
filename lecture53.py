

def vatCaculate(totalPrice) :
    result = totalPrice + (totalPrice*7/100)
    return result

inputmoney = int(input())
print(vatCaculate(inputmoney))