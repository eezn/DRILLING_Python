number = int(input("정수를 입력하세요> "))


#1 들여쓰기 발생
if number % 2 == 0:
    print("""\
        입력한 문자열은 {}입니다.
        {}는(은) 짝수 입니다.""".format(number, number))
else:
    print("""\
        입력한 문자열은 {}입니다.
        {}는(은) 홀수 입니다.""".format(number, number))
print()

#2
if number % 2 == 0:
    print("""입력한 문자열은 {}입니다.
{}는(은) 짝수입니다.""".format(number, number))
else:
    print("""입력한 문자열은 {}입니다.
{}는(은) 홀수입니다.""".format(number, number))
print()



output = [i for i in range(1, 100+1) if "{:b}".format(i).count("0") == 1]
for i in output:
    print("{} : {}".format(i, "{:b}".format(i)))
print("합계:", sum(output))
