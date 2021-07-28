# pegs = [[16, 15, 14, 13, 12, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [], []]
NUMBER_OF_DISKS = 16
pegs = [list(range(NUMBER_OF_DISKS, 0, -1)), [], []]

# """
def move_disks(number, start, end):
	global pegs

	if number == 1:
		pegs[end].append(pegs[start].pop())
	else:
		# Finds the intermediate
		intermediate = 3 - (start + end)

		move_disks(number - 1, start, intermediate)
		pegs[end].append(pegs[start].pop())
		move_disks(number - 1, intermediate, end)


move_disks(len(pegs[0]), 0, 2)
print(pegs)
# """


""" DIRTY LITTLE CHEATER!!!
def move_disks():
	global pegs
	pegs.append(pegs.pop(0))

move_disks()
print(pegs)
# """
