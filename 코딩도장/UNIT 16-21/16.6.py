# 표준 입력으로 정수가 입력됩니다. 
# 입력된 정수의 구구단을 출력하는 프로그램을 만드세요
# (input에서 안내 문자열은 출력하지 않아야 합니다). 
# 출력 형식은 숫자 * 숫자 = 숫자처럼 만들고 숫자와 *, = 사이는 공백을 한 칸 띄웁니다.

DAN = int(input())

for i in range(1, 10):
    print(DAN, '*', i, '=', end = ' ')
    print(DAN * i)

