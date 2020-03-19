# 표준 입력으로 문자열이 입력됩니다. 
# 다음 소스 코드를 완성하여 입력된 문자열이 회문이면 문자열을 그대로 출력하고, 
# 회문이 아니면 '회문이 아닙니다.'를 출력하도록 만드세요. 
# palindrome 함수와 NotPalindromeError 예외를 작성해야 합니다.

# level
# level

# hello
# 회문이 아닙니다.

class NotPalindromeError(Exception):
    def __init__(self):
        super().__init__('회문이 아닙니다.')

def palindrome(word):
    if word == word[::-1]:
        print(word)
    else:
        raise NotPalindromeError

try:
    word = input()
    palindrome(word)
except NotPalindromeError as e:
    print(e)