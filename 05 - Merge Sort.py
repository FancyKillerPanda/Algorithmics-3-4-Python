# Takes two sorted arrays and combines them
# For example:
#	[1, 2, 3, 4] and [3, 4, 5, 6] -> [1, 2, 3, 3, 4, 4, 5, 6]
def merge_arrays(arrayA, arrayB):
	output = []
	bIndex = 0 # Keeps track of how much of arrayB we have added

	for a in arrayA:
		# Adds everything in arrayB that is lower than this value first
		while bIndex < len(arrayB) and arrayB[bIndex] < a:
			output.append(arrayB[bIndex])
			bIndex += 1

		output.append(a)

	# Everything else in arrayB (higher than the highest value of arrayA)
	while bIndex < len(arrayB):
		output.append(arrayB[bIndex])
		bIndex += 1

	return output

def merge_sort(array):
	# Base case (section of length 1)
	if len(array) == 1:
		return array

	# Recursively gets the two halves
	sectionA = merge_sort(array[0 : len(array) // 2])
	sectionB = merge_sort(array[len(array) // 2 : len(array)])

	return merge_arrays(sectionA, sectionB)

array = [1, 5, 3, 2, 4, 6]
print(merge_sort(array))
