class Solution:
    def value(self,r):
        if (r == 'I'):
            return 1
        if (r == 'V'):
            return 5
        if (r == 'X'):
            return 10
        if (r == 'L'):
            return 50
        if (r == 'C'):
            return 100
        if (r == 'D'):
            return 500
        if (r == 'M'):
            return 1000
        return -1

    def romanToInt(self,s):
            result = 0
            i = 0
            while i<len(s):
                temp1 = self.value(s[i])
            #     i+=1
            # print(result)
                if i+1<len(s):
                    temp2 = self.value(s[i+1])
                    if temp1 >= temp2:
                        result = result + temp1
                        i+=1
                    else:
                        result = result + temp2 - temp1
                        i+=2
                else:
                    result+=temp1
                    i+=1
            print(result)

if __name__=='__main__':
    obj = Solution()
    obj.romanToInt("III")