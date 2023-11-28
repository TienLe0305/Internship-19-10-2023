import numpy as np


def matrix_factorization(Dtrain, K, B, A, max_iter=5000, tol=1e-5):
    n_users, n_items = Dtrain.shape
    W = np.random.rand(n_users, K)
    H = np.random.rand(n_items, K).T  # Transpose for matrix multiplication
    err_prev = float('inf')
    for iteration in range(max_iter):
        u, i = np.random.randint(n_users), np.random.randint(n_items)
        if Dtrain[u, i] > 0:  # Only update for non-zero entries
            r = Dtrain[u, i]
            err = r - np.dot(W[u, :], H[:, i])
            W[u, :] += B * (err * H[:, i] - A * W[u, :])
            H[:, i] += B * (err * W[u, :] - A * H[:, i])
        # Recompute error for stopping condition
        if iteration % 100 == 0:  # Check error every 100 iterations
            err = np.linalg.norm(Dtrain - np.dot(W, H), ord='fro')
            if np.abs(err - err_prev) < tol:
                break
            err_prev = err
    return W, H.T  # Return H to its original orientation
n = int(input("Nhập giá trị n: "))
Dtrain = np.random.randint(0, 5, size=(n, n))
K = 3
B = 0.01
A = 0
W, H = matrix_factorization(Dtrain, K, B, A)
print("Ma trận ban đầu")
print(Dtrain)
print("Ma trận W")
print(W)
print("Ma trận H")
print(H)
