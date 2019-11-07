import networkx as nx
import numpy as np
import sys

def unit_vector(v):
	temp = [x*x for x in v]
	#print(temp)
	denom = sum(temp) ** 0.5
	#print(denom)
	unit_vec = []
	for i in range(len(v)):
		unit_vec.append(round(v[i]/denom, 6))
	unit_vec = np.matrix(unit_vec).getT()
	return unit_vec

def normalized(a):
	return round(sum([x*x for x in a])**0.5, 5)

def leading_eigen_vector(adjacency_matrix):
	order = adjacency_matrix.shape[0]
	eigen_vector = [1] * order
	eigen_vector = np.matrix(eigen_vector).getT()
	result = np.dot(adjacency_matrix, eigen_vector)
	#print(result)#ok
	normalized_val = normalized(result.getA1())
	#print(normalized_val)#ok
	while(True):
		eigen_vector = unit_vector(result.getA1())
		#print(eigen_vector)#ok
		result = np.dot(adjacency_matrix, eigen_vector)
		current_normalized_val = normalized(result.getA1())
		if normalized_val - current_normalized_val == 0:
			break
		normalized_val = current_normalized_val
		#print(normalized_val)

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

G = nx.read_edgelist(sys.argv[1])
m = nx.linalg.modularitymatrix.modularity_matrix(G)
#m = np.matrix(adj3)
no_of_vertices = m.shape[0]
lev = leading_eigen_vector(m).getA1()
#print(lev)
c1 = []
c2 = []
for i in range(no_of_vertices):
	if lev[i] < 0:
		c2.append(i+1)
	else:
		c1.append(i+1)
print(c1, c2)
