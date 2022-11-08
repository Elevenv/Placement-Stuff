# https://www.codechef.com/submit/TSTROBOT
# Testing Robot


for _ in range(int(input())):
    n,x = map(int,input().split())
    s = input()
    Set = set()
    Set.add(x)
    for i in range(n):
        if s[i]=='R':
            x = x+1
            Set.add(x)
        else:
            x-=1
            Set.add(x)
    print(len(Set))