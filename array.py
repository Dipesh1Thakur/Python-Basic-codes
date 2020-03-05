import numpy as np

#A=np.array([1,3,5,7])
#print (A)

#matrix =np.mat([[1,2],[3,4]])
#print(matrix)

matrix =np.mat([[1,2,3],[3,4,5]])
print(matrix)

print('Shape:',matrix.shape) # gives the dimesion of matrix
print("size:",matrix.size) #gives the number of elements
print("data type :",matrix.dtype) # gives the data type 
print('size in bytes',matrix.itemsize) # gives size in bytes


matrix1= np.arange(6).reshape(2,2,2)
print(matrix1)
A=np.array([2,3],[4,5])
B=np.array([1,2],[3,4])
total -A+B

print(total)

difference =B - A
print(difference)

product =A*B
print(priduct)
product= A.dot(B)
print(product)

# determinant
print('determinant of B', np.linalg.deb(B))

#Transpose
print("tramspose of B", np.matrix.transpose(B))
