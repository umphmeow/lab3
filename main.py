import random
def print_matrix(mat):
    for row in mat:
        print(' '.join(str(elem) for elem in row))

def paste(matF, matrix, col_in, row_in):
    for row, i in zip(matrix, range(row_in, row_in + len(matrix))):
        for elem, j in zip(row, range(col_in, col_in + len(row))):
            matF[i][j] = elem

K = int(input('Введите число K: '))

n = int(input('Введите число N, (N > 3): '))

if n < 4:
    print('Введено неправильное N')
    exit()

type = input('Использовать случайно сгенерированную матрицу? (y/n): ').lower().strip()

if type == 'y':
    A = [[random.randint(-10, 10) for j in range(n)] for i in range(n)]
else:
    A = [[1 if i==j else 0 for j in range(n)] for i in range(n)]

print('Матрица А:')
print_matrix(A)
print()

n2 = n_hl = n // 2
E = [row[n2:n] for row in A[0:n_hl+1]]
B = [row[n2:n] for row in A[n2:n]]
C = [row[0:n_hl+1] for row in A[n2:]]
D = [row[0:n_hl+1] for row in A[0:n_hl+1]]
if n % 2 == 1:
    n2 = n_hl = n // 2 + 1

print('--------------------------------------------------------------------------------------------------------------------------------------------------------')
print('Подматрицы матрицы A:')
print('Подматрица D')
print_matrix(D)
print()
print('Подматрица E')
print_matrix(E)
print()
print('Подматрица C')
print_matrix(C)
print()
print('Подматрица B')
print_matrix(B)
print()


print('--------------------------------------------------------------------------------------------------------------------------------------------------------')
sym=True
for i in range(n):
    for j in range(n):
        if i != j:
            if A[i][j] == A[j][i]:
                continue
            else:
                sym = False

if sym:
    print('Матрица А симметрична относительно главной диагонали.')
    print('Начальная подматрциа B:')
    print_matrix(B)
    right_matrix = [[0] * (n2+1) for i in range(n2 + 1)]
    for i in range(n2 + 1):
        for j in range(i, n2 - i):
            right_matrix[j][n2 - i - 1] = B[j][n2 - i - 1]

    # Извлекаем матрицу слева
    left_matrix = [[0] * (n2+1) for i in range(n2+1)]
    for i in range(n2 + 1):
        for j in range(i, n2 - i):
            left_matrix[j][i] = B[j][i]
    for i in range(n2):
        for j in range(i, n2 - i):
            B[j][n2 - i - 1] = left_matrix[j][i]
            B[j][i] = right_matrix[j][n2 - i - 1]

    print('Получившаяся подматрица B:')
    print_matrix(B)
else:
    print('Матрица А не симметрична относительно главной диагонали')
    C, E = E, C
if n % 2 == 1:
    n2 = n_hl = n_hl-1
F = [[0 for j in range(n)] for i in range(n)]
for i in range(n_hl):
    for j in range(n_hl):
        F[i][j] = D[i][j]
for i in range(n_hl):
    for j in range(n2, n):
        F[i][j] = E[i][j-n2]
for i in range(n2, n):
    for j in range(n2, n):
        F[i][j] = B[i-n2][j-n2]
for i in range(n2, n):
    for j in range(n_hl):
        F[i][j] = C[i-n2][j]

print('Матрица F:')
print_matrix(F)
print()

print('--------------------------------------------------------------------------------------------------------------------------------------------------------')
print('Вычисляем К * (F+A) * AT – AT + F:')

FA = [[A[i][j] + F[i][j] for j in range(n)] for i in range(n)]
print('Результат (F+A):')
print_matrix(FA)
print()

KFA = [[K * FA[i][j] for j in range(n)] for i in range(n)]
print('Результат К * (F+A):')
print_matrix(KFA)
print()

At = [[A[j][i] for j in range(n)] for i in range(n)]
print("Матрица А транспонированая:")
print_matrix(At)
print()

KFAT = [[sum([KFA[i][k] * At[k][j] for k in range(n)]) for j in range(n)] for i in range(n)]
print('Результат К * (F+A) * AT:')
print_matrix(KFAT)
print()

ATF = [[At[i][j] + F[i][j] for j in range(n)] for i in range(n)]
print('Результат AT + F:')
print_matrix(ATF)
print()

result = [[KFAT[i][j] - ATF[i][j] for j in range(n)] for i in range(n)]
print('Результат:')
print_matrix(result)
