import numpy as np

from collections import defaultdict

# Hàm tính trung bình độ mờ Fuzzy
def fuzzy_aggregate(matrix):
    # Tính trung bình theo cột của ma trận
    return np.mean(matrix, axis=0)

# Hàm tính trọng số chuẩn hóa Fuzzy
def normalize_weights(w_aggregate):
    normalized_weights = defaultdict(float)
    
    # Tổng các trung bình ở mức độ mờ (hàng thứ hai của triplet)
    total_weights = np.sum(w_aggregate[1])
    for index, weight in enumerate(w_aggregate[1]):
        normalized_weights[f'criteria{index + 1}'] = weight / total_weights
    return normalized_weights

# Tạo 'fuzzy' ma trận đối sánh
fuzzy_matrix = np.array([
    [(1, 1, 1), (1/2, 2/3, 1)],
    [(1, 3/2, 2), (1, 1, 1)]
])

# Tính trung bình độ mờ Fuzzy và chuẩn hóa trọng số
fuzzy_weighted_average = fuzzy_aggregate(fuzzy_matrix)
normalized_fuzzy_weights = normalize_weights(fuzzy_weighted_average)
print("Trung bình độ mờ Fuzzy: ", fuzzy_weighted_average)
print("Trọng số chuẩn hóa Fuzzy: ", dict(normalized_fuzzy_weights))