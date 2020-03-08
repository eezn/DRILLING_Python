MIN = 2
MAX = 4
ALL = 8
memo = {}

def FUNCTION(남은사람수, 앉힌사람수):
    key = str([남은사람수, 앉힌사람수])
    # 종료조건
    if key in memo:
        return memo[key]
    if 남은사람수 < 0:
        return 0
    if 남은사람수 == 0:
        return 1

    # 재귀 처리
    count = 0
    for i in range(앉힌사람수, MAX + 1):
        count += FUNCTION(남은사람수 - i, i)
    # 메모화 처리
    memo[key] = count
    # 종료
    return count


print(FUNCTION(ALL, MIN))
