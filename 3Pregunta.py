from google.colab import drive
import os
import cv2
from google.colab.patches import cv2_imshow

drive.mount("/content/drive")

os.chdir("/content/drive/MyDrive/2do:241")

image1_path = 'img1.jpg'
image2_path = 'img2.jpg'

image1 = cv2.imread(image1_path)
image2 = cv2.imread(image2_path)

if image1 is None:
    print(f"No se pudo cargar la imagen en {image1_path}")
elif image2 is None:
    print(f"No se pudo cargar la imagen en {image2_path}")
else:
    # Asegurarse de que las imágenes tengan las mismas dimensiones
    if image1.shape != image2.shape:
        print("Las imágenes no tienen las mismas dimensiones. Cambia el tamaño de una de las imágenes.")
        # Cambiar el tamaño de image2 a las dimensiones de image1
        image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))

    # Realizar la suma de las dos imágenes
    sum_image = cv2.add(image1, image2)

    # Realizar la resta de las dos imágenes
    sub_image = cv2.subtract(image1, image2)

    # Mostrar las imágenes originales y las resultantes
    cv2_imshow(image1)
    cv2_imshow(image2)
    cv2_imshow(sum_image)
    cv2_imshow(sub_image)
