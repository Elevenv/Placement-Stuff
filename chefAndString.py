# https://www.codechef.com/problems/RECNDSTR

s = "abcd"

ls = [i for i in s]
print(ls)

# bcda
ls0 = ls[0]
ls.remove(ls0)
ls.append(ls0)
print(ls)

rs = [j for j in s]
print(rs)

rs_1 = rs[-1]
rs.remove(rs_1)
rs.insert(0, rs_1)

print(rs)

print("YES") if ls == rs else print("NO")

#  if ( s[i] != s[(i+2)%s.size()] )