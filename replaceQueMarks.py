#Replace question marks in string such that no letters appear next to another letter of same kind.


s = 'ab?ac?'
# s = '???'
s1 = ''

chars = 'abc'
print(s)

for i in range(len(s)):
    if s[i] == '?':

        if i==0:
            for j in chars:
                if s[1]!=j:
                    # s1[0] = j
                    s1+=j
                    break
        elif i==len(s)-1:
            for j in chars:
                if s[len(s)-2] != j:
                    # s1[len(s)-1] = j
                    s1+=j
                    break
        else:
            prev = s[i-1]
            next = s[i+1]
            for j in chars:
                if j!=prev and j!=next:
                    s1+=j
                    break
    else:
        s1+=s[i]

print(s1)
        # if i != 0 and i!=len(s)-1:
        #     sub = s[i-1:i+2]
        #     for j in chars:
        #         if j not in sub:
        #             s = s.replace('?', j,1)
        #             break
        # else:
        #     if i==0:
        #         sub = s[:2]
        #         for j in chars:
        #             if j not in sub:
        #                 s = s.replace('?', j,1)
        #                 break
        #     else:
        #         sub = s[len(s)-2:]
        #         for j in chars:
        #             if j not in sub:
        #                 s = s.replace('?',j,1)

# print(s)