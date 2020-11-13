# latitude and longitude
from collections import Counter
s1 = input()
s2 = input()

di = { 'n':'North', 's':'South', 'e':'East', 'w':'West' }
ans = ['0', di[s1[-1]], '0', di[s2[-1]]]

s1, s2 = s1[:-1], s2[:-1]

s1, s2 = dict(Counter(s1)), dict(Counter(s2))
max1, min1 = max(s1.values()), min(s1.values())

ans[0] = max1 - min1
max2, min2 = max(s2.values()), min(s2.values())

ans[2] = max2 - min2

print(ans[0], ans[1], ans[2], ans[3], sep=" ")