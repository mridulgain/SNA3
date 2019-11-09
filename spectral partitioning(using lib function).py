#Graph partitioning usig Fiedler vector 
#using library function

import networkx as nx
import numpy as np
import sys

def cutset(G, fv):
	edges = G.edges()
	#print(edges)
	c = sorted(range(len(fv)), key=lambda k: fv[k])
	c11 = set(i+1 for i in c[:16])#pick 1st 16
	#print(c11)
	c12 = set(j+1 for j in c[16:])# pick rest i.e 18
	c21 = set(j+1 for j in c[-16:])#pick last 16
	c22 = set(j+1 for j in c[:-16])#pick rest
	# minimize cut size
	cut_size_1 = 0
	cut_size_2 = 0
	for e in edges:
		u = int(e[0]) 
		v = int(e[1])
		if (u in c11 and v in c12) or (v in c11 and u in c12):
			cut_size_1 += 1
		if (u in c21 and v in c22) or (u in c22 and v in c21):
			cut_size_2 += 1
	#print(cut_size_1, cut_size_2)
	if cut_size_1 < cut_size_2:
		print("p1")
		return c11, c12
	else: 
		print("p2")
		return c21, c22		
#start
G = nx.read_edgelist(sys.argv[1])
fv = nx.linalg.algebraicconnectivity.fiedler_vector(G)
#print(fv)
c1, c2 = cutset(G, fv)
print(c1, c2)
#end
