#Pregunta5
import numpy as np
from scipy.sparse import csr_matrix
from multiprocessing import Pool

def multiply_row(row):
    return A.getrow(row).dot(B).toarray()

def parallel_multiply(A, B, num_processes):
    with Pool(num_processes) as pool:
        result = pool.map(multiply_row, range(A.shape[0]))
    return np.vstack(result)

# Generar matrices sparse aleatorias
A = csr_matrix(np.random.random((1001, 1001)))
B = csr_matrix(np.random.random((1001, 1001)))

# Número de procesos 
num_processes = 4

# Multiplicar matrices en paralelo
C = parallel_multiply(A, B, num_processes)
print(C)
