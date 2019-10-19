def gnirts(s):
	l = 0
	for i in s:
		l = l + 1
	for i in range(l):
		print(s[l-i-1],end=''),
	return 17
s = input()
if 17 == gnirts(s):
	print('\nAll good')
else:
	print('\nAll is bad')
