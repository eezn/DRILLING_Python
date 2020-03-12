# 10자 이하인 단어 개수 세기

with open('words.txt', 'r') as file:
    count = 0
    lines = file.readline()
    for line in lines:
        if len(line.strip('\n')) <= 10:
            count += 1