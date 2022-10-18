# https://www.codechef.com/submit/MASKPOL
# Mask Policy

for _ in range(int(input())):
    n,a = map(int,input().split())
    ans = n-a

    print(a) if ans>a else print(ans)