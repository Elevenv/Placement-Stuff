# https://www.codechef.com/submit/AVG
#Average Number 

for _ in range(int(input())):
    n,k,v = map(int,input().split())
    
    nArr = list(map(int,input().split()))
    nArrSum = sum(nArr)
    v = v*(n+k)
    x = v-nArrSum
    print(int(x/k)) if x>0 and x%k==0 else print(-1)
