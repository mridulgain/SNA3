#Community discovery by Modularity Maximization
import networkx as nx
import numpy as np
import sys
from my_implementation import unit_vector
from my_implementation import normalized
from my_implementation import leading_eigen_vector

if __name__ == '__main__':
	try:
		G = nx.read_edgelist(sys.argv[1])
		#Community discovery by Modularity Maximization
		m = nx.linalg.modularitymatrix.modularity_matrix(G)
		no_of_vertices = m.shape[0]
		lev = leading_eigen_vector(m).getA1()
		c1 = set()
		c2 = set()
		# assigning community based on sign
		for i in range(no_of_vertices):
			if lev[i] < 0:
				c2.add(i+1)
			else:
				c1.add(i+1)
		print("Community discovery by Modularity Maximization ---- ")
		print("Community 1 :", c1)
		print("Community 2 :", c2)
		print("Size : ",len(c1), len(c2), "respectively")

	except FileNotFoundError:
		print("Check the file name you entered")
	except IndexError:
		print("Enter input file name as command line argument")
		print("Usage : python leading_eigen_vector.py <file_name>")
	except TypeError:
		print("You should enter your graph in EDGE LIST format")
