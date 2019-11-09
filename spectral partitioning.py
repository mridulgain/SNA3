#Graph partitioning by modularity maximisation
import networkx as nx
import numpy as np
import sys
from common_helping_func import unit_vector
from common_helping_func import normalized
from common_helping_func import leading_eigen_vector
from common_helping_func import eigenVec_2nd_smallest_eigenVal
from common_helping_func import get_partition

if __name__ == '__main__':
	try:
		G = nx.read_edgelist(sys.argv[1])
		m = nx.linalg.laplacianmatrix.laplacian_matrix(G).todense()
		lev = leading_eigen_vector(m)
		fv = eigenVec_2nd_smallest_eigenVal(lev, m)
		c1, c2 = get_partition(G, fv)
		#input()
		print("Spectral partitioning using Fiedler vector -----")
		print("\n......Own implementation.......")
		print("Community 1 : ", c1)
		print("Community 2 : ", c2)
		print("Size : ",len(c1), " and ", len(c2), "respectively")
		#using library function
		fv2 = nx.linalg.algebraicconnectivity.fiedler_vector(G)
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