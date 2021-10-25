"""
https://projecteuler.net/problem=2

Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""

even_numbers = 0
i = 0
j = 1
k = 2

while k < 4000001:
	if k%2 == 0:
		even_numbers += k
		i = j
		j = k
		k += i
		
	else:
		i = j
		j = k
		k += i

print(even_numbers)