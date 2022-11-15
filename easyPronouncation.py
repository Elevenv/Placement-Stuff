# https://www.codechef.com/problems/EZSPEAK

s = 'schtschurowskia'
# s = 'apple'
vowels = ['a','e','i','o','u']
ct = 0

for i in s:
    if i not in vowels:
        ct+=1
    else:
        ct = 0
    if ct ==4:
        print("NO")
        break
else:
    print("YES")