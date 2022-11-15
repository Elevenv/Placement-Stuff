# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

# haystack = "sadbutsad"
# needle = "sad"

haystack = "mississippi"
needle = "issipi"

# haystack = "hello"
# needle = "helloo"

if len(needle)>len(haystack):
    print(-1)

else:
    char = needle[0]

    for i in range(len(haystack)):
        ans = ''
        if haystack[i] == char:
            idx = 0
            j =i
            while j<i+len(needle) and j<len(haystack):
                if haystack[j]==needle[idx]:
                    ans+=haystack[j]
                else:
                    break
                idx+=1
                j+=1
            # print(ans)
        if ans == needle:
            # print(i)
            break
    else:
        print(-1)        