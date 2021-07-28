def sequentialSearch(array, target):
	for i, element in enumerate(array):
		if element == target:
			return i

	return None

array = [3, 2, 6, 1, 5, 4]
print(sequentialSearch(array, 2))
print(sequentialSearch(array, 0))

def printMatrix(matrix):
	print("Matrix:")

	for row in matrix:
		print("\t[", end = " ")

		for col in row:
			print(col, end = " ")

		print("]")

def addMatrices(matrixA, matrixB):
	result = []

	for row in range(0, len(matrixA)):
		newRow = []

		for col in range(0, len(matrixA[row])):
			newRow.append(matrixA[row][col] + matrixB[row][col])

		result.append(newRow)

	return result

# NOTE(fkp): This doesn't work
def multiplyMatrices(matrixA, matrixB):
	# result = [[0] * len(matrixA)] * len(matrixA[0])

	result = []
	for row in range(0, len(matrixA)):
		result.append([])
		for col in range(0, len(matrixA[row])):
			result[row].append(0)

	for row in range(0, len(matrixA)):
		for col in range(0, len(matrixA[row])):
			result[row][col] += matrixA[row][col] * matrixB[col][row]

	return result

matrixA = [
	[1, 2],
	[3, 4]
]
matrixB = [
	[2, 4],
	[3, 1]
]
printMatrix(addMatrices(matrixA, matrixB))
printMatrix(multiplyMatrices(matrixA, matrixB))
