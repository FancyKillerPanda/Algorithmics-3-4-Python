weights = [ 6, 2,  4,  3, 11]
values =  [20, 8, 14, 13, 35]


def unbounded_knapsack(capacity):
	solved = [0 for i in range(capacity + 1)]

	for currentCapacity in range(capacity + 1):
		objects = zip(weights, values)
		
		for weight, value in objects:
			if weight <= currentCapacity:
				solved[currentCapacity] = max(solved[currentCapacity], solved[currentCapacity - weight] + value)

	return solved

print(unbounded_knapsack(10))
