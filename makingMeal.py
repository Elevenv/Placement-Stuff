# https://www.codechef.com/problems/CFMM

# l = ["cplusplus","oscar",'deck','fee','hat','near']

for _ in range(int(input())):
    n = int(input())
    l = []
    for j in range(n):
        l=l+list(input())
        
    ans=[l.count('c')//2,l.count('o'),l.count('d'),l.count('e')//2,l.count('h'),l.count('f')]
    print(min(ans))

# s = ''
# for i in l:
#     s+=i

# d = {}

# for i in s:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i] = 1

# ans = 0
# for i in range(len(l)):
#     if d['c']>=2 and d['o']>=1 and d['d']>=1 and d['e']>=2 and d['h']>=1 and d['f']>=1:
#         ans+=1
#         d['c']-=2
#         d['o']-=1
#         d['d']-=1
#         d['e']-=2
#         d['h']-=1
#         d['f']-=1

# print(ans)
