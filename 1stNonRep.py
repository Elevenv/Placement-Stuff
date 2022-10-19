# First Non repeating Character from string

# s = "characterhr"
s = 'geeksforgeeks'

for i in range(len(s)):
    ct = 1
    for j in range(len(s)):
        if i!=j:
            if s[i] == s[j]:
                ct+=1
    if ct<2:
        print(ct)
        print(s[i])
        break

# OR

    # if s.count(i)<2:
    #     print(i)
    #     break
