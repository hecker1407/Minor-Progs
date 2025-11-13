import numpy as np
from scipy.optimize import minimize

def qp_interior_point(Q, c, Aeq=None, beq=None, bounds=None, x0=None):
    Q = np.array(Q, dtype=float)
    c = np.array(c, dtype=float)
    n = Q.shape[0]
    def obj(x):
        return 0.5 * x.dot(Q.dot(x)) + c.dot(x)
    def jac(x):
        return Q.dot(x) + c
    cons = []
    if Aeq is not None:
        Aeq = np.array(Aeq, dtype=float)
        beq = np.array(beq, dtype=float)
        for i in range(Aeq.shape[0]):
            cons.append({'type': 'eq', 'fun': lambda x, A=Aeq[i], b=beq[i]: A.dot(x) - b, 'jac': lambda x, A=Aeq[i]: A})
    res = minimize(obj, x0 if x0 is not None else np.zeros(n), method='trust-constr', jac=jac, constraints=cons, bounds=bounds, options={'gtol':1e-8, 'maxiter':1000})
    return res.x, res.fun, res.success

def qp_gradient_descent(Q, c, x0=None, lr=1e-3, max_iters=100000, tol=1e-8):
    Q = np.array(Q, dtype=float)
    c = np.array(c, dtype=float)
    n = Q.shape[0]
    if x0 is None:
        x = np.zeros(n)
    else:
        x = np.array(x0, dtype=float)
    for i in range(max_iters):
        grad = Q.dot(x) + c
        step = -lr * grad
        x = x + step
        if np.linalg.norm(step) < tol:
            break
    return x, 0.5 * x.dot(Q.dot(x)) + c.dot(x), i+1

if __name__ == "__main__":
    Q = [[6, 0], [0, 2]]
    c = [-12, -4]
    bounds = [(0, None), (0, None)]
    x_ip, val_ip, ok = qp_interior_point(Q, c, bounds=bounds)
    x_gd, val_gd, iters = qp_gradient_descent(Q, c, lr=0.1)
    print("Interior-point result x:", x_ip)
    print("Interior-point objective:", val_ip, "success:", ok)
    print("Gradient descent result x:", x_gd)
    print("Gradient descent objective:", val_gd, "iterations:", iters)
