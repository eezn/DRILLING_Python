# 3의 배수, 5의 배수 처리
# 3, 6, 9, 12, (15), 18, 21, 24, 27, (30)
# 5, 10, (15), 20, 25, (30)

for i in range(1, 100+1): 
    if i % 3 == 0 and i % 5 == 0:
    # if i % 15 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)