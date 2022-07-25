import re #To unpack potential_matrix
import networkx as nx
from pyvis.network import Network
import random

def graph_gen(potential_matrix, start):
    graph = nx.DiGraph()
    
    dest = [0,0]
    for i in range(len(potential_matrix)):
        for j in range(len(potential_matrix[i])):
            if potential_matrix[i][j] > potential_matrix[dest[0]][dest[1]]:
                dest = [i,j]
    print("dest = ", dest)
    
    def N_loop(graph, TRAV, ct):     
        N = []  #List of neighbour of Q
        Ns = []
        Q = [TRAV[ct]]
        
        x = Q[0][0]  #x co-ord of node
        y = Q[0][1]  #y co-ord of node
        
    #For edge nodes of matrix neighbour node calc.
        if ((x == 0) | (x == len(potential_matrix)-1) | (y == 0) | (y == len(potential_matrix)-1)):
            #Adjacent neighbours
            if x != 0:
                Ns.append([x-1,y])  
            if y != 0:
                Ns.append([x,y-1])
            if x != len(potential_matrix)-1:
                Ns.append([x+1,y])
            if y != len(potential_matrix)-1:
                Ns.append([x,y+1])
                
            #Diagonal neighbours
            if  (x != 0 and y != 0):
                N.append([x-1,y-1])
            if  (x != 0 and y != len(potential_matrix)-1):
                N.append([x-1,y+1])
            if  (x != len(potential_matrix)-1 and y != 0):
                N.append([x+1,y-1])
            if  (x != len(potential_matrix)-1 and y != len(potential_matrix)-1):
                N.append([x+1,y+1])
                
        #For inner nodes of matrix neighbour node calc.
        else:
           #Adjacent neighbours
           Ns.append([x-1,y])
           Ns.append([x,y-1])
           Ns.append([x+1,y])
           Ns.append([x,y+1])
           
           #Diagonal neighbours
           N.append([x-1,y-1])
           N.append([x-1,y+1])
           N.append([x+1,y-1])
           N.append([x+1,y+1])
        
        #print("Neighbours found: ")   
        #print("N = ", N)
        #print("TRAV = ", TRAV)
        t = 0
        root = str(x) + " " + str(y)
        for i in N:
            if potential_matrix[i[0]][i[1]] > potential_matrix[x][y]:
                TRAV.append(i)
                leaf = str(i[0]) + " " + str(i[1])
                #print(root + " " + leaf)
                graph.add_edge(root, leaf)
                t+=1
                
        #print(t)
        if t == 0:
            for i in Ns:
                if potential_matrix[i[0]][i[1]] > potential_matrix[x][y]:
                    TRAV.append(i)
                    leaf = str(i[0]) + " " + str(i[1])
                    #print(root + " " + leaf)
                    graph.add_edge(root, leaf)
        
        TRAV1 = []
        for t in TRAV:
            if t not in TRAV1:
                TRAV1.append(t)
        
        N.clear()
        Q.clear()
        return [graph, TRAV1]
    
    TRAV = [start]
    ct = 0
    while len(TRAV) > ct:
        LST = N_loop(graph, TRAV, ct)
        ct += 1
        graph = LST[0]
        #TRAV.clear()
        TRAV = LST[1]
    return graph

#Main Function
potential_matrix = []
with open('map_out.txt') as f:
    rows = f.readlines()
    for row in rows:
        potential_matrix.append([int(i) for i in re.findall(r'-?\d+\b',row)])

'''print("Potential Matrix = ")
for i in potential_matrix:
    print(i)'''

#Start node input    
'''s = input("Enter start as i,j: ")
start = s.split(",")
start[0] = int(start[0])
start[1] = int(start[1])'''
start = [0, 0]
print("start = ", start)

#Call function to generate graph
graph = nx.DiGraph()
graph = graph_gen(potential_matrix, start)
net = Network(notebook = True)
net.from_nx(graph)
net.show("graph.html")

if (nx.is_empty(graph))==False:
    dest = [0,0]
    for i in range(len(potential_matrix)):
        for j in range(len(potential_matrix[i])):
            if potential_matrix[i][j] > potential_matrix[dest[0]][dest[1]]:
                dest = [i,j]
        
    #generate paths from graph with no duplicates        
    pts = []
    Paths = []
    for path in nx.all_simple_paths(graph, source=str(str(start[0]) + " " + str(start[1])), target=str(str(dest[0]) + " " + str(dest[1]))):
        #print(path)
        pts.append(path)
        
    ct = 0    
    for pth in pts:
        Paths.append([])
        for node in pth:
            nds = [int(nd) for nd in node.split() if nd.isdigit()]
            Paths[ct].append(nds)
        ct += 1
        
    if len(Paths) != 0:
        #print(Paths)
        #Write all generated paths in file
        with open('paths.txt', 'w') as f:
            for x in Paths:
                f.write(str(x))
                f.write("\n")
            print("Paths generated!!!")
            print("Number of paths: ", len(Paths))
            print("Nodes in paths: ", len(Paths[0]))
    else:
        print("*** Error Paths not Found ***")
else:
    print("*** Error Paths not Found ***")