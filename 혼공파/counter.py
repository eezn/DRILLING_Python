list = []
count_A = 0
count_B = 0
count_C = 0
count_T = 0

number = int(input("문항수는: "))
print()
print("\n".join([
    "1. A",
    "2. B",
    "3. C",
    "0. 해당없음"
]))
print()

for i in range(0, number):
    input_a = input("1, 2, 3, 0 >")
    list.append(input_a)
    if input_a == "1":
        count_A += 1
    elif input_a == "2":
        count_B += 1
    elif input_a == "3":
        count_C += 1
count_T = count_A + count_B + count_C

print()
print(list)
print()
print("A는 {}개, B는 {}개, C는 {}개, 총 {}개의 질문에 응답하였습니다.".format(count_A, count_B, count_C, count_T))
print()