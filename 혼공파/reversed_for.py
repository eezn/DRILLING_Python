# range()함수 매개변수 세 개 사용
# 4, 4-1(3), 4-1-1(2), 4-1-1-1(1), 4-1-1-1-1(0)
for i in range(4, 0 - 1, -1):
    print("현재 반복 변수: {}".format(i))
print()

# reversed()함수 사용
for i in reversed(range(5)):
    print("현재 반복 변수: {}".format(i))