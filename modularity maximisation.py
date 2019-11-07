#Community discovery by Modularity Maximization
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


if __name__ == '__main__':
	try:
		G = nx.read_edgelist(sys.argv[1])
		#Community discovery by Modularity Maximization
		m = nx.linalg.modularitymatrix.modularity_matrix(G)
		no_of_vertices = m.shape[0]
		lev = leading_eigen_vector(m).getA1()
		c1 = set()
		c2 = set()
		for i in range(no_of_vertices):
			if lev[i] < 0:
				c2.add(i+1)
			else:
				c1.add(i+1)
		print("Community discovery by Modularity Maximization ---- ")
		print("Community 1 :", c1)
		print("Community 2 :", c2)
		print("Size : ",len(c1), len(c2), "respectively")
		#Graph partitioning usig Fiedler vector
		fv = nx.linalg.algebraicconnectivity.fiedler_vector(G)
		c = sorted(range(len(fv)), key=lambda k: fv[k])
		#Since this is a prititioning problem, we must specify partition sizes
		c11 = set(i+1 for i in c[:16])
		c12 = set(j+1 for j in c[16:])
		print("Spectral partitioning (2 partition of size 16 & 18 respectively) using Fiedler vector -----")
		print("Community 1 : ", c11)
		print("Community 2 : ", c12)


	except FileNotFoundError:
		print("Check the file name you entered")
	except IndexError:
		print("Enter input file name as command line argument")
		print("Usage : python leading_eigen_vector.py <file_name>")
	except TypeError:
		print("You should enter your graph in EDGE LIST format")
