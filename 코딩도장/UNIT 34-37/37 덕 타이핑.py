class Duck:
    def quack(self): print('꽥!')
    def feathers(self): print('오리는 흰색과 회색 털을 가지고 있습니다.')

class Person:
    def quack(self): print('사람은 오리를 흉내냅니다. 꽥!')
    def feathers(self): print('사람은 땅에서 깃털을 주워서 보여줍니다.')

def in_the_forest(duck):
    duck.quack()
    duck.feathers()

donald = Duck()
james = Person()

in_the_forest(donald)
in_the_forest(james)