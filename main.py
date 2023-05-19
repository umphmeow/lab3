import numpy as np


def print_matrix(mat):
    print(str(mat).replace('[', ' ').replace(']', ' ').replace('\n', '\n '))


def paste(matF, matrix, col_in, row_in):
    for row, i in zip(matrix, range(row_in, row_in + len(matrix))):
        for elem, j in zip(row, range(col_in, col_in + len(row))):
            matF[i][j] = elem


K = int(input('Введите число K: '))

n = int(input('Введите число N, (N >= 5): '))

if n < 5:
    print('Введен неправильное N, попробуйте еще')
    exit()

type = input('Использовать случайно сгенерированную матрицу? (y/n): ').lower().strip()

if type == 'y':
    A = np.random.randint(-10, 10, (n, n))
else:
    A = np.eye(n)

print('Матрица А:\n', print_matrix(A), '\n')

n2 = n_hl = n // 2
if n % 2 != 0:
    n2 += 1

E = A[0:n_hl, n2:n]
B = A[n2:n, n2:n]
C = A[n2:n, 0:n_hl]
D = A[0:n_hl, 0:n_hl]

print('--------------------------------------------------------------------------------------------------------------------------------------------------------')
print('Подматрицы матрицы A:')
print('Подматрица D\n', D, '\n')
print('Подматрица E\n', E, '\n')
print('Подматрица C\n', C, '\n')
print('Подматрица B\n', B, '\n')


print('--------------------------------------------------------------------------------------------------------------------------------------------------------')
for i in range(n):
    for j in range(n):
        if i != j:
            if A[i][j] == A[j][i]:
                sym=True
                continue
            else:
                sym = False

if sym:
    print('Матрица А симметрична относительно главной диагонали.')
    print('Начальная подматрциа B:')
    print_matrix(C)
    for i in range((n // 4) + 1):
        for j in range(i, n_hl - i):
            B[j][i], B[j][((n // 4) + 1) - i] = B[j][((n // 4) + 1) - i], B[j][i]
    print('Получившаяся подматрица B:')
    print_matrix(C)
else:
    print('Матрица А не симметрична относительно главной диагонали')
    C, E = E, C

F = np.zeros((n, n))
F[:n_hl, :n_hl] = D
F[:n_hl, n2:n] = E
F[n2:n, n2:n] = B
F[n2:n, :n_hl] = C

print('Матрица F:')
print_matrix(F)

print('--------------------------------------------------------------------------------------------------------------------------------------------------------')
print('Вычисляем К * (F+A) * AT – AT + F:')

FA = A + F
print('Результат (F+A):')
print_matrix(FA)

KFA = K * FA
print('Результат К * (F+A):')
print_matrix(KFA)

At = A.T
print("Матрица А транспонированая:")
print_matrix(At)

KFAT = np.dot(KFA, At)
print('Результат К * (F+A) * AT:')
print_matrix(KFAT)

ATF = At + F
print('Результат AT + F:')
print_matrix(ATF)

result = KFAT - ATF
print('Результат:')
print_matrix(result)
