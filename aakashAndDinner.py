# https://www.codechef.com/problems/CHEFDINE

def dinner(n,k,l,l1):
    
    lct = len(set(l))
    if lct<k:
        return -1
        
    d = {}

    for j in range(n):
        if l[j] not in d:
            d[l[j]] = l1[j]
        elif d[l[j]]>l1[j]:
            d[l[j]] = l1[j]
    
    ans = list(d.values())
    ans.sort()

    return sum(ans[:k])
        
    
for _ in range(int(input())):
    n,k = map(int,input().split())
    l = list(map(int,input().split()))
    l1 = list(map(int,input().split()))
    
    print(dinner(n,k,l,l1))