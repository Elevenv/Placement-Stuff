#Second Maximum difference

arr = [14,12,70,15,95,65,22,30]
n = len(arr)

diff = []

for i in range(n):
    for j in range(n):
        diff.append(arr[i]-arr[j])

diff.sort(reverse=True)
print(diff[1])