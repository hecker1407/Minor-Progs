import numpy as np

A=np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

B=np.array([
    [0,0,0],
    [0,1,0],
    [0,0,1]
])

M=np.array([
    [0,0,0],
    [0,0,0],
    [0,0,0]
])
for i in range(3):
    for j in range(3):
         for k in range(3):
             M[i][j]+=A[i][k]*B[k][j]
         print (M[i][j],"",end=" ")
    print("\n")    



 