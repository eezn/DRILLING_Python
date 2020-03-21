# 표준 입력으로 정수 두 개가 입력됩니다
# (첫 번째 입력 값의 범위는 10~1000, 두 번째 입력 값의 범위는 100~1000이며 
# 첫 번째 입력 값은 두 번째 입력 값보다 항상 작습니다). 
# 다음 소스 코드에서 첫 번째 정수부터 두 번째 정수 사이의 소수(prime number)를 생성하는 제너레이터를 만드세요. 
# 소수는 1과 자기자신만으로 나누어 떨어지는 1보다 큰 양의 정수입니다.

# 50 100

# <class 'generator'>
# 53 59 61 67 71 73 79 83 89 97

# 950 1000

# <class 'generator'>
# 953 967 971 977 983 991 997


def prime_number_generator(start, stop):
    for i in range(start, stop):
        for j in range(2, i + 1):
            if i == j:
                yield i
            if i % j == 0:
                break
    



start, stop = map(int, input().split())

g = prime_number_generator(start, stop)
print(type(g))
for i in g:
    print(i, end=' ')