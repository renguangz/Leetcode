def decimalToBinary(num):
    res = []
    while num > 0:
        res.append(num % 2)
        num //= 2
    res.reverse() # 如果想要從右邊開始當第零位數
    return res