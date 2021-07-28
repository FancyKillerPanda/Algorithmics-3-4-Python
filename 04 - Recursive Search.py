def iterative_search(array, target):
	for i, item in enumerate(array):
		if item == target:
			return i

	return None

def recursive_search(array, target, start = 0, end = None): # start inclusive, end not
	# Initial check
	if end == None:
		end = len(array)

	# Searching a section of length 1
	if end - start == 1:
		if array[start] == target:
			return start
		else:
			return None

	# Recursion
	result = recursive_search(array, target, start, start + (((end - start) // 2)))
	if result == None:
		result = recursive_search(array, target, start + ((end - start) // 2), end)

	return result




array = [1, 4, 5, 8, 10]
target = 8
print(iterative_search(array, target))
print(recursive_search(array, target))
