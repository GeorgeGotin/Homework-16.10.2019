n = int(input())
j = []
for i in range(n):
    j.append(int(input()))
for i in range(n):
	if j[i] < 25 and j[i] % 4 == 0:
		print(j[i])
