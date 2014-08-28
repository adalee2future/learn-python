# define function cost_of_MST
# input tuple list edges, num of vertices n, infinite number
# (which should be larger than any of of edge length)
# output overall cost of a minimum spanning tree
def cost_of_MST(edges, n, inf):
    cost = 0
    V = set(range(1, n + 1))
    X = set()
    X.add(1)
    T = set()
    while X != V:
        Xc = V - X
        min = inf
        for edge in edges:
            if (edge[0]in X and edge[1] in Xc) or (edge[1]in X and edge[0] in Xc):
                if edge[2] < min:
                    min = edge[2]
                    if edge[0] in Xc:
                        add_v = edge[0]
                    else:
                        add_v = edge[1]
        X.add(add_v)
        cost += min
    return cost

# import data
filename = 'edges.txt'
edges = []
with open(filename,'r') as f:
    for line in f:
        s = line.split()
        edge = (int(s[0]), int(s[1]), int(s[2]))
        edges.append(edge)
 
inf = 10000  # set inf to 10000
n = 500       
# call function cost_of_MST(edges, inf) 
print cost_of_MST(edges, n, inf) 

