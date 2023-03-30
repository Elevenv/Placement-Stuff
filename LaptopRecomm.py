# https://www.codechef.com/problems/LAPTOPREC

def solve(l):
    d = {}
    
    for i in l:
        if i not in d:
            d[i] = 1
        else:
            d[i]+=1
    
    mx = 0
    key = 0
    print(d)
    for i in d:
        if d[i]>mx:
            mx = d[i]
            key = i
    
    ct = 0
    for i in d:
        if d[i] == mx:
            ct+=1
    if ct == 1:
        return key
    return 'CONFUSED'

for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    print(solve(l))