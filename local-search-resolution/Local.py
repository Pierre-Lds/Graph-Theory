# ##### COPYRIGHT #####
#  ➔ File created by Hugo BOURREAU (aka SkY)
#  ➔ All right reserved
#  ➔ If you find this code online (Github, forum, etc...) please credit !
#  ➔ Have a good day !
#    ##### END #####
import datetime
from GraphLocal import GraphLocal
from art import *

def saveTime(n, m, time):
    f = open("../instances/times/localSearch/time_x_" + str(m) + ".csv", "a")
    f.write(str(n) + ";" + str(time) + "\n")

def saveWeights(n, m, weight):
    f = open("../instances/weights/localSearch/weights_x_" + str(m) + ".csv", "a")
    f.write(str(n) + ";" + str(weight) + "\n")

def main():
    #tprint("Local_search")
    for elem in [25]:   #elem is the percentage of edges
        for k in range (5, 21, 5):  #k is the number of vertices  + in range(begin include, end exclude, pas), WARNING : if the input don't exists, we have an error
            bob = GraphLocal("../instances/input_x_" + str(elem)+ "/" + str(k) + "_" + str(elem)+ ".in")
            start_time = datetime.datetime.now()
            node, weight = bob.maxWeightNode()
            clique, weight = bob.realLocalSearch(node)
            vrai_time = str((datetime.datetime.now() - start_time).total_seconds())
            print(str(k) + "_" + str(elem)+ ".in")
            print("Execution time : " + str(vrai_time))
            print(weight)
            print("\n")

            ## Write the result in files
            # f = open("localSearch_x_" + str(elem)+ "/" + str(k) + "_" + str(elem)+ "_localSearch.out", "w")
            # f.write(str(len(clique)) + " " + str(weight) + '\n')
            # for i in range(len(clique)):
            #     f.write(str(clique[i] + 1) + ' ')
            # f.close()
            # saveTime(k, elem, vrai_time)
            # saveWeights(k, elem, weight)


main()
