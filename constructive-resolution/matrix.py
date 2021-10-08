import datetime

class graphMatrix:
    def __init__(self, fileName):
        file = open(fileName, 'r')
        fLine = file.readline()
        self.nbVerticies = int(fLine.split()[0])
        self.nbEdges = int(fLine.split()[1])
        self.totalWeight = 0
        self.availableVerticies = list()
        self.choosenVerticies = list()
        for i in range(0, self.nbVerticies):
            self.availableVerticies.append(i+1)
        self.matrix = [[0]*self.nbVerticies for i in range(0, self.nbVerticies)]
        lines = file.readlines()
        for line in lines:
            values = line.split()
            self.matrix[int(values[0])-1][int(values[1])-1] = int(values[2])
            self.matrix[int(values[1])-1][int(values[0])-1] = int(values[2])
        file.close()

def constructiveHeuristic_Matrix(graph):
    # Get the starting vertex
    startingVertex = 0
    cptMax = 0
    for i in range(0, graph.nbVerticies):
        cpt = 0
        for j in range(0, graph.nbVerticies):
            if graph.matrix[i][j] != 0:
                cpt = cpt+1
        if cpt > cptMax:
            cptMax = cpt
            startingVertex = i+1
    graph.choosenVerticies.append(startingVertex)
    graph.availableVerticies.remove(startingVertex)
    # Delete all points wich are not connected to this point
    for i in range(0, graph.nbVerticies):
        if (graph.matrix[startingVertex-1][i] == 0) and (i+1 in graph.availableVerticies):
            graph.availableVerticies.remove(i+1)
    currentVertex = startingVertex
    # Algorithm
    while len(graph.availableVerticies) != 0:
        # Search the maximum weighted edge and the associated vertex
        maxWeight = 0
        vertex = 0
        for i in graph.availableVerticies:
            if graph.matrix[currentVertex-1][i-1] > maxWeight:
                maxWeight = graph.matrix[currentVertex-1][i-1]
                vertex = i
        # Add the vertex to the final list
        currentVertex = vertex
        for i in graph.choosenVerticies:
            graph.totalWeight = graph.totalWeight + graph.matrix[currentVertex-1][i-1]
        graph.choosenVerticies.append(vertex)
        graph.availableVerticies.remove(vertex)
        # Delete all points wich are not connected to this point
        for i in range(0, graph.nbVerticies):
            if (graph.matrix[currentVertex-1][i] == 0) and (i+1 in graph.availableVerticies):
                graph.availableVerticies.remove(i+1)
    return graph

def main():
    # YOU CAN CHANGE HERE THE VALUES OF THE INPUT FILE
    listI = [100,200,300]
    for i in listI:
        # YOU CAN CHANGE HERE THE VALUES OF THE INPUT FILE
        listJ = [25,50,75,100]
        for j in listJ:
            timeArray = [0,0,0]
            # Object creation
            inputFile = str(i)+"_"+str(j)
            for k in range(0,3):
                # YOU CAN CHANGE HERE THE PATH
                myGraphMatrix = graphMatrix("../instances/"+inputFile+".in")
                #print(">", myGraphMatrix.matrix, "\n> Verticies:", myGraphMatrix.nbVerticies, "| Edges:", myGraphMatrix.nbEdges, "\n> Available Verticies:", myGraphMatrix.availableVerticies, "| Choosen Verticies:", myGraphMatrix.choosenVerticies)
                # Algorithm (Matrix)
                start_time = datetime.datetime.now()
                myGraphMatrix = constructiveHeuristic_Matrix(myGraphMatrix)
                end_time = datetime.datetime.now()
                timeArray[k] = (end_time-start_time)
            # Write the output file
            f = open("outputs/" + inputFile + "_constructive.out", "w")
            f.write(str(len(myGraphMatrix.choosenVerticies))+" "+str(myGraphMatrix.totalWeight)+"\n")
            for l in range(0, len(myGraphMatrix.choosenVerticies)):
                f.write(str(myGraphMatrix.choosenVerticies[l])+" ")
            f.close()
            finalTime = (timeArray[0]+timeArray[1]+timeArray[2])/3
            print(">>> ["+str(i)+"_"+str(j)+"]"+str(finalTime))

main()
