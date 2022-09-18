string = "tomsjkafjsgdtomsdfhsftomsdfs"
searchEle = 'tom'
count = 0
for i in range(int(len(string)/3)):
    if searchEle in string:
        count+=1
        string = string.replace(searchEle,'',1)
print(count)