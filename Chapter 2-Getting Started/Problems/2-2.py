# Exercise 2-2
# a. Answer:
# We also need to prove that A and A' contains the same set of elements.
# d. Answer:
# In the worst case number of comparisons and swaps are both O(n^2), same as insertion sort.
import re

def bubble_sort(a):
	n = len(a)
	for i in xrange(n - 1):
		for j in xrange(n - 1, i, -1):
			if a[j - 1] > a[j]:
				a[j - 1], a[j] = a[j], a[j - 1]

def main():
	a = map(int, re.split('\s+', raw_input()))
	print(' '.join(map(str, a)))
	bubble_sort(a)
	print(' '.join(map(str, a)))

if __name__ == '__main__':
	main()
