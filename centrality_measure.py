import numpy as np

def it(a):
	temp = [x*x for x in a]
	denom = sum(temp) ** 0.5
	for i in range(len(a)):
		a[i] = round(a[i]/denom, 3)
	return a

def norma(a):
	return round(sum([x*x for x in a])**0.5, 2)

adj = ([0, 1, 0, 0, 0],
		[1, 0, 0, 1, 0],
		[0, 0, 0, 1, 1],
		[0, 1, 1, 0, 1],
		[0, 0, 1, 1, 0])
v = [1, 1, 1, 1, 1]
res = list(np.dot(adj, v))
#print(res)
print(norma(v))
print(it(res))