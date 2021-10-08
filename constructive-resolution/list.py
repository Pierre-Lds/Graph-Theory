import datetime

class graphList:
    def __init__(self, fileName):
        file = open(fileName, 'r')
        fLine = file.readline()
        self.nbVerticies = int(fLine.split()[0])
        self.nbEdges = int(fLine.split()[1])
        self.totalWeight = 0
        self.availableVerticies = list()
        self.choosenVerticies = list()
        self.list = list()
        for i in range(0, self.nbVerticies):
            self.availableVerticies.append(i+1)
            self.list.append([])
        lines = file.readlines()
        for line in lines:
            values = line.split()
            self.list[int(values[0])-1].append([int(values[1]), int(values[2])])
            self.list[int(values[1])-1].append([int(values[0]), int(values[2])])

def constructiveHeuristic_List(graph):
    # Get the starting vertex
    startingVertex = 0
    cptMax = 0
    for i in range(0, graph.nbVerticies):
        cpt = 0
        for j in range(0, len(graph.list[i])):
            if graph.list[i][j][1] != 0:
                cpt = cpt+1
        if cpt > cptMax:
            cptMax = cpt
            startingVertex = i+1
    graph.choosenVerticies.append(startingVertex)
    graph.availableVerticies.remove(startingVertex)
    # Delete all points which are not connected to this point
    list1 = list()
    for i in range(0, len(graph.list[startingVertex-1])):
        list1.append(graph.list[startingVertex-1][i][0])
    graph.availableVerticies = list(set(graph.availableVerticies)-set(set(graph.availableVerticies) - set(list1)))
    currentVertex = startingVertex
    # Algorithm
    while len(graph.availableVerticies) != 0:
        # Search the maximum weighted edge and the associated vertex
        maxWeight = 0
        vertex = 0
        for i in range(0, len(graph.list[currentVertex-1])):
            if (graph.list[currentVertex-1][i][1] > maxWeight) and (graph.list[currentVertex-1][i][0] in graph.availableVerticies):
                maxWeight = graph.list[currentVertex-1][i][1]
                vertex = graph.list[currentVertex-1][i][0]
        # Add the vertex to the final list
        currentVertex = vertex
        # Add the total weight
        for i in graph.choosenVerticies:
            for j in range(0, len(graph.list[currentVertex-1])):
                if i == graph.list[currentVertex-1][j][0]:

                    graph.totalWeight = graph.totalWeight + graph.list[currentVertex-1][j][1]
        graph.choosenVerticies.append(vertex)
        graph.availableVerticies.remove(vertex)
        # Delete all points which are not connected to this point
        list1 = list()
        for i in range(0, len(graph.list[currentVertex-1])):
            list1.append(graph.list[currentVertex-1][i][0])
        graph.availableVerticies = list(set(graph.availableVerticies)-set(set(graph.availableVerticies) - set(list1)))
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
            #print(">", myGraphList.list, "\n> Verticies:", myGraphList.nbVerticies, "| Edges:", myGraphList.nbEdges, "\n> Available Verticies:", myGraphList.availableVerticies, "| Choosen Verticies:", myGraphList.choosenVerticies)
            for k in range(0,3):
                # YOU CAN CHANGE HERE THE PATH
                myGraphList = graphList("../instances/"+inputFile+".in")
                # Algorithm (Matrix)
                start_time = datetime.datetime.now()
                myGraphList = constructiveHeuristic_List(myGraphList)
                end_time = datetime.datetime.now()
                timeArray[k] = (end_time-start_time)
                #print("["+str(i)+"_"+str(j)+"]"+str(end_time-start_time))
            # Write the output file
            f = open("outputs/" + inputFile + "_constructive.out", "w")
            f.write(str(len(myGraphList.choosenVerticies))+" "+str(myGraphList.totalWeight)+"\n")
            for l in range(0, len(myGraphList.choosenVerticies)):
                f.write(str(myGraphList.choosenVerticies[l])+" ")
            f.close()
            finalTime = (timeArray[0]+timeArray[1]+timeArray[2])/3
            print(">>> ["+str(i)+"_"+str(j)+"]"+str(finalTime))

main()
