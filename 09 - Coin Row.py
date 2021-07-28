def solve_coin_row(row):
	if len(row) == 0:
		return 0
	if len(row) == 1:
		return row[0]
	if len(row) == 2:
		return max(row[0], row[1])

	i = 1
	indices = []
	total = 0
	
	row.append(0)

	while i < len(row) - 1:
		if (row[i] > row[i - 1] + row[i + 1]):
			if i not in indices:
				print("Abc")
				total += row[i]
				indices.append(i)

			if i - 1 in indices:
				total -= row[i - 1]
				indices.remove(i - 1)

			if i + 1 in indices:
				total -= row[i + 1]
				indices.remove(i + 1)

			i += 1
		else:
			print("Here")
			if i - 1 not in indices:
				total += row[i - 1]
				indices.append(i - 1)
			if i + 1 not in indices:
				total += row[i + 1]
				indices.append(i + 1)

			if i in indices:
				total -= row[i]
				indices.remove(i)

			i += 2

	return total

#print(solve_coin_row([]))					# Should be 0
#print(solve_coin_row([1]))					# Should be 1
#print(solve_coin_row([1, 2]))				# Should be 2
#print(solve_coin_row([1, 2, 3]))			# Should be 4
print(solve_coin_row([1, 2, 3, 4]))			# Should be 6
#print(solve_coin_row([1, 2, 3, 4, 5]))		# Should be 9
#print(solve_coin_row([5, 1, 2, 10, 6, 2]))	# Should be 17
