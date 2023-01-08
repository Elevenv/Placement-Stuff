
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle)>len(haystack):
            return -1
        char = needle[0]

        for i in range(len(haystack)):
            ans = ''
            if haystack[i] == char:
                idx = 0
                # for j in range(i,i+len(needle)):
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
                return i
        return -1
