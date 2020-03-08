print('3진수를 입력하면 10진수로 바꾸는 프로그램입니다.')

Number = list(map(int, input('3진수 입력: ').split()))
# print(len(Number))
Number = Number[::-1]

# print(Number)
sum = 0

for i in range(0, len(Number)):
    if Number[i] <= 2:
        Number[i] = Number[i] * (3**i)
        sum += Number[i]
    else:
        print('3진수가 아닙니다.')
        break

print(sum)

