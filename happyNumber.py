# https://leetcode.com/problems/happy-number/submissions/
# 202. Happy Number


def helper(num):
    ans = 0
    while num!=0:
        ans+=(num%10)**2
        num//=10
    return ans

n = 19
l = []
flag = False
while True:
    n = helper(n)
    if n==1:
        flag = True
        break

    if n not in l:
        l.append(n)
    else:
        n = -1
        break
print(flag)
