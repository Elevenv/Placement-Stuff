# https://leetcode.com/problems/valid-parentheses
# 20.Valid Paranthesis

def paraCheck(s):  
   while True:  
       if '()' in s :  
           s = s.replace ( '()' , '' )  
       elif '{}' in s :  
           s = s.replace ( '{}' , '' )  
       elif '[]' in s :  
           s = s.replace ( '[]' , '' )  
       else :  
           return not s
        #    return False

s = "(){}[]"
print(paraCheck(s))
