# https://leetcode.com/problems/power-of-three/

def isPowerOfThree(n):
    # for i in range(20):
    #     if 3**i == n:
    #         return True
    # return False
        
    x = 1
    while x<=n:
        if x != n:
            x = x*3
        else:
            return True
    return False

n = 27
print(isPowerOfThree(n))