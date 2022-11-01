# https://leetcode.com/problems/divide-two-integers/
# 29. Divide Two Integers

def divide(dividend, divisor):
    positive = False
    if (dividend>=0 and divisor>0) or (dividend<0 and divisor<0):
        positive = True
    dividend, divisor = abs(dividend), abs(divisor)
    res = 0
    while dividend >= divisor:
        temp, i = divisor, 1
        while dividend >= temp:
            dividend -= temp
            res += i
            i +=1
            temp +=divisor
    if not positive:
        res = -res
    return min(max(-2147483648, res), 2147483647)

print(divide(-1,-1))