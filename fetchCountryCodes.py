#Dunzo internship Test (API Program)

import requests
import json

con = input()
mob = input()

URL = "https://jsonmock.hackerrank.com/api/countries?name="

URL+=con

r = requests.get(URL)

res = r.json()

d = res['data']
print(d)

if d:
    a = d[0]['callingCodes']
    ans = "+" +  a[-1] + " "  + mob
    print(ans)
else:
    print(-1)