# 10 20
# 덧셈: 30, 뺄셈: -10, 곱셈: 200, 나눗셈: 0.5

# 40 8
# 덧셈: 48, 뺄셈: 32, 곱셈: 320, 나숫셈: 5.0

x, y = map(int, input().split())

def calc(a, b):
    return a+b, a-b, a*b, a/b


a, s, m, d = calc(x, y)
print('덧셈: {0}, 뺄셈: {1}, 곱셈: {2}, 나눗셈: {3}'.format(a, s, m, d))