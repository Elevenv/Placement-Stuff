string = 'cat batman latt matter cat matter cat'
wordDict = {}

stringSplit = string.split(' ')
for word in stringSplit:
    if stringSplit.count(word)>1:
        wordDict[stringSplit.count(word)] = word
l = []
for i in wordDict:
    l.append(i)
l.sort()
l = l[::-1]
for j in l:
    print(wordDict[j],end=' ')