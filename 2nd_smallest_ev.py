#Graph partitioning usig Fiedler vector
import networkx as nx
import numpy as np
import sys

#start
G = nx.read_edgelist(sys.argv[1])
fv = nx.linalg.algebraicconnectivity.fiedler_vector(G)
#print(fv)
c = sorted(range(len(fv)), key=lambda k: fv[k])
print(c)
print(c[:16], c[16:])
print(G.nodes())
cutval, partition = nx.algorithms.flow.minimum_cut(G, '1', '34')
print(cutval, partition)