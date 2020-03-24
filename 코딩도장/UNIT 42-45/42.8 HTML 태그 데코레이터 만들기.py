# 표준 입력으로 HTML 태그 이름 두 개가 입력됩니다.
# 다음 소스 코드에서 함수의 반환값을 HTML 태그로 감싸는 데코레이터를 만드세요.
# HTML 태그는 웹 페이지에서 사용하는 문법이며 <span>문자열</span>, <p>문자열</p>처럼
# <태그이름>으로 시작하며 </태그이름>으로 끝납니다.

# p span
# <p><span>Hello, world!</span></p>

# b i
# <b><i>Hello, world!</i></b>


# -----

import functools

def html_tag(x):
    def real_decorator(func):
        def wrapper():
            return '<{0}>{1}</{0}>'.format(x, func())
        return wrapper
    return real_decorator
        


# -----

a, b = input().split()

@html_tag(a)
@html_tag(b)
def hello():
    return 'Hello, world!'

print(hello())