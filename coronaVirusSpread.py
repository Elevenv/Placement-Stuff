# https://www.codechef.com/problems/COVID19?tab=statement

def InfectedPeoples(n,l):
    ans = []
    temp = 1
    for i in range(n-1):
        if abs(l[i+1]-l[i])<=2:
            temp+=1
        else:
            ans.append(temp)
            temp = 1
    ans.append(temp)
    return min(ans),max(ans)

for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    ans = InfectedPeoples(n,l)
    print(ans[0],ans[1])