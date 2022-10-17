# https://www.codechef.com/submit/CHNGIT
# Change it code chef Problem

for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    ctMax = 0
    for i in l:
        if l.count(i)>ctMax:
            ctMax = l.count(i)
    print(n-ctMax)