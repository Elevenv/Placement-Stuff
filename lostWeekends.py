# https://www.codechef.com/submit/LOSTWKND
# Lost Weekends

for _ in range(int(input())):
    l = list(map(int,input().split()))
    n = l[-1]
    l = [x*n for x in l ]
    ans = sum(l[:len(l)-1])/(len(l)-1)
    if ans>24:
        print('Yes')
    else:
        print('No')
