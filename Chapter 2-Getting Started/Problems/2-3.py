# Exercise 2-3 Horner's Rule
# I don't feel like spending more time on the loop invariant.
# Just code.
import re

def poly1(a, x):
	y = 0
	n = len(a)
	# The O(n) solution, which is also the deviation-convergent one.
	for i in xrange(n - 1, -1, -1):
		y = y * x + a[i]
	return y

def poly2(a, x):
	y = 0
	n = len(a)
	# The O(n ^ 2) solution, which is also the deviation-divergent one.
	for i in xrange(n):
		t = a[i]
		for j in xrange(i):
			t *= x
		y += t
	return y

def main():
	a = map(int, re.split('\s+', raw_input()))
	x = int(raw_input())
	print(poly1(a, x))
	print(poly2(a, x))

if __name__ == '__main__':
	main()
