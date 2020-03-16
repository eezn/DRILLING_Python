# 표준 입력으로 정수가 입력됩니다. 
# 다음 소스 코드를 완성하여 함수 c를 호출할 때마다 숫자가 1씩 줄어들게 만드세요. 
# 여기서는 함수를 클로저로 만들어야 합니다. 
# 정답에 코드를 작성할 때는 def countdown(n):에 맞춰서 들여쓰기를 해주세요.

def countdown(n):
    count = n + 1
    def decrease():
        nonlocal count
        count -= 1
        return count
    return decrease



n = int(input())

c = countdown(n)
for i in range(n):
    print(c(), end=' ')