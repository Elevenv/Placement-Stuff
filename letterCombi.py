# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
#  Letter Combinations of a Phone Number

digits = input()
d = {2:'abc',3:'def',4:'ghi',5:'jkl',6:'mno',7:'pqrs',8:'tuv',9:'wxyz'}
dStr = []
for digit in digits:
    dStr.append(d[int(digit)])

print(dStr)
ans = []
if dStr:
    # for i in range(stop)
    pass
print(ans)