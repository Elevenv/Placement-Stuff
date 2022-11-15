# https://www.codechef.com/problems/CHEALG

# s = "bbbbbbbbbbaa"
# s = "c"
s = "aaaaaaaaaabcdefgh"
newS = ''
VisitedChar = []

for i in range(len(s)):
    ct = 0
    char = s[i]
    for j in range(i,len(s)):
        if s[j] == char:
            ct+=1
        else:
            break

    if char not in VisitedChar:
        VisitedChar = []
        newS = newS + (char+str(ct))
        VisitedChar.append(char)

print("YES") if len(newS)<len(s) else print("NO")

