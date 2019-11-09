#Graph partitioning by modularity maximisation
import networkx as nx
import numpy as np
import sys
from my_implementation import unit_vector
from my_implementation import normalized
from my_implementation import leading_eigen_vector
from my_implementation import eigenVec_2nd_smallest_eigenVal
from my_implementation import get_partition

if __name__ == '__main__':
	try:
		G = nx.read_edgelist(sys.argv[1])
		L = nx.linalg.laplacianmatrix.laplacian_matrix(G).todense()
		n = G.number_of_nodes()
		k_max = max(G.degree())[1]#max degree 
		I = np.matrix(np.identity(n))
		m = (2 * k_max * I) - L
		lev = leading_eigen_vector(m)
		fv = eigenVec_2nd_smallest_eigenVal(lev, m)
		#print(fv)
		c1, c2 = get_partition(G, fv)
		print("Spectral partitioning using Fiedler vector -----")
		print("\n......Own implementation.......")
		print("Community 1 : ", c1)
		print("Community 2 : ", c2)
		print("Size : ",len(c1), " and ", len(c2), "respectively")
		#same thing using library function
		fv2 = nx.linalg.algebraicconnectivity.fiedler_vector(G)
		#print(fv2)
		c11, c12 = get_partition(G, fv2)
		print("\n......using library function....")
		print("Community 1 : ", c11)
		print("Community 2 : ", c12)
		print("Size : ",len(c11), " and ", len(c12), "respectively")

	except FileNotFoundError:
		print("Check the file name you entered")
	except IndexError:
		print("Enter input file name as command line argument")
		print("Usage : python leading_eigen_vector.py <file_name>")
	except TypeError:
		print("You should enter your graph in EDGE LIST format")