import math
import sys

myprint = sys.stdout.write

def f1(x):
	return math.log(x) / math.log(2)

def f2(x):
	return math.sqrt(x)

def f3(x):
	return x

def f4(x):
	return x * f1(x)

def f5(x):
	return x ** 2
	
def f6(x):
	return x ** 3

def f7(x):
	return 2 ** x

def f8(x):
	return math.factorial(x)

def solve(f, t):
	if f == f7 or f == f8:
		i = 1
		while True:
			if f(i) >= t:
				i -= 1
				break
			i += 1
		return i
	ll = 1
	rr = 1 << 63
	while rr - ll > 1:
		mm = ll + (rr - ll) / 2
		if f(mm) < t:
			ll = mm
		else:
			rr = mm
	return ll

if __name__ == '__main__':
	a = [f1, f2, f3, f4, f5, f6, f7, f8]
	b = []
	b.append(10 ** 6)
	b.append(10 ** 6 * 60)
	b.append(10 ** 6 * 60 * 60)
	b.append(10 ** 6 * 60 * 60 * 24)
	b.append(10 ** 6 * 60 * 60 * 24 * 30)
	b.append(10 ** 6 * 60 * 60 * 24 * 365)
	b.append(10 ** 6 * 60 * 60 * 24 * 365 * 100)
	res = [[0 for j in xrange(len(b))] for i in xrange(len(a))]
	for i in xrange(1, len(a)):
		for j in xrange(len(b)):
			res[i][j] = solve(a[i], b[j])
	row = ['lg(n)', 'sqrt(n)', 'n', 'n * lg(n)', 'n ^ 2', 'n ^ 3', '2 ^ n', 'n!']
	col = ['second', 'minute', 'hour', 'day', 'month', 'year', 'century']
	myprint('%10s ' % ' ')
	print(' '.join(['%12s' % val for val in col]))
	for i in xrange(len(a)):
		myprint('%10s ' % row[i])
		print(' '.join(['%12e' % val for val in res[i]]))

	