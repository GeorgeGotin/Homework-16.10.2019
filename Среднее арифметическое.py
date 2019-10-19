n = int(input())
j = []
for i in range(n):
    j.append(int(input()))
av = 0
for i in range(n):
	av = av + j[i]
av=av/n
print(av)
