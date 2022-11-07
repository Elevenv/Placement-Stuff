# https://www.codechef.com/submit/SUSSTR
# Suspense String

for _ in range(int(input())):
    n = int(input())
    s = input()
    turn = 'alice'
    t = ''
    while s:
        if turn == 'alice':
            pickedChar = s[0]               #Pick first character
            s = s[1:]                       #delete picked char
            if pickedChar == '1':
                t+=pickedChar
            else:
                pickedChar+=t
                t = pickedChar
            turn = 'bob'
            print(t,' from alice')
        else:
            pickedChar = s[-1]              #pick last char
            s = s[:-1]                      #Delete picked char
            if pickedChar == '0':
                t+=pickedChar
            else:
                pickedChar+=t               #append at first position
                t = pickedChar
            turn = 'alice'
            print(t,' from bob')
    print(t)