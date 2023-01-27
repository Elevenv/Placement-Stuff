class Solution:
    def reverse(self, x: int) -> int:
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
