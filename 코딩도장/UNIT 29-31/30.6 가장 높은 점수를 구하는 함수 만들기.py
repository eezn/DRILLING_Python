korean, english, mathematics, science = 100, 86, 81, 91

def get_max_score(korean=0, english=0, mathematics=0, science=0):
    max_score = korean
    if max_score < english:
        max_score = english
    if max_score < mathematics:
        max_score = mathematics
    if max_score < science:
        max_scroe = science
    return max_score

# def get_max_score(*args):
#     return max(args)
    



max_score = get_max_score(korean, english, mathematics, science)
print('높은 점수:', max_score)

max_score = get_max_score(english, science)
print('높은 점수:', max_score)