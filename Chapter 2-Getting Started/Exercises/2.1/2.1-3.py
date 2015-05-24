# Exercise 2.1-3, linear search.
def linear_search(a, key):
	n = len(a)
	for i in xrange(n):
		if a[i] == key:
			# Return the first match
			return i
	# Value not found
	return -1

def main():
	a = [31, 41, 59, 26, 41, 58]
	while True:
		key = int(raw_input().strip())
		print(linear_search(a, key))

if __name__ == '__main__':
	main()
