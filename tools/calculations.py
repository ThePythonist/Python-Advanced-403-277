def isPrime(num):
	divs = [i for i in range(1,num+1) if num % i == 0]
	return True if len(divs) == 2 else False
