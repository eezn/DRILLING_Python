for i in range(5):
    for j in range(5):
        print('j:', j, sep=' ', end=' ')
    
    print('i:', i, '\\n', sep=' ')

print()


for i in range(5):
    for j in range(5):
        print('*', end='')
    print()

print()


# 계단식
for i in range(5):
    for j in range(5):
        if j <= i:
            print('*', end='')
    print()

print()

# 대각선
for i in range(5):
    for j in range(5):
        if i == j:
            print('*', end='')
        elif j <= i:
            print(' ', end='')
    print()

print()