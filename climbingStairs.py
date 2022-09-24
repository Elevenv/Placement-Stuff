# https://leetcode.com/problems/climbing-stairs/
# 70.Climbing stairs


n = 5
one,two = 1,1
for i in range(n-1):
    temp = one
    one = one + two
    two = temp
print(one)