from google.colab import drive
import os
import cv2
import numpy as np
from matplotlib import pyplot as plt
from scipy.sparse import csr_matrix
drive.mount("/content/drive")
os.chdir("/content/drive/MyDrive/2do:241")

img1_path = 'img1.jpg'
img2_path = 'img2.jpg'

img1 = cv2.imread(img1_path, cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread(img2_path, cv2.IMREAD_GRAYSCALE)

# Crear matrices dispersas CSR para cada imagen
sparse_img1 = csr_matrix(img1.flatten())
sparse_img2 = csr_matrix(img2.flatten())

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(img1, cmap='gray')
plt.title('Imagen 1')

plt.subplot(1, 2, 2)
plt.imshow(img2, cmap='gray')
plt.title('Imagen 2')

plt.show()

# Imprimir 
print("Matriz dispersa de la Imagen 1:")
print(sparse_img1)

print("\nMatriz dispersa de la Imagen 2:")
print(sparse_img2)

'''
#Pregunta2
import networkx as nx
from scipy.sparse import csr_matrix, vstack

# Crear los grafos más complejos
G1 = nx.Graph()
G1.add_edges_from([(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)])

G2 = nx.Graph()
G2.add_edges_from([(0, 2), (2, 1), (1, 3), (3, 4)])

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

# Extender A3_sparse
A1_extended = csr_matrix((max_rows, max_cols))
A1_extended[:rows1, :cols1] = A1_sparse

# Extender A4_sparse
A2_extended = csr_matrix((max_rows, max_cols))
A2_extended[:rows2, :cols2] = A2_sparse

# Combinar matrices dispersas
combined_sparse_matrix = vstack([A1_extended, A2_extended])

# Imprimir la matriz dispersa combinada
print("Matriz dispersa combinada:\n", combined_sparse_matrix)


'''
