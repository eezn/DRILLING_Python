x = input().split()

del x[-5:]
# x[len(x)-5:]
# x[-5:len(x)]

y = tuple(x)
print(y)