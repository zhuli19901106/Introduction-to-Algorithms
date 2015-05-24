# Exercise 2.1-2, modify the algorithm to sort in reverse order.
# The reversed insertion sort
def insertion_sort(a):
	n = len(a)
	for i in xrange(1, n):
		tmp = a[i]
		j = i - 1
		while j >= 0 and a[j] < tmp:
			a[j + 1] = a[j]
			j -= 1
		a[j + 1] = tmp
		print(a)

def main():
	a = [31, 41, 59, 26, 41, 58]
	insertion_sort(a)

if __name__ == '__main__':
	main()
