import networkx as nx
from scipy.sparse import csr_matrix, vstack, hstack
import numpy as np

# Crear los grafos
G1 = nx.Graph()
G1.add_edges_from([(0, 1), (1, 2), (2, 3)])

G2 = nx.Graph()
G2.add_edges_from([(0, 2), (2, 1), (1, 3)])

# Convertir grafos a matrices de adyacencia
A1 = nx.adjacency_matrix(G1)
A2 = nx.adjacency_matrix(G2)

# Asegurarse de que son matrices dispersas CSR
A1_sparse = csr_matrix(A1)
A2_sparse = csr_matrix(A2)

# Ajustar dimensiones para que ambas matrices tengan el mismo tamaño
rows1, cols1 = A1_sparse.shape
rows2, cols2 = A2_sparse.shape

max_rows = max(rows1, rows2)
max_cols = max(cols1, cols2)

A1_extended = csr_matrix((max_rows, max_cols))
A1_extended[:rows1, :cols1] = A1_sparse

A2_extended = csr_matrix((max_rows, max_cols))
A2_extended[:rows2, :cols2] = A2_sparse

# Combinar matrices dispersas
combined_sparse_matrix = vstack([A1_extended, A2_extended])

print(combined_sparse_matrix)

