def phan_ra_ma_tran(matrix):

    rows, cols = len(matrix), len(matrix[0])

    if rows % 2 != 0 or cols % 2 != 0:

        print("Ma trận không thể phân rã thành các ma trận con.")

        return

    a = [[0] * (cols // 2) for _ in range(rows // 2)]

    b = [[0] * (cols // 2) for _ in range(rows // 2)]

    c = [[0] * (cols // 2) for _ in range(rows // 2)]

    d = [[0] * (cols // 2) for _ in range(rows // 2)]

    for i in range(rows // 2):

        for j in range(cols // 2):

            # Phân rã ma trận

            a[i][j] = matrix[i][j]

            b[i][j] = matrix[i][j + cols // 2]

            c[i][j] = matrix[i + rows // 2][j]

            d[i][j] = matrix[i + rows // 2][j + cols // 2]

    return a, b, c, d

# Ma trận đầu vào

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

# Phân rã ma trận

submatrices = phan_ra_ma_tran(matrix)

# In các ma trận con

print("Ma trận a:")

for row in submatrices[0]:

    print(row)

print("Ma trận b:")

for row in submatrices[1]:

    print(row)

print("Ma trận c:")

for row in submatrices[2]:

    print(row)

print("Ma trận d:")

for row in submatrices[3]:

    print(row)