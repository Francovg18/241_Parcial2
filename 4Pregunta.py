#Pregunta4
import numpy as np
import scipy.sparse as sp

n = 1001

# Densidad de la matriz (fracción de elementos no ceros)
density = 0.01

# Matriz dispersa A en formato CSR
A = sp.random(n, n, density=density, format='csr')

# Matriz dispersa B en formato CSR
B = sp.random(n, n, density=density, format='csr')

# Multiplicación de matrices dispersas
C = A.dot(B)

print(f"A:\n{A}")
print(f"B:\n{B}")
print(f"C:\n{C}")
print(f"Shape of C: {C.shape}")
print(f"Number of non-zero elements in C: {C.nnz}")
