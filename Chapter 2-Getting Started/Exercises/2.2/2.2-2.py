import re

def selection_sort(a):
    n = len(a)
    for i in xrange(n - 1):
        mi = i
        for j in xrange(i + 1, n):
            if a[j] < a[mi]:
                mi = j
        a[i], a[mi] = a[mi], a[i]

def main():
    a = [31, 64, 12, 8, 4532, 22, 13, 31]
    print(' '.join(map(str, a)))
    selection_sort(a)
    print(' '.join(map(str, a)))

if __name__ == '__main__':
    main()
