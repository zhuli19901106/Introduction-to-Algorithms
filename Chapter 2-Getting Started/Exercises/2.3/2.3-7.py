# Exercise 2.3-7 an algorithm that runs in O(n * lg(n)) time.
# Find out for a given sum, if there exists a pair in the given set, that add to this sum.
import re

def has_sum(a, sum):
	n = len(a)
	for i in xrange(n - 1):
		ll = i + 1
		rr = n - 1
		while ll <= rr:
			mm = (ll + rr) / 2
			if a[mm] < sum - a[i]:
				ll = mm + 1
			elif a[mm] > sum - a[i]:
				rr = mm - 1
			else:
				return True
	return False

def main():
	# Sample input:
	#1 34  2
	#35
	#34
	#3
	#4
	
	# Sample output:
	#True
	#False
	#True
	#False
	a = map(int, re.split('\s+', raw_input()))
	# Sort the array to enable binary search.
	a.sort()
	while True:
		sum = int(raw_input())
		print(has_sum(a, sum))

if __name__ == '__main__':
	main()
