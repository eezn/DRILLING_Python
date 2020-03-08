# 역삼각형
for i in range(5):
    for j in range(5):
        if j >= i:
            print('*', end='')
        else:
            print(' ', end='')
    print()

print()

for i in range(5):
    for j in range(5):
        if j < i:
            print(' ', end='')
        else:
            print('*', end='')
    print()