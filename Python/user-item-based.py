import numpy as np

def hybrid_recommendation_system(Dtrain, K, B, A, max_iter=5000, tol=1e-5):
    n_users, n_items = Dtrain.shape
    # Khởi tạo ma trận người dùng (User Matrix)
    W_user = np.random.rand(n_users, K)
    # Khởi tạo ma trận sản phẩm (Item Matrix)
    H_item = np.random.rand(n_items, K).T  # Transpose for matrix multiplication
    err_prev = float('inf')
    for iteration in range(max_iter):
        for u in range(n_users):
            for i in range(n_items):
                if Dtrain[u, i] > 0:  # Chỉ xử lý các mục đã được đánh giá
                    r = Dtrain[u, i]
                    err = r - np.dot(W_user[u, :], H_item[:, i])
                    # Cập nhật ma trận người dùng dựa trên lỗi
                    W_user[u, :] += B * (err * H_item[:, i] - A * W_user[u, :])
                    # Cập nhật ma trận sản phẩm dựa trên lỗi
                    H_item[:, i] += B * (err * W_user[u, :] - A * H_item[:, i])
        # Recompute error for stopping condition
        err = np.linalg.norm(Dtrain - np.dot(W_user, H_item), ord='fro')
        if np.abs(err - err_prev) < tol:
            break
        err_prev = err
    return W_user, H_item.T

# Tham số mô phỏng
n_users = 10
n_items = 15
Dtrain = np.random.randint(0, 5, size=(n_users, n_items))
# Số đặc trưng ẩn
K = 3
# Tỷ lệ học
B = 0.01
# Trừng phạt thuật ngữ quá khớp
A = 0.1
W_user, H_item = hybrid_recommendation_system(Dtrain, K, B, A)
print("Ma trận đánh giá ban đầu")
print(Dtrain)
print("Ma trận người dùng (User Matrix)")
print(W_user)
print("Ma trận sản phẩm (Item Matrix)")
print(H_item)