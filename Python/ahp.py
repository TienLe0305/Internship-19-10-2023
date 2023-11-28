import numpy as np
import pandas as pd

def get_comparison_matrices(num_plans, num_factors):
    matrices = []
    for i in range(num_factors):
        matrix = np.zeros((num_plans, num_plans))
        for j in range(num_plans):
            for k in range(j+1, num_plans):
                value = float(input(f"Nhập giá trị so sánh giữa phương án {j+1} và phương án {k+1} cho yếu tố {i+1}: "))
                matrix[j, k] = value
                matrix[k, j] = 1/value
                matrix[j, j] = 1
                matrix[k, k] = 1
        matrices.append(matrix)
    return matrices

def get_comparison_matrix(num_factors):
    matrix = np.zeros((num_factors, num_factors))
    for i in range(num_factors):
        for j in range(i+1, num_factors):
            value = float(input(f"Nhập giá trị so sánh giữa yếu tố {i+1} và yếu tố {j+1}: "))
            matrix[i, j] = value
            matrix[j, i] = 1/value
            matrix[i, i] = 1
            matrix[j, j] = 1
    return matrix

# Phương pháp Vector riêng
# def calculate_weights(matrix):
#     squared_matrix = np.square(matrix)
#     row_sums = np.sum(squared_matrix, axis=1)
#     weights = row_sums / np.sum(row_sums)
#     return weights

# Phương pháp chuẩn hóa ma trận
def calculate_weights(matrix):
    column_sums = np.sum(matrix, axis=0)
    normalized_matrix = matrix / column_sums
    row_sums = np.sum(normalized_matrix, axis=1)
    weights = row_sums / np.sum(row_sums)
    return weights

def consistency_index(matrix):
    n = matrix.shape[0]
    weights = calculate_weights(matrix)
    weighted_matrix = matrix * weights
    sum_weights = np.sum(weighted_matrix, axis=1)
    consistent_vector = sum_weights / weights
    lambda_max = np.mean(consistent_vector)
    consistency_index = (lambda_max - n) / (n - 1)
    return consistency_index

# Nhập vào số lượng phương án và số lượng yếu tố
num_plans = int(input("Nhập số lượng phương án: "))
num_factors = int(input("Nhập số lượng yếu tố: "))

# Nhập ma trận so sánh cho từng yếu tố
comparison_matrices = get_comparison_matrices(num_plans, num_factors)

# Nhập ma trận so sánh giữa các yếu tố
comparison_matrix = get_comparison_matrix(num_factors)

# Tính toán trọng số của ma trận so sánh giữa các yếu tố
weight = calculate_weights(comparison_matrix)

# Tính toán trọng số cho từng yếu tố
weights = []
for matrix in comparison_matrices:
    weights.append(calculate_weights(matrix))

weights = np.array(weights)

# Kiểm tra tính nhất quán của từng yếu tố
ri_value = [0, 0, 0.58, 0.9, 1.12, 1.24, 1.32, 1.41]
ri = ri_value[num_factors - 1]
crs = []
for matrix in comparison_matrices:
    ci = consistency_index(matrix)
    cr = ci/ri
    crs.append(cr)

# Kiểm tra tính nhất quán của ma trận so sánh giữa các yếu tố
ci = consistency_index(comparison_matrix)
cr_factor = ci/ri

# lấy tất ra giá trị cr
cr_all = crs
cr_all.append(cr_factor)
# print("\n Giá trị CR")
# print(cr_all)

#Tính toán giá trị cho từng phương án để đưa ra kết luận
results = []
for i in range(num_plans):
    result = weights[:, i] * weight
    sum_result = np.sum(result)
    results.append(sum_result)
# results = np.array(results)

# Tổng hợp và xếp hạng
plans = [f"phương án {i+1}" for i in range(num_plans)]
data = {'phương án': plans, 'Trọng số': results}
df = pd.DataFrame(data)
df = df.sort_values('Trọng số', ascending=False)
rankings = df.reset_index(drop=True)

print("Ma trận so sánh từng yếu tố:")
for i in range(num_factors):
    print(f"Yếu tố {i+1}:")
    print(comparison_matrices[i])
    print()

print("Ma trận so sánh giữa các yếu tố:")
print(comparison_matrix)

print("\nTrọng số của từng yếu tố:")
print(weights)
print("\nBộ trọng số cho từng phương án:")
for i in range(num_plans):
    print(f"Phương án {i+1}:")
    print(weights[:, i])
    print()
print("\nTrọng số của ma trận so sánh giữa các yếu tố:")
print(weight)
print("\nTính nhất quán của từng ma trận yếu tố:")
print(crs)
print("\nTính nhất quán của ma trận so sánh giữa yếu tố:")
print(cr_factor)
print("\nkết quả thu được sau khi tính toán:")
print(results)
print("\nXếp hạng:")
print(rankings)