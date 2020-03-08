dictionary = {
    "name" : "건조 망고",
    "type" : "당절임",
    "ingredient" : ["맹고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "origin" : "필리핀"
}
dictionary_2 = {}

print("name: ", dictionary["name"])
print("type: ", dictionary["type"])
print("ingredient: ", dictionary["ingredient"])
print("ingredient[0]: ", dictionary["ingredient"][0])
print("ingredient[1]: ", dictionary["ingredient"][1])
print("ingredient[2]: ", dictionary["ingredient"][2])
print("ingredient[3]: ", dictionary["ingredient"][3])
print("origin: ", dictionary["origin"])
print()

dictionary["name"] = "8D 건조 망고"
print("name: ", dictionary["name"])
dictionary["ingredient"][0] = "망고"
print("ingredient[0]: ", dictionary["ingredient"][0])
print()

print("# 딕셔너리에 값 추가하기/제거하기")

dictionary["price"] = 5000
print("price: ", dictionary["price"])
print(dictionary)

del dictionary["ingredient"]
print("del dictionary[\"ingredient\"]: ", dictionary)
print()

print("요소 추가 이전: ", dictionary_2)
dictionary_2["name"] = "새로운 이름"
dictionary_2["head"] = "새로운 정신"
dictionary_2["body"] = "새로운 몸"
print("요소 추가 이후: ", dictionary_2)
print()
del dictionary_2["name"]
del dictionary_2["head"]
del dictionary_2["body"]
print("요소 제거 이후: ", dictionary_2)
print()

print("# 딕셔너리 내부에 키가 있는지 확인하기")
key = input(">접근하고자 하는 키: ")
if key in dictionary:
    print(dictionary[key])
else:
    print("존재하지 않는 키에 접근하고 있습니다.")
print()