# Exercise 2.1-4, adding two integers in their binary form.
import re

def convert_binary(a):
	a = map(int, list(a))
	a.reverse()
	return a

def add_binary(a, b):
	if len(a) > len(b):
		return add_binary(b, a)
	a.extend([0 for i in range(len(b) - len(a))])
	c = [0 for i in range(len(b) + 1)]
	carry = 0
	for i in range(len(b)):
		# Full adder
		c[i] = a[i] ^ b[i] ^ carry
		carry = (carry & (a[i] | b[i])) | (a[i] & b[i])
	c[i] = carry
	return c

def print_binary(a):
	a = map(str, a)
	while len(a) > 1 and a[-1] == '0':
		a.pop()
	a.reverse()
	print(''.join(a))

def main():
	#Sample Input:
	#10101 1101111
	#Sample Output:
	#1000100
	a, b = re.split('\s+', raw_input().strip())
	a = convert_binary(a)
	b = convert_binary(b)
	c = add_binary(a, b)
	print_binary(c)

if __name__ == '__main__':
	main()
