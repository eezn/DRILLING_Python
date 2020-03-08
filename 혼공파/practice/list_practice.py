list_a = [1,2,3]
list_b = [4,5,6]
list_c = []
list_d = []

print()
print("# 리스트에 요소 추가하기")
print()

print("list_a = ", list_a)
print("list_b = ", list_b)
print()

print("list_a + list_b = ", list_a + list_b)
print("list_a * 3", list_a * 3)
print()

print("len(list_a) = ", len(list_a))
print()

for i in range(4,10):
    list_a.append(i)
print("list_a =", list_a)
print()

# [8], [7], [6], [5], [4], [3], [2], [1], [0] / len(list_a) = 9
for i in range(len(list_a)-1, 0-1,-1):
    list_c.append(list_a[i])
print("list_c =", list_c)
print()

# 파괴적 처리 / .extend()
list_a.extend(list_c) 
print("list_a.extend(list_c) =", list_a)
print()

print("list_a = ", list_a)
print("list_b = ", list_b)
print("list_c = ", list_c)
print()

print("# 리스트에 요소 제거하기")
print()

print("- 인덱스로 제거 : del 리스트명[인덱스]")
del list_a[len(list_a)-1]
print("del_list_a[len(list_a)-1]: ", list_a)
print()

print("- 인덱스로 제거 : 리스트명.pop(인덱스)")
list_a.pop(len(list_a)-1)
print("list_a.pop(len(list_a)-1): ", list_a)
list_a.pop()
print("list_a.pop(len(): ", list_a)
print()

print("- 값으로 제거 : 리스트.remove(값)")
list_a.remove(9)
print("list_a.remove(9): ", list_a)
print()

print("- 모두 제거 : 리스트.clear()")
list_a.clear()
print("list_a.clear(): ", list_a)
print()
print()