# 모듈을 읽어 들입니다.
import os

# 현재 폴더의 파일/폴더를 출력합니다.
output = os.listdir(".")
print("os.listdir():", output)
print()

# 현재 폴더의 파일/폴더를 구분합니다.
print("# 폴더와 파일 구분하기")
for path in output:
    if os.path.isdir(path):
        print("폴더:", path)
    else:
        print("파일:", path)