import random
lotto_num = [[], [], [], [], []]
lotto = [[], [], [], [], []]

for i in range(0, 5):
        for j in range(0, 6):
            lotto_num[i].append(random.randrange(1, 45+1))

for i in range(0, len(lotto_num)):  
    print(lotto_num[i])