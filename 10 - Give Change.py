coins = [1, 3, 4]

def give_change(amount):
	if amount < coins[0]:
		return None

	for coin in coins:
		if amount == coin:
			return 1

	minimum = 999999999999

	for coin in coins:
		value = give_change(amount - coin)
		if value == None:
			continue

		if value < minimum:
			minimum = value

	return minimum + 1


def give_change_1(amount):
	if amount < coins[0]:
		return None

	for coin in coins:
		if amount == coin:
			return [coin]

	coinUsed = -1
	minimum = 999999999999
	value = []

	for coin in coins:
		value = give_change_1(amount - coin)

		if value == None:
			continue

		if len(value) < minimum:
			minimum = len(value)
			coinUsed = coin

	if value == None:
		return None
		
	value.append(coinUsed)
	return value

# print([(i, give_change(i)) for i in range(30)])
print(give_change_1(6))
