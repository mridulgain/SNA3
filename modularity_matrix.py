import sys
import networkx as nx
def modularity_matrix(G):
    m = nx.linalg.modularitymatrix.modularity_matrix(G)
    print(m)
    print(type(m))
if __name__ == '__main__':
	try:
		G = nx.read_edgelist(sys.argv[1])
		modularity_matrix(G)
	except FileNotFoundError:
		print("Check the file name you entered")
	except IndexError:
		print("Enter input file name as command line argument")
		print("Usage : python graph_analysis.py file_name")
	except TypeError:
		print("You should enter your graph in EDGE LIST format")
