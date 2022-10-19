# https://www.codechef.com/submit/FRUITS
# Chef and Fruits 

for _ in range(int(input())):
    n,m,k = map(int,input().split())

    if n==m:
        print(0)
    elif n<m:
        add = n+k
        if add>=m:
            print(0)
        else:
            print(m-add)
    else:
        add = m+k
        if add>=n:
            print(0)
        else:
            print(n-add)