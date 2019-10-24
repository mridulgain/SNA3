import numpy as np
def unit_vector(v):
	temp = [x*x for x in v]
	denom = sum(temp) ** 0.5
	for i in range(len(v)):
		v[i] = round(v[i]/denom, 3)
	return v

def normalized(a):
	return round(sum([x*x for x in a])**0.5, 2)

def leading_eigen_vector(adjacency_matrix):
	order = 6
	eigen_vector = [1] * order
	result = np.dot(adjacency_matrix, eigen_vector)
	normalized_val = normalized(result)
	while(True):
		eigen_vector = unit_vector(list(result))
		result = np.dot(adjacency_matrix, eigen_vector)
		current_normalized_val = normalized(result)
		if normalized_val - current_normalized_val == 0:
			break
		normalized_val = current_normalized_val
		print(normalized_val)

	return eigen_vector

adj = ([0, 1, 0, 0, 0],
		[1, 0, 0, 1, 0],
		[0, 0, 0, 1, 1],
		[0, 1, 1, 0, 1],
		[0, 0, 1, 1, 0])
adj2 = ([0,1,1,1,0,0,0,0],
		[1,0,1,0,0,0,0,0],
		[1,1,0,1,0,0,0,0],
		[1,0,1,0,1,0,0,0],
		[0,0,0,1,0,1,0,0],
		[0,0,0,0,1,0,1,1],
		[0,0,0,0,0,1,0,1],
		[0,0,0,0,0,1,1,0])
adj3 = ([0,1,1,0,0,0],
		[1,0,1,0,0,0],
		[1,1,0,1,0,0],
		[0,0,1,0,1,1],
		[0,0,0,1,0,1],
		[0,0,0,1,1,0])
print(leading_eigen_vector(adj3))
