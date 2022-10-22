arr = [4,11,2,35,33,9,52,45,15]

large = 0
secLarge = 0

for i in arr:
    if i>large:
        secLarge = large
        large = i
    elif i>secLarge and i != large:
        secLarge = i
print(secLarge)