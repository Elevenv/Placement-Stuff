# Find characters that missed while transfromation of data from server to client


# s1 = 'abcdsdf'
# s2 = 'ads'
s1 = input()
s2 = input()

for i in s2:
    if i in s1:
        s1 = s1.replace(i,'',1)
print(s1)