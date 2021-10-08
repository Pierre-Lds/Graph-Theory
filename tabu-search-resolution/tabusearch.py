import datetime
import time

from GraphTabu import GraphTabu
#from art import *

#------------------------------------------------------------------------------
def stoppingCondition(graph, iteration, timer_stop):

    timer1 = int(time.time())
    timer2 = int(graph.global_timer)
    stop_time = timer1 - timer2
    if (graph.global_compteur_localsearch > iteration or stop_time > timer_stop): #the stopping conditions are reached
        return 1
    else:
        return 0


def fitness(var, graph): # Var have all verticies of the clique and graph is the graph basically
    size = len(var)
    sum = 0
    for i in range(size):
        for j in range(i+1, size):
            sum += graph.graph[var[i]][var[j]]

    return sum


def getNeighbors2(Candidate, graph):
    neighboor = []
    for element in Candidate:
        for i in range(len(graph.graph[0])):
            if graph.graph[element][i] != 0 and (not (i in Candidate)) and (not (i in neighboor)):
                neighboor.append(i)

    clique = []
    taille = []
    node, weight = graph.maxWeightNode2(neighboor)
    test1, test2 = graph.realLocalSearch(node)
    clique.append(test1)
    taille.append(test2)#local_search

    return clique, taille

def tabuSearch(iteration, graph, maxTabuSize, timer_stop):
    #We initialise the variables with the initial solution
    node, weight = graph.maxWeightNode()
    s0,poid_sBest = graph.realLocalSearch(node)
    sBest = s0
    bestCandidate = s0
    #We create a list which will contain the best and recent solutions
    #Then we put the first solution (initial solution) in the list
    tabuList = []
    tabuList.append(s0)

    #We begin a loop which will find the optimal solution
    #The loop stops when the number of iteration or execution time is so important
    while stoppingCondition(graph, iteration , timer_stop) != 1:
        #We get in an array all neighbor cliques of the current best solution
        #The new current best solution become the first variable of this array
        sNeighborhood, taille = getNeighbors2(bestCandidate, graph)
        bestCandidate =  sNeighborhood[0]
        #print("taille retournee par get neighbors2 : " + str(taille[bestCandidate]))
        compteur = 0
        current_candidate = 0


        #For each clique of the array, we study if it can be a best solution that the                                                                                            current best solution
        #Then we put the current best solution in the list, if the list is highter than the size maximum we remove the old solution saved
        for sCandidate in sNeighborhood:
            if (not (sCandidate in tabuList)) and (taille[compteur] > taille[current_candidate]):
                current_candidate = compteur
                bestCandidate = sCandidate
            compteur += 1

        if taille[current_candidate] > poid_sBest:
            sBest = bestCandidate
            poid_sBest = taille[current_candidate]
            graph.global_compteur_localsearch = 0
        else:
            graph.global_compteur_localsearch += 1

        #If the current best solution is better than the best solution of the graph, it becomes the best solution
        tabuList.append(bestCandidate)
        if len(tabuList) > maxTabuSize:
            tabuList.pop(0)

        #We return the best solution
    return sBest, poid_sBest

def saveTime(n, m, time):
    f = open("../instances/times/tabuSearch/time_x_" + str(m) + ".csv", "a")
    f.write(str(n) + ";" + str(time) + "\n")

def saveWeights(n, m, weight):
    f = open("../instances/weights/tabuSearch/weights_x_" + str(m) + ".csv", "a")
    f.write(str(n) + ";" + str(weight) + "\n")

def main():
    #tprint("Tabu_search")
    for elem in [25]:   #elem is the percentage of edges
        for k in range (5, 21, 5):  #k is the number of vertices  + in range(begin include, end exclude, pas), WARNING : if the input don't exists, we have an error
            bob = GraphTabu("../instances/input_x_" + str(elem)+ "/" + str(k) + "_" + str(elem)+ ".in")
            start_time = datetime.datetime.now()
            bob.global_timer = time.time()
            limite_timer_max = 1800
            taille_tabulist_max = 10
            tabu_search_best_clique, poid_best_clique = tabuSearch(5, bob , taille_tabulist_max, limite_timer_max) #Tab
            print(str(k) + "_" + str(elem)+ ".in")
            print("Weight : " + str(poid_best_clique))
            vrai_time = str((datetime.datetime.now() - start_time).total_seconds())
            print("Execution time : " + vrai_time + "\n")

            ## Write the result in files

            # f = open("../instances/tabuSearch_x_" + str(elem)+ "/" + str(k) + "_" + str(elem)+ "_tabuSearch.out", "w")
            # f.write(str(len(tabu_search_best_clique)) + " " + str(poid_best_clique) + '\n')
            # for i in range(len(tabu_search_best_clique)):
            #     f.write(str(tabu_search_best_clique[i] + 1) + ' ')
            # f.close()
            #saveTime(k, elem, vrai_time)
            #saveWeights(k, elem, poid_best_clique)

main()
# ~~ SkY
