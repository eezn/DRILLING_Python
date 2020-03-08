# 23.7 심사문제: 지뢰찾기

col, row = map(int, input().split())
ex_col, ex_row = col+2, row+2

matrix = []
for i in range(row):
    matrix.append(list(input()))


matrix_02 = [[0]*ex_col for i in range(ex_row)]
for i in range(1, row+1):
    for j in range(1, col+1):
        matrix_02[i][j] = matrix[i-1][j-1]

real_i = 1
while real_i < row+1:
    real_j = 1
    while real_j < col+1:
        if matrix_02[real_i][real_j] != '*':
            count = 0
            for a in range(real_i -1, real_i +2):
                for b in range(real_j -1, real_j +2):
                    if matrix_02[a][b] == '*':
                        count += 1
            matrix_02[real_i][real_j] = count
            

        real_j += 1
    real_i += 1


# print(matrix)
# print(matrix_02)

for i in range(1,row+1):
    for j in range(1, col+1):
        print(matrix_02[i][j], end='')
    print()