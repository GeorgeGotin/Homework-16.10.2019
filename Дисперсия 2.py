n = int(input())
j = []
for i in range(n):
    j.append(int(input()))
av = 0
av = sum(j)
av = av/n
ar = 0
for i in range(n):
	ar = ar + (j[i] - av)**2
ar=ar/n
print(ar)
