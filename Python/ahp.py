import numpy as np

# Định nghĩa ma trận đánh giá

matrix = np.array([

    [1, 1/2, 4],

    [2, 1, 9],

    [1/4, 1/9, 1],

])

# Tính toán các giá trị riêng và vector riêng của ma trận

eigenvalues, eigenvectors = np.linalg.eig(matrix)

# Chọn vector riêng tương ứng với giá trị riêng lớn nhất

eigenvector = eigenvectors[:, np.argmax(eigenvalues)]

# Tính toán trọng số bằng cách chuẩn hóa vector riêng

weights = eigenvector / eigenvector.sum()

print("Trọng số: ", weights)