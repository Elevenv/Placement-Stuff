# https://leetcode.com/problems/excel-sheet-column-number/
# 171. Excel sheet column number

s = 'AA'
ans,pos = 0,0
for i in reversed(s):
    digit = ord(i)-64
    ans += digit*26**pos
    pos+=1
print(ans)