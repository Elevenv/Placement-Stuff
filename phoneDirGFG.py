# https://practice.geeksforgeeks.org/problems/phone-directory4628/1
#Phone Directory

def DisplayContacts(n,contact,s):
    ans = []
    for i in range(1,len(s)+1):
        sub = s[:i]
        # print(sub)
        flag = False
        for j in contact:
            if j[:i] == sub:
                ans.append(j)
                flag = True
        if not flag:
            ans.append(0)
    return ans

n = 3
contact = ["geeikistest", "geeksforgeeks", "geeksfortest"]
s = "geeips"

print(DisplayContacts(n, contact, s))

