#Implementation of some common vector operations
#that are needed in both algorithms
import networkx as nx
import numpy as np

def unit_vector(v):
    #unit vector computation
    v = v.getA1()#handling type mismatch
    temp = [x*x for x in v]
    #print(temp)
    denom = sum(temp) ** 0.5
    unit_vec = []
    for i in range(len(v)):
        unit_vec.append(round(v[i]/denom, 5))
    unit_vec = np.matrix(unit_vec).getT()
    return unit_vec

def normalized(a):
    #returns magnitude
    a = a.getA1()# type compatibility
    return round(sum([x*x for x in a])**0.5, 5)

def leading_eigen_vector(adjacency_matrix):
    #leading eigen vector computation using power method
    order = adjacency_matrix.shape[0]
    #initial vector with all +ve components
    eigen_vector = [3, 2] * (order // 2)
    eigen_vector += [1] * (order % 2)
    eigen_vector = np.matrix(eigen_vector).getT()#34x1 matrix
    result = np.dot(adjacency_matrix, eigen_vector)
    normalized_val = normalized(result)
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

def eigenVec_2nd_smallest_eigenVal(lev, l_mat):
    #calculates eigen vector corresponding to 2nd smallest eigen value of a matrix
    order = lev.shape[0]
    #initial vector with all +ve components
    x = [1, 2] * (order//2)
    x += [3] * (order % 2)
    x = np.matrix(x).getT()#creating 34x1 vector
    c = float(np.dot(lev.getT(), x))
    y = x - c * lev
    it = 500
    while(it > 0):
        y = np.dot(l_mat.getT(), y)
        if it % 10 == 0:
        #removing component of largest ev from y periodically       
            c = float(np.dot(lev.getT(), y))
            y = y - c * lev
        it -= 1
        y = unit_vector(y)
    return y

def get_partition(G, fv):
    #partitioning based on minimum cut size
    edges = G.edges()
    #sorting the vertices based on components of fiedler vector
    c = sorted(range(len(fv)), key=lambda k: fv[k])
    #partition 1
    c11 = set(i+1 for i in c[:16])#pick 1st 16
    c12 = set(j+1 for j in c[16:])# pick rest i.e 18
    #partition 2
    c21 = set(j+1 for j in c[-16:])#pick last 16
    c22 = set(j+1 for j in c[:-16])#pick rest
    # minimize cut size
    cut_size_1 = 0
    cut_size_2 = 0
    for e in edges:
        u = int(e[0]) 
        v = int(e[1])
        if (u in c11 and v in c12) or (u in c12 and v in c11):
            cut_size_1 += 1
        if (u in c21 and v in c22) or (u in c22 and v in c21):
            cut_size_2 += 1
    #return partition with min cut size
    if cut_size_1 < cut_size_2:
        return c11, c12
    else: 
        return c21, c22