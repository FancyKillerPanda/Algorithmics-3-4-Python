# This is the triomino number, it is incremeted after every triomino is addded
currentNumber = 1

# If board is n*n, size = n
# row, col determine location of the missing piece
# rowOffset and colOffset are used to pretend we start in the top left quadrant, even if we don't
def tile_board(board, size, row, col, rowOffset = 0, colOffset = 0):
	global currentNumber

	# Don't need to do anything
	if size <= 1:
		return

	# Base case: draw a single triomino
	if size == 2:
		for i in range(2):
			for j in range(2):
				if i != row or j != col:
					board[int(rowOffset + i)][int(colOffset + j)] = currentNumber

		currentNumber += 1
		return

	# The locations of the new "missing" pieces, relative to the top left of each smaller square
	locations = [
		[(size / 2) - 1, (size / 2) - 1],
		[0, (size / 2) - 1],
		[(size / 2) - 1, 0],
		[0, 0]
	]

	# The offset of the top-left of each smaller square
	locationOffsets = [
		[rowOffset, colOffset],
		[rowOffset + (size / 2), colOffset],
		[rowOffset, colOffset + (size / 2)],
		[rowOffset + (size / 2), colOffset + (size / 2)]
	]

	# We want to keep the actual missing piece in the same location.
	# It requires some adjustment because of the smaller square offset.
	if row < size / 2 and col < size / 2:
		changedIndex = 0
		locations[0] = [int(row - 0), int(col - 0)]
	elif row >= size / 2 and col < size / 2:
		changedIndex = 1
		locations[1] = [int(row - (size / 2)), int(col - 0)]
	elif row < size / 2 and col >= size / 2:
		changedIndex = 2
		locations[2] = [int(row - 0), int(col - (size / 2))]
	elif row >= size / 2 and col >= size / 2:
		changedIndex = 3
		locations[3] = [int(row - (size / 2)), int(col - (size / 2))]

	# Fills in the triomino of the "missing"
	for index, (location, locationOffset) in enumerate(zip(locations, locationOffsets)):
		if index == changedIndex: # Not the one which has the actual missing piece
			continue
		board[int(locationOffset[0] + location[0])][int(locationOffset[1] + location[1])] = currentNumber

	currentNumber += 1

	# Recursively solves the puzzle, cutting the size in half and adjuusting the offsets
	for location, locationOffset in zip(locations, locationOffsets):
		tile_board(board, size / 2, location[0], location[1], locationOffset[0], locationOffset[1])

# The zeroes are just fillers, they will get overwritten.
# The location of the missing piece is determined by the tile_board() call
board = [
	[0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0],
]

# Helper method to print out the board
def print_board(board):
	for row in board:
		for value in row:
			print(value, end="\t") # We end in a tab so the spacing is even

		print()

# Runs the program
tile_board(board, 8, 1, 1)
print_board(board)
