arr = [54,23,55,21,6,43]
# arr = [4,11,2,35,33,9,52,45,15]

small = arr[0]
secSmall = arr[0]

for i in arr:
    if i<small:
        secSmall = small
        small = i
    elif i<secSmall and i != small:
        secSmall = i
print(secSmall)