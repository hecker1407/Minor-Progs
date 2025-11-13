import numpy as np

def gradient_descent(A, b, x0=None, lr=0.1, max_iters=1000, tol=1e-8):
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    n = A.shape[0]
    if x0 is None:
        x = np.zeros(n)
    else:
        x = np.array(x0, dtype=float)
    for i in range(max_iters):
        grad = A.dot(x) + b
        step = -lr * grad
        x = x + step
        if np.linalg.norm(step) < tol:
            break
    return x, i+1

if __name__ == "__main__":
    A = np.array([[4, 0], [0, 2]])
    b = np.array([-8, -4])
    x_opt, iters = gradient_descent(A, b, lr=0.2, max_iters=10000)
    print("Found minimizer x:", x_opt)
    print("Iterations:", iters)
    print("Objective value:", 0.5 * x_opt.dot(A.dot(x_opt)) + b.dot(x_opt))
