import numpy as np
from scipy import linalg

A = np.array([[3., 2.], [1., 4.]])
b = np.array([6., 5.])

x = linalg.solve(A, b)
print("Solution x =", x)
print("A @ x =", A.dot(x))
