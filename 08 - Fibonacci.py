def recursive_fibonacci(n):
	if n == 0:
		return 0
	if n == 1:
		return 1

	return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)

def iterative_fibonacci(n):
	if n == 0:
		return 0
	if n == 1:
		return 1

	a = 0
	b = 1

	for i in range(2, n + 1):
		total = a + b
		a = b
		b = total

	return total

print(recursive_fibonacci(30))
print(iterative_fibonacci(30))
