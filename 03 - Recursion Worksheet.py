from timeit import default_timer as timer

# Number 1
def laugh(times, string):
	if times == 1:
		print(string)
	elif times > 1:
		print(string, end="")
		laugh(times - 1, string)


laugh(3, "Ha")

# Number 2
def add_up(upTo):
	if upTo == 1:
		return 1
	else:
		return upTo + add_up(upTo - 1)

print(add_up(4))

# Number 3
def reverse_string(string):
	if len(string) <= 1:
		return string
	else:
		return string[-1] + reverse_string(string[:-1])

print(reverse_string("Hello"))

# Number 4
def list_length(list):
	if not list:
		return 0
	else:
		list.pop()
		return 1 + list_length(list)

print(list_length([]))
print(list_length([1, 2, 3, 4]))
print(list_length([1, 2, 3, 4, 5, 6, 7, 8]))

# Number 5
def recursive_factorial(upTo):
	if upTo == 0:
		return 1
	else:
		return upTo * recursive_factorial(upTo - 1)

print(recursive_factorial(5))

def iterative_factorial(upTo):
	if upTo <= 1:
		return 1

	total = 1

	for i in range(2, upTo + 1):
		total *= i

	return total

print(iterative_factorial(5))

NUMBER_OF_TIMES = 10000
UP_TO = 32

recursiveStart = timer()
for i in range(NUMBER_OF_TIMES):
	recursive_factorial(UP_TO)
recursiveEnd = timer()

iterativeStart = timer()
for i in range(NUMBER_OF_TIMES):
	iterative_factorial(UP_TO)
iterativeEnd = timer()

print(f"Recursive: {recursiveEnd - recursiveStart} seconds")
print(f"Iterative: {iterativeEnd - iterativeStart} seconds")

# Number 6
def fibbonacci(upTo):
	if upTo <= 2:
		return 1
	else:
		return fibbonacci(upTo - 1) + fibbonacci(upTo - 2)

print(fibbonacci(2))
print(fibbonacci(7))

# Number 7
def any_7(list):
	if list[0] == 7:
		return 0
	else:
		list.pop(0)
		return 1 + any_7(list)

print(any_7([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(any_7([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))

# Number 8
def both_equal(string1, string2):
	if (string1 and not string2) or (string2 and not string1):
		return False

	if not (string1 and string2):
		return True

	if string1[0] == string2[0]:
		return both_equal(string1[1:], string2[1:])
	else:
		return False

print(both_equal("Hello", "Hello"))
print(both_equal("Hello", "olleH"))
print(both_equal("Hello", ""))
print(both_equal("", ""))

# Number 9
def count_down(numberFrom):
	if numberFrom == 0:
		print("0")
	else:
		print(numberFrom, end="")
		count_down(numberFrom - 1)

count_down(5)

# Number 10
def square_list(list, index = 0):
	if (not list) or (index >= len(list)):
		return list
	else:
		list[index] *= list[index]
		list = square_list(list, index + 1)

	return list

print(square_list([3, 4, 5, 6]))
