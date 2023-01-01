# https://www.codechef.com/problems/EVMHACK


def winner(a,b,c,p,q,r):
    # sum1 = a+b+c
    sum2 = (p+q+r)/2
    # print(sum2)

    if (a+b+p)>sum2 or (a+b+q)>sum2 or (a+b+r)>sum2 or (p+b+c)>sum2 or (q+b+c)>sum2 or (r+b+c)>sum2 or (a+p+c)>sum2 or (a+q+c)>sum2 or (a+r+c)>sum2:
        return "YES"
    return "NO"


for _ in range(int(input())):
    a,b,c,p,q,r = map(int,input().split())
    print(winner(a, b, c, p, q, r))
