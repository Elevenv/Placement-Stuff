# https://www.codechef.com/ZCOPRAC/problems/ZCO14003

l = []
ans = []
for _ in range(int(input())):
    l.append(int(input()))

for i in range(max(l)):
    profit = 0
    for j in l:
        if i<=j:
            profit+=i
    ans.append(profit)

print(max(ans)) if ans else print(-1)