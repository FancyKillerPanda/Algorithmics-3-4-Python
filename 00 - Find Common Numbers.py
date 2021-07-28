def findCommonNumbers(listA, listB):
	listC = []

	if len(listA) == 0 or len(listB) ==0:
		return listC

	listA.sort()
	listB.sort()

	indexA = 0
	indexB = 0

	while indexA < len(listA):
		while listB[indexB] < listA[indexA]:
			indexB += 1

			if indexB >= len(listB):
				return listC

		if listA[indexA] == listB[indexB]:
			listC.append(listA[indexA])

		indexA += 1

	return listC


print(findCommonNumbers([], []))
print(findCommonNumbers([0], []))
print(findCommonNumbers([], [0]))
print(findCommonNumbers([0, 1, 2], [1, 2, 3]))
print(findCommonNumbers([0, 1, 2], [3, 4, 5]))
print(findCommonNumbers([0, 1, 2], [0, 1, 2]))
print(findCommonNumbers([2, 1, 6], [4, 2, 3]))
input()
