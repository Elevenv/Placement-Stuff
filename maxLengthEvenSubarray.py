# https://www.codechef.com/problems/MXEVNSUB?tab=statement

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    s = n*(n+1)/2
    
    print(n) if s%2==0 else print(n-1)
    