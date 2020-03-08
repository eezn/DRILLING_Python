# 표준 입력으로 삼각형의 높이가 입력됩니다.
# 입력된 높이만큼 산 모양으로 별을 출력하는 프로그램을 만드세요
# (input에서 안내 문자열은 출력하지 않아야 합니다.)
# 이때 출력 결과는 예제와 정확히 일치해야 합니다.
# 모양이 같더라도 공백이나 빈 줄이 더 들어가면 틀린 것으로 처리됩니다.

height = int(input())
#length = 2*height - 1

#for i in range(height-1, -1, -1): # 4 3 2 1 0
#    print(i, end='')
#    print(' ' * i, end='')
#    for j in range(1, length+1, 2): # 1 3 5 7 9
#        print(j, end='')
#        print('*', end='')
#    print()

for i in range(height): # 0 1 2 3 4
    for j in reversed(range(height)): # 4 3 2 1 0
        if i < j:
            print(' ', end='')
        else:
            print('*', end='')
    for j in range(height-1): # 3 2 1 0
        if i > j:
            print('*', end='')
    print()