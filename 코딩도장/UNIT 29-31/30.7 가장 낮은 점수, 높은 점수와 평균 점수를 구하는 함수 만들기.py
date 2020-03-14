# 표준 입력으로 국어, 영어, 수학, 과학 점수가 입력됩니다. 
# 다음 소스 코드를 완성하여 가장 높은 점수, 가장 낮은 점수, 평균 점수가 출력되게 만드세요. 
# 평균 점수는 실수로 출력되어야 합니다.

# 76 82 89 84
# 낮은 점수: 76.00, 높은 점수: 89.00, 평균 점수: 82.75
# 낮은 점수: 82.00, 높은 점수: 84.00, 평균 점수: 83.00

korean, english, mathematics, science = map(int, input().split())

def get_min_max_score(*args):
    min_score = min(args)
    max_score = max(args)
    
    return min_score, max_score

def get_average(**kwargs):
    hap = sum(kwargs.values())

    return hap / len(kwargs)



min_score, max_score = get_min_max_score(korean, english, mathematics, science)
average_score = get_average(korean=korean, english=english, mathematics=mathematics, science=science)

print('낮은 점수: {0:.2f}', '높은 점수: {1:.2f}', '평균 점수: {2:.2f}'.format(min_score, max_score, average_score))

min_score, max_score = get_min_max_score(english, science)
average_score = get_average(english=english, science=science)

print('낮은 점수: {0:.2f}', '높은 점수: {1:.2f}', '평균 점수: {2:.2f}'.format(min_score, max_score, average_score))


