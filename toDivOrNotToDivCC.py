# https://www.codechef.com/problems/DIVAB?tab=statement

def solve(a,b,n):
    if a%b==0:
        return -1
    res = n-n%a
    if n%a != 0:
        res+=a
    if res%b == 0:
        res+=a
    return res
    
for _ in range(int(input())):
    a,b,n = map(int,input().split())
    
    print(solve(a,b,n))