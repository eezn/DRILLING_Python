i = 0
while True:
    print(i)
    i += 1
    if i == 100:
        break
    

for i in range(10000):
    print(i)
    if i == 100:
        break


for i in range(100):
    if i % 2 == 0:
        continue
    print(i)


i = 0
while i < 100:
    i += 1
    if i % 2 == 0:
        continue
    print(i)