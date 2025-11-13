import numpy as np

def simplex(c, A, b):
    c = np.array(c, dtype=float)
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    m, n = A.shape
    tableau = np.zeros((m + 1, n + m + 1))
    tableau[:m, :n] = A
    tableau[:m, n:n+m] = np.eye(m)
    tableau[:m, -1] = b
    tableau[-1, :n] = -c
    basis = list(range(n, n + m))
    while True:
        col = None
        for j in range(tableau.shape[1]-1):
            if tableau[-1, j] < -1e-12:
                col = j
                break
        if col is None:
            break
        ratios = []
        for i in range(m):
            aij = tableau[i, col]
            if aij > 1e-12:
                ratios.append(tableau[i, -1]/aij)
            else:
                ratios.append(np.inf)
        row = int(np.argmin(ratios))
        if ratios[row] == np.inf:
            raise ValueError("Unbounded")
        pivot = tableau[row, col]
        tableau[row, :] = tableau[row, :] / pivot
        for i in range(m+1):
            if i != row:
                tableau[i, :] = tableau[i, :] - tableau[i, col] * tableau[row, :]
        basis[row] = col
    x = np.zeros(n + m)
    for i in range(m):
        x[basis[i]] = tableau[i, -1]
    return x[:n], tableau[-1, -1]

if __name__ == "__main__":
    c = [3, 2]
    A = [[1, 2], [4, 0], [0, 4]]
    b = [8, 16, 12]
    x_opt, val = simplex(c, A, b)
    print("Maximizer x:", x_opt)
    print("Maximum objective value:", val)
