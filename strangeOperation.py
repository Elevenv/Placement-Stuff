# https://www.codechef.com/problems/UTMOPR?tab=statement

for _ in range(int(input())):
    
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))

    # s = sum(arr)
    
    # for i in range(k):
    #     s = sum(arr)
    #     arr.append(s+1)

    
    print('odd') if sum(arr)%2==0 and k==1 else print('even')
    
    # print('even') if arr[-1]%2==0 else print('odd')
