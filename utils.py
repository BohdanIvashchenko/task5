def factorial(n):
	res = 1
	for i in range(1, n + 1):
		res *= i
	return res

def prime(n):
	for i in range(2, n):
			if n % i == 0:
				return False
	return True