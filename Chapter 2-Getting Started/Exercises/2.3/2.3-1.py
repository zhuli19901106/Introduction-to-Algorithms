# Exercise 2.3-1 merge sort
import re

def merge(a, ll, mm, rr):
	b = []
	i = ll
	j = mm + 1
	while i <= mm and j <= rr:
		if a[i] < a[j]:
			b.append(a[i])
			i += 1
		else:
			b.append(a[j])
			j += 1
	while i <= mm:
		b.append(a[i])
		i += 1
	while j <= rr:
		b.append(a[j])
		j += 1
	a[ll: rr + 1] = b[:]

def msort(a, ll, rr):
	if ll == rr:
		return
	mm = (ll + rr) / 2
	msort(a, ll, mm)
	msort(a, mm + 1, rr)
	merge(a, ll, mm, rr)
	# Show the result after every recursion.
	print(' '.join(map(str, a[: ll]))),
	print('{' + (' '.join(map(str, a[ll: rr + 1]))) + '}'),
	print(' '.join(map(str, a[rr + 1: ])))
	

def merge_sort(a):
	msort(a, 0, len(a) - 1)

def main():
	a = [3, 41, 52, 26, 38, 57, 9, 49]
	print(a)
	merge_sort(a)
	print(a)

if __name__ == '__main__':
	main()
