# Sahil - 2021-07-20

board = [
	[0, 0, 0, 0, 0],
	[0, 1, 0, 0, 0],
	[0, 0, 1, 1, 1],
	[0, 0, 0, 0, 1],
	[0, 0, 0, 0, 0],
	[0, 0, 0, 1, 0],
	[0, 0, 0, 0, 1],
]

board_filled = [[-1 for j in range(len(board[0]))] for i in range(len(board))]

def find_max_coins(row, col):
	previousRow = 0
	if row > 0:
		if board_filled[row - 1][col] != -1:
			previousRow = board_filled[row - 1][col]
		else:
			previousRow = find_max_coins(row - 1, col)

	previousCol = 0
	if col > 0:
		if board_filled[row][col - 1] != -1:
			previousCol = board_filled[row][col - 1]
		else:
			previousCol = find_max_coins(row, col - 1)

	board_filled[row][col] = board[row][col] + max(previousRow, previousCol)
	return board_filled[row][col]

def trace_path(row, col):
	path = [[0 for j in range(len(board[0]))] for i in range(len(board))]

	currentRow = row
	currentCol = col
	path[currentRow][currentCol] = 1

	while True:
		path[currentRow][currentCol] = 1

		if currentRow == 0:
			if currentCol == 0:
				break
			else:
				currentCol -= 1
		else:
			if currentCol == 0:
				currentRow -= 1
			else:
				if board_filled[currentRow - 1][currentCol] > board_filled[currentRow][currentCol - 1]:
					currentRow -= 1
				else:
					currentCol -= 1

	print(f"\nPath to ({row}, {col}):")
	for printRow in path:
		print(printRow)

print(find_max_coins(0, 0))
print(find_max_coins(0, 3))
print(find_max_coins(3, 0))
print(find_max_coins(3, 3))
print(find_max_coins(4, 4))
print(find_max_coins(6, 4))

trace_path(6, 4)
