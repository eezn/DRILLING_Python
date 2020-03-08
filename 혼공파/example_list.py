example_list = ["요소A", "요소B", "요소C"]
i = 0
for item in example_list:
    print("{}번째 요소는 {}입니다.".format(i, item))
    i += 1

print()
for i in range(len(example_list)):
    print("{}번째 요소는 {}입니다.".format(i, example_list[i]))