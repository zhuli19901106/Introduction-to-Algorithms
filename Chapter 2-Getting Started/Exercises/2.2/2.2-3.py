def linear_search(a, key):
	n = len(a)
	for i in xrange(n):
		if a[i] == key:
			return i
	return -1
