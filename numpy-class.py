import numpy as np

# 1. Creating arrays
array_1d = np.array([1, 2, 3, 4, 5])
print("1D array:", array_1d)

array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("2D array:\n", array_2d)

# 2. Array attributes
print("Shape of 2D array:", array_2d.shape)
print("Data type of elements:", array_2d.dtype)
print("Size of array:", array_2d.size)
print("Number of dimensions:", array_2d.ndim)

# 3. Array initialization
zeros_array = np.zeros((2, 3))
print("Zeros array:\n", zeros_array)

ones_array = np.ones((2, 3))
print("Ones array:\n", ones_array)

identity_matrix = np.eye(3)
print("Identity matrix:\n", identity_matrix)

# 4. Array operations
sum_array = array_1d + 5
print("Array after addition:", sum_array)

product_array = array_1d * 2
print("Array after multiplication:", product_array)

matrix_product = np.dot(array_2d, array_2d.T)
print("Matrix product:\n", matrix_product)

# 5. Slicing and indexing
print("First element of 1D array:", array_1d[0])
print("Last element of 1D array:", array_1d[-1])
print("First row of 2D array:\n", array_2d[0, :])
print("First column of 2D array:\n", array_2d[:, 0])

# 6. Statistical operations
mean_value = np.mean(array_1d)
print("Mean value of 1D array:", mean_value)

sum_value = np.sum(array_2d)
print("Sum of elements in 2D array:", sum_value)

# 7. Reshaping arrays
reshaped_array = array_1d.reshape((5, 1))
print("Reshaped array:\n", reshaped_array)

# 8. Concatenation and stacking
array_a = np.array([[1, 2], [3, 4]])
array_b = np.array([[5, 6], [7, 8]])

concatenated_array = np.concatenate((array_a, array_b), axis=0)
print("Concatenated array along rows:\n", concatenated_array)

stacked_array = np.stack((array_a, array_b), axis=1)
print("Stacked array along a new axis:\n", stacked_array)

# 9. Creating special arrays
linspace_array = np.linspace(0, 10, 5)
print("Linspace array:", linspace_array)

random_array = np.random.random((2, 2))
print("Random array:\n", random_array)

# 10. Boolean indexing
bool_index = array_1d > 3
print("Boolean indexing:", bool_index)
print("Elements greater than 3:", array_1d[bool_index])
