import numpy as np
matrice_1 = np.ones((6,6))
matrice_2 = np.ones((6,6))
matrice_1 = matrice_1*2
matrice_2 = matrice_2*4
print('Matrice 1 = ',matrice_1)
print('Matriec 2 = ',matrice_2)

# Euclidian Distance
euclidian =(matrice_1**2)-(matrice_2**2)
#print ('Euclidian =', euclidian )
euclidian = np.sum(euclidian)
euclidian = np.sqrt(euclidian)
print('The Euclidian Distance is = ', euclidian)

# Manhattan Distance
manhattan = (matrice_1 - matrice_2)
#print ("Manhattan = ", manhattan)
manhattan = np.abs(manhattan)
manhattan = np.sum(manhattan)
print('The Manhatan Distance is = ',manhattan)
