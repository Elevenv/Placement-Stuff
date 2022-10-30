# https://leetcode.com/problems/valid-palindrome/submissions/
#Valid Palindrome

s = "A man, a plan, a canal: Panama"
# s = " "
s = s.lower()
s1 = ''
for i in s:
    if i.isalnum():
        s1+=i
revese = s1[::-1]
print(s1)
print(revese)
print(s1==revese)