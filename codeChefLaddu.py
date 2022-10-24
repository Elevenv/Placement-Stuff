# https://www.codechef.com/submit/LADDU

for i in range(int(input())):
    a,o=map(str,input().split())
    c=0
    for i in range(int(a)):
        s=list(map(str,input().split()))
        if(s[0]=='CONTEST_WON'):
           c=c+300+max(0,20-int(s[1]))
        elif(s[0]=='TOP_CONTRIBUTOR'):
            c+=300
        elif(s[0]=='BUG_FOUND'):
            c=c+int(s[1])
        else:
            c+=50
    if(o=='INDIAN'):
        print(c//200)
    else:
        print(c//400)