# https://www.codechef.com/submit/FODCHAIN
# food chain Code chef problem


import math
for _ in range(int(input())):
    a,b = map(int,input().split())
    ct = 1
    ans = 1
    while ans!=0:
        ans = math.floor(a/b)
        if ans==0:
            break
        ct+=1
        a = ans
    print(ct)