import math

def log2(x):
	return math.log(x) / math.log(2.0)

def f(x):
	return x / log2(x)
	
if __name__ == '__main__':
	for i in xrange(32, 65):
		if f(i) >= 8:
			break
	print(i)
#44