number = input("int> ")
last_character = number[-1]

if last_character in "02468":
    print("짝수")

if last_character in "13579":
    print("홀수")