def alternate(num):
    numStr = bin(num)[2:]
    if '11' in numStr or '00' in numStr:
        return False
    else:
        return True

num = 5
print(alternate(num))