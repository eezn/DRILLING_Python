character = { 
    "name" : "기사", # 딕셔너리
    "level" : 12,
    "items" : {
        "sword" : "불꽃의 검",
        "armor" : "풀플레이트"
    }, 
    "skill" : ["베기", "세게 베기", "아주 세게 베기"] # 리스트
}

for key in character:
    if type(character[key]) is dict:
        for element in character[key]:
            print(element, ":", character[key][element])
    elif type(character[key]) is list:
        for element in character[key]:
            print(key, ":", element)
    else:
        print(key, ":", character[key])