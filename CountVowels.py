def CountVowels(string):
    string = string.lower()
    strList = []
    strDict = {}
    for i in string:
        if i != ' ' and i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            strList.append(i)
    for i in strList:
        strDict[i] = strList.count(i)
    return strDict

print("Enter String : ")
string = input()
dict1 = CountVowels(string)
if len(dict1)!=0:
    print(dict1)
else:
    print("No vowels Found")
