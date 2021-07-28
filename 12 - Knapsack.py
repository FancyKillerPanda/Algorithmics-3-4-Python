maxWeight = 4
weights = [2, 1, 4]
values  = [5, 3, 9]
table = [[0 for i in range(maxWeight + 1)] for j in range(len(values))] # +1 to add a 0 column

for i in range(len(values)):
	for j in range(maxWeight + 1): # +1 because range() has non-inclusive upper-bound
		if weights[i] > j:
			continue

		table[i][j] = max(table[i - 1][j], table[i - 1][j - weights[i]] + values[i])

# Printing
print(list(range(len(table[0]))))
print("===================")
for row in table:
	print(row)

print(f"\nMax Value: ${table[-1][-1]}")
