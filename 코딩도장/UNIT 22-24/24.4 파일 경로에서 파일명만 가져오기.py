# 파일 경로에서 파일명만 출력시키기
# 단, 경로에서 폴더의 깊이가 달라지더라도 파일명만 출력할 수 있어야 합니다.
path = 'C:\\Users\\dojang\\AppData\\Local\\Programs\\Python\\Python36-32\\python.exe'

x = path.split('\\')

filename_1 = x[-1]
x.reverse()
filename_2 = x[0]
filename_3 = path[path.rfind('\\') + 1:]

print(filename_1)
print(filename_2)
print(filename_3)