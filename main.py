import convert
import networkx as nx
import matplotlib.pyplot as plt


#Introduce
print("-------------------------------------Visualizing Graph with Python----------------------------")
run = True

while run:
    
    
    choice = input("                                         1: From adjacency list\n\
                                         2: From adjacency matrix\n\
                                         3: From adjacency edgelist\n\
Please enter a number:\n")
    
    
    
    #Get a edge list path
    edge_list_path = "./edgeList.txt"
    run = False
    if choice == '1': 
        convert.adjcencyList_to_edgeList("./AdjacencyList.txt")
        edge_list_path = "./output.txt"
    elif choice == '2' :
        convert.adjacencyMatrix_to_edgeList("./AdjacencyMatrix.txt")
        edge_list_path = "./output.txt"
    elif choice == '3':
        pass
    else :  
        runkey = input("Invalid input! Do you wanna try again?(y)")
        if runkey == 'y':
            run = True

    #Read edgelistpath to make a list of edge
    edge = []
    edge_list_file = open(edge_list_path)
    for line in edge_list_file :
        line = line.strip()
        if len(line) == 0 : continue
        From,To = map(int,line.split(" "))
        edge.append((From,To))
    
    
    v,e = edge[0][0],edge[0][1]
    print(f"The graph has {v} verticles and {e} edges")
    G = nx.Graph()
    G.add_edges_from(edge)
    nx.draw_planar(G,with_labels = True)
    plt.show() 