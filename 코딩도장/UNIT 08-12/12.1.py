lux = [490, 334, 550, 18.72]
lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}

print(lux)

lux1 = dict(health=490, mana=334, melee=550, armor=18.72)
lux2 = dict(zip(['health', 'mana', 'melee', 'armor'], [490, 334, 550, 18.72]))
lux3 = dict([('health', 490), ('mana', 334), ('melee', 550), ('armor', 18.72)])
lux4 = dict({'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72})

print(lux1)
print(lux2)
print(lux3)
print(lux4)

