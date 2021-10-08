import datetime

from Exact.Source.Graph import Graph
# from art import *


def main():
    for elem in [25]:
        for k in range(5, 506, 5):
            resolveGraph("../Instances/input_x_" + str(elem) + "/", k, elem)
    for elem in [50]:
        for k in range(5, 251, 5):
            resolveGraph("../Instances/input_x_" + str(elem) + "/", k, elem)
    for elem in [75]:
        for k in range(5, 91, 5):
            resolveGraph("../Instances/input_x_" + str(elem) + "/", k, elem)
    for elem in [100]:
        for k in range(5, 25, 1):
            resolveGraph("../Instances/input_x_" + str(elem) + "/", k, elem)


def mainFast():
    for elem in [25]:
        for k in range(5, 101, 5):
            resolveGraph("../Instances/input_x_" + str(elem) + "/", k, elem)
    for elem in [50]:
        for k in range(5, 81, 5):
            resolveGraph("../Instances/input_x_" + str(elem) + "/", k, elem)
    for elem in [75]:
        for k in range(5, 41, 5):
            resolveGraph("../Instances/input_x_" + str(elem) + "/", k, elem)
    for elem in [100]:
        for k in range(5, 16, 1):
            resolveGraph("../Instances/input_x_" + str(elem) + "/", k, elem)


def resolveGraph(pathGraph, vertices, purcentage):
    myGraph = Graph(pathGraph + str(vertices) + "_" + str(purcentage) + ".in")

    start_time = datetime.datetime.now()
    myGraph.findCliques(-1, 0)
    # print("Temps d'execution : " + str(datetime.datetime.now() - start_time))
    saveTime(vertices, purcentage, datetime.datetime.now() - start_time)
    myGraph.writeInFile("Instances/output_x_" + str(purcentage))


def saveTime(n, m, time):
    f = open("../Instances/times/time_x_" + str(m) + ".csv", "a")
    f.write(str(n) + "," + str(time.total_seconds() * 1000) + "\n")


def execOneFile():
    input_file = "50_75"
    # tprint("Exact")

    myGraph = Graph("../Instances/input/" + input_file + ".in")
    start_time = datetime.datetime.now()
    myGraph.findCliques(-1, 0)
    print("Temps d'execution : " + str(datetime.datetime.now() - start_time))
    myGraph.printMaxClique()
    myGraph.writeInFile("Instances/input")


# main()
mainFast()
