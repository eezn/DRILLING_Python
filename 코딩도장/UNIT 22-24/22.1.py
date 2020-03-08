# 리스트와 튜플 응용하기
# append : 요소 하나를 추가 
# extend : 리스트를 연결하여 확장
# insert : 특정 인덱스에 요소 추가

a = [10, 20, 30]
a.append(500)
print(a)
print(len(a))

# 빈 리스트에 값 추가
a = []
a.append(10)
print(a)

# 리스트에 리스트 추가
a = [10, 20 ,30]
a.append([500, 600])
print(a)
print(len(a))

# 리스트 확장하기
a = [10, 20, 30]
a.extend([500, 600])
print(a)
print(len(a))

a = [10, 20, 30]
a.append([500, 600])
b = [1, 2, 3, 4, 5]
b.extend(a)
print(b)
print(len(b))

# 리스트의 특정 인덱스에 요소 추가하기 : insert(인덱스, 요소)
a = [10, 20, 30]
a.insert(2, 500)
print(a)
print(len(a))

a.insert(0, 'first')
a.insert(len(a), 'end')
print(a)

a = [10, 20, 30]
print(a)
print(a.pop())
print(a)