a = [[10, 20],
     [30, 40],
     [50, 60]]

print(a[0][0])
print(a[1][1])
print(a[2][1])

b = [[10, 20], [30, 40], [50, 60]]

from pprint import pprint
pprint(b, indent=4, width=25)

for x, y in b:
    print(x, y)