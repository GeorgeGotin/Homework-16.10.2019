def sum_of_max_and_min(a):
	max = a[0]
	min = a[0]
	for i in a:
		if a[i-1] < min: min = a[i-1]
		if a[i-1] > max: max = a[i-1]
	return min + max

n = int(input())
j = []
for i in range(n):
    j.append(int(input()))
print(sum_of_max_and_min(j))
