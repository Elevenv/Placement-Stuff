# https://www.codechef.com/submit/S02E10
# The One with Russ

T = int(input())
for i in range(T):
    n,x,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    count = 0
    for i in range(n):
        if abs(a[i]-b[i])<=k:
            count+=1
    if count<x:
        print("NO")
    else:
        print("YES")

# Input : 
# 3
# 4 2 2
# 1 7 7 5
# 1 8 1 2
# 5 1 3
# 9 8 7 2 5
# 5 4 1 8 9
# 3 3 0
# 2 3 4
# 2 3 4

# Output:
# YES
# NO
# YES