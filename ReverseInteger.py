# https://leetcode.com/problems/reverse-integer/
#Reverse Integer

def reverse(x):
    if x==0:
        return 0
    neg = 1
    if x<0:
        neg=-1
    x = str(abs(x))
    intReverse = x[::-1]
    if abs(int(intReverse))>2**31:
        return 0
    else:
        return int(intReverse)*neg
# OR

# def reverse(x):
#         symbol = -1 if x < 0 else 1
#         res = int(str(abs(x))[::-1])*symbol
#         if res<-2**31  or 2**31 + 1 < res:
#             return 0
#         return res

x = -123
print(reverse(x))