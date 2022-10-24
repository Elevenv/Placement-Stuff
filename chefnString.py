# https://www.codechef.com/submit/XYSTR
# Chef and String 

for _ in range(int(input())):
    s = input()
    yxStr = s.replace('xy','')
    print('yxstr',yxStr)
    print(s.count('xy')+yxStr.count('yx'))