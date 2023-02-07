# cook your dish here
for _ in range(int(input())):
    n,x = map(int,input().split())
    m = 0
    for i in range(n):
        s,r = map(int,input().split())
        if s<=x:
            if r>m:
                ans = r
                m = r
    print(ans)