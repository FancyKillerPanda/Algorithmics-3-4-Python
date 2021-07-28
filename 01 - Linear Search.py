def linear_search(array, target):
	for value in array:
		if value == target:
			print("Target found!")
			break
	else:
		print("Target does not exist in the array!")

array = [47, 14, 5, 580, 2, 1, 6, 9, 4, 10]
linear_search(array, 0)
linear_search(array, 1)
