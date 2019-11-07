#Graph partitioning by modularity maximisation
import networkx as nx
import numpy as np
import sys

def unit_vector(v):
	v = v.getA1()#handling type mismatch
	temp = [x*x for x in v]
	#print(temp)
	denom = sum(temp) ** 0.5
	#print(denom)
	unit_vec = []
	for i in range(len(v)):
		unit_vec.append(round(v[i]/denom, 5))
	unit_vec = np.matrix(unit_vec).getT()
	return unit_vec

def normalized(a):
	a = a.getA1()# type compatibility
	return round(sum([x*x for x in a])**0.5, 5)

def leading_eigen_vector(adjacency_matrix):
	order = adjacency_matrix.shape[0]
	#initial vector with all +ve components
	eigen_vector = [3, 2] * (order // 2)
	eigen_vector += [1] * (order % 2)
	eigen_vector = np.matrix(eigen_vector).getT()#34x1 matrix
	result = np.dot(adjacency_matrix, eigen_vector)
	#print(result)#ok
	normalized_val = normalized(result)
	#print(normalized_val)#ok
	while(True):
		eigen_vector = unit_vector(result)
		#print(eigen_vector)#ok
		result = np.dot(adjacency_matrix, eigen_vector)
		current_normalized_val = normalized(result)
		if normalized_val - current_normalized_val == 0:
			break
		normalized_val = current_normalized_val
		#print(normalized_val)
	return eigen_vector

def eigenVec_2nd_smallest_eval(lev, l_mat):
	order = lev.shape[0]
	#initial vector with all +ve components
	x = [3,4] * (order//2)
	x += [1] * (order % 2)
	x = np.matrix(x).getT()#34x1
	c = float(np.dot(lev.getT(), x))
	y = x - c * lev
	it = 100
	while(it > 0):
		y = np.dot(l_mat.getT(), y)		
		if it % 10 == 0:
			c = float(np.dot(lev.getT(), y))
			y = y - c * lev
		it -= 1
		y = unit_vector(y)
	return y



if __name__ == '__main__':
	try:
		G = nx.read_edgelist(sys.argv[1])
		#Community discovery by Modularity Maximization
		m = nx.linalg.laplacianmatrix.laplacian_matrix(G).todense()
		lev = leading_eigen_vector(m)
		#print(lev)
		fv = eigenVec_2nd_smallest_eval(lev, m)
		c = sorted(range(len(fv)), key=lambda k: fv[k])
		c11 = set(i+1 for i in c[:16])
		c12 = set(j+1 for j in c[16:])
		print("Spectral partitioning (2 partition of size 16 & 18 respectively) using Fiedler vector -----")
		print("Community 1 : ", c11)
		print("Community 2 : ", c12)
		#Graph partitioning usig Fiedler vector
		fv = nx.linalg.algebraicconnectivity.fiedler_vector(G)
		print(fv)
		c = sorted(range(len(fv)), key=lambda k: fv[k])
		#Since this is a prititioning problem, we must specify partition sizes
		c21 = set(i+1 for i in c[:16])
		c22 = set(j+1 for j in c[16:])
		print("Spectral partitioning (2 partition of size 16 & 18 respectively) using Fiedler vector -----")
		print("Community 1 : ", c21)
		print("Community 2 : ", c22)


	except FileNotFoundError:
		print("Check the file name you entered")
	except IndexError:
		print("Enter input file name as command line argument")
		print("Usage : python leading_eigen_vector.py <file_name>")
	except TypeError:
		print("You should enter your graph in EDGE LIST format")