character = {
    "name" : "기사",
    "level" : 12,
    "items" : {
        "sword" : "불꽃의 검",
        "armor" : "풀플레이트"
    },
    "skill" : ["베기", "세게 베기", "아주 세게 베기"]
}


for key in character:
    if type(character[key]) is list:
        for s_key in character[key]:
            print(key, ":", s_key)
    elif type(character[key]) is dict:
        for s_key in character[key]:
            print(s_key, ":", character[key][s_key])
    else:
        print(key, ":", character[key])