korean, english, math, science = map(int,input().split())

# 소수점 포함
avg = (korean + english + math + science)/4 
print(int(avg))

# 소수점 버림
avg = (korean + english + math + science)//4 
print(avg)