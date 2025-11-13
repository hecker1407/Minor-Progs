import numpy as np

def inverse_matrix(A):
    A = np.array(A, dtype=float)
    if A.shape[0] != A.shape[1]:
        raise ValueError("matrix must be square")
    det = np.linalg.det(A)
    if abs(det) < 1e-12:
        return np.linalg.pinv(A)
    return np.linalg.inv(A)

if __name__ == "__main__":
    A = [[4, 7], [2, 6]]
    invA = inverse_matrix(A)
    print("Input matrix:")
    print(np.array(A))
    print("Inverse (or pseudo-inverse if singular):")
    print(invA)
    print("Check A * invA:")
    print(np.dot(np.array(A, float), invA))
 