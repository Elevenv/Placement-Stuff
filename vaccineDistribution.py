# https://www.codechef.com/problems/VACCINE2


def MinDays(n,d,l):
    if d == 1:
        return n
    ct = 0
    risk = 0
    NotRisk = 0
    
    for i in l:
        if i>=80 or i<=9:
            risk+=1
        else:
            NotRisk+=1
    while risk>0 or NotRisk>0:
        flag = True
        if risk!=0:
            if risk>=d:
                risk-=d
                flag = False
                ct+=1
            else:
                risk = 0
                ct+=1
                flag = False

        if flag and NotRisk!=0:
            if NotRisk>=d:
                NotRisk-=d
                ct+=1   
            else:
                NotRisk = 0
                ct+=1
    return ct

for _ in range(int(input())):
    n,d = map(int,input().split())
    l = list(map(int,input().split()))
    print(MinDays(n, d, l))
