# https://leetcode.com/problems/string-to-integer-atoi/
# 8. String to Integer (atoi)



def strtoInt(s):# sorted(arr2)
    s = s.strip()
    ans = ''
    if s[0] == "+" or s[0] =="-" or s[0] =="." or s[0].isnumeric():
        for i in s:
            if i.isnumeric():
                ans+=i
        ans1 = -int(ans)
        if str(ans1) in s:
            return int(ans1)
        else: 
            return(ans)
    else:
        return 0

# s ="-91283472332"
s = "-4193- with words"
print(strtoInt(s))

# for i in s:
#     if i.isnumeric():
#         ans+=i
# ans1 = -int(ans)
# print(ans1) if str(ans1) in s else print(ans)
