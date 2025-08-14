import numpy as np

def forward_elimination(A, b):
    n = len(A)
    for i in range(n):
        max_element = abs(A[i][i])
        max_row = i
        for k in range(i + 1, n):
            if abs(A[k][i]) > max_element:
                max_element = abs(A[k][i])
                max_row = k
        if max_element < 1e-10:
            continue
        
        if max_row != i:
            A[i], A[max_row] = A[max_row].copy(), A[i].copy()
            b[i], b[max_row] = b[max_row], b[i]
            
        pivot = A[i][i]
        for j in range(i + 1, n):
            factor = A[j][i] / pivot
            A[j] = A[j] - factor * A[i]
            b[j] = b[j] - factor * b[i]
    return A, b

def check_infinite_solutions(A, b):
    n = len(A)
    rank_A = 0
    rank_Ab = 0
    
    for i in range(n):
        if not all(abs(A[i][j]) < 1e-10 for j in range(n)):
            rank_A += 1
        if not all(abs(A[i][j]) < 1e-10 for j in range(n)) or abs(b[i]) >= 1e-10:
            rank_Ab += 1
    
    if rank_A < n and rank_A == rank_Ab:
        return True
    return False

def back_substitution(A, b):
    n = len(A)
    x = np.zeros(n)
    
    if check_infinite_solutions(A, b):
        return None, "Infinite solutions exist"
    
    for i in range(n-1, -1, -1):
        if abs(A[i][i]) < 1e-10:
            if abs(b[i]) >= 1e-10:
                return None, "No consistent solution exists"
            continue
        sum_ax = sum(A[i][j] * x[j] for j in range(i+1, n))
        x[i] = (b[i] - sum_ax) / A[i][i]
    return x, "Unique solution found"

def gaussian_elimination(A, b):
    if A.shape[0] != A.shape[1]:
        return None, "Not a square matrix"
    
    A = A.astype(float)
    b = b.astype(float)
    A, b = forward_elimination(A, b)
    return back_substitution(A, b)

n = int(input("Enter the number of variables: "))
print("\nEnter the augmented matrix [A|b] row by row:")
print("For each row, enter all coefficients including the constant, separated by spaces")

augmented = []
for i in range(n):
    row = list(map(float, input(f"Row {i+1}: ").split()))
    augmented.append(row)

augmented = np.array(augmented)
A = augmented[:, :-1]
b = augmented[:, -1]

solution, message = gaussian_elimination(A, b)
if solution is not None:
    print("\nSolution:")
    for i, x in enumerate(solution):
        print(f"x{i+1} = {x:.4f}")
else:
    print(f"\nMessage: {message}")