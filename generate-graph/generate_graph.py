# from generate_graphes import Graph
# import secrets # It's useless (like you)
# from generate_graphes.graph import Graph
from graph import Graph

def main():
    vals = [18000]
    for j in vals :
        val = [50]
        for i in val :
            # EDIT HERE TO GENERATE DIFFERENT GRAPHES
            nb_of_vertex = j
            purcentage_of_edges = i  # Between [1;100]
            # Do not edit this part
            isConnex = False  # Var we use in the loop -> While we generate non connex graph, we regenerate
            graph = Graph(nb_of_vertex, purcentage_of_edges)  # Create object graph
            while not isConnex:
                graph.fillGraph(nb_of_vertex, purcentage_of_edges)  # Generate the graph
                isConnex = graph.isConnex(0)  # 0 use BFS | 1 use DFS (DFS = max ~ 990 vertices)
                if not isConnex:  # Friendly message in console to tell we regenerate
                    graph.resetGraph()
                    print("DEBUG : Fuck that's not connex, let me try again bro")  # Testing/Debug
            graph.userGraphGenerated()  # Tell user graph is generated (part 1 done)
            graph.writeInFile()  # Generate the file of the graph we generated
            graph.userFinished()  # Tell user file is created


main()
