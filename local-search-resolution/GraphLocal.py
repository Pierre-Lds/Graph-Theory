# ##### COPYRIGHT #####
#  ➔ File created by Hugo BOURREAU (aka SkY)
#  ➔ All right reserved
#  ➔ If you find this code online (Github, forum, etc...) please credit !
#  ➔ Have a good day !
#    ##### END #####
import datetime
from random import randrange, randint

import numpy as np


class GraphLocal:

    def __init__(self, inputFile):
        with open(inputFile, 'r', encoding='utf-8') as infile:
            self.n = int(infile.readline().split(' ')[0])  # n = number of vertices
            self.graph = np.zeros((self.n, self.n))  # graph is a matrice n*n
            self.degres = [0] * self.n  # degres is degre of every vertex
            for line in infile:
                line = line.split()
                # Fill graph
                self.graph[int(line[0])-1][int(line[1])-1] = line[2]
                self.graph[int(line[1])-1][int(line[0])-1] = line[2]
                # Fill degres
                self.degres[int(line[0])-1] += 1
                self.degres[int(line[1])-1] += 1
        self.maxClique = [[], 0]
        self.store = [-1] * self.n  # Store current vertices in getMaxClique
        for val in range(self.n):
            self.graph[val][val] = -1

    def maxWeightNode(self):
        weightMax = 0
        maxWeightVertex = 0
        for vertex in range(self.n):
            weight = 0
            for linked_vertex in range(self.n):
                weight += self.graph[vertex][linked_vertex]
            if weight > weightMax:
                weightMax = weight
                maxWeightVertex = vertex
        return maxWeightVertex, weightMax

    def isClique(self, k):
        size = len(k) - 1
        if (size == 1 and self.graph[k[0]][k[1]] == 0) or self.graph[k[size-1]][k[size]] == 0:
            return False
        for i in range(0, size-2 + 1):
            # If any edge is missing
            if self.graph[k[i]][k[size]] == 0 or self.graph[k[i]][k[size-1]] == 0:
                return False
        return True

    def isCliqueOld(self, k):
        length = len(k)
        for i in range(length):
            for j in range(i + 1, length):
                # If any edge is missing
                if self.graph[k[i]][k[j]] == 0:
                    print(str(k[i]) + " " + str(k[j]))
                    return False
        return True

    def getCliqueWeight(self, vertices, param =0):
        size = len(vertices)-param
        weight = 0
        for i in range(size):
            for j in range(i+1, size):
                weight += self.graph[vertices[i]][vertices[j]]
        return weight

    def getNeighbors(self, i):
        neighbors = []
        for elem in range(self.n):
            if self.graph[i][elem] > 0:
                neighbors.append(elem)
        return neighbors

    def realLocalSearch(self, s, cutoff_time=-1, iteration_max=-1):
        start_time = datetime.datetime.now()
        iteration = 0
        clique = [s]  # Where we store the clique
        neighbors_of_s = self.getNeighbors(s)  # Get neighbors of s

        while len(neighbors_of_s) != 0 and ((datetime.datetime.now() - start_time).total_seconds() < cutoff_time or cutoff_time == -1) and (iteration < iteration_max or iteration_max == -1):

            vertex1 = neighbors_of_s[randint(0, len(neighbors_of_s) - 1)]
            neighbors_of_s.remove(vertex1)
            clique.append(vertex1)

            if not neighbors_of_s:
                if self.isClique(clique):
                    return clique, self.getCliqueWeight(clique)
                else:
                    return clique[:-1], self.getCliqueWeight(clique, 1)

            # If at the beginning of the loop 1 elem left we have to remove only one so we don't go here
            vertex2 = neighbors_of_s[randint(0, len(neighbors_of_s) - 1)]
            neighbors_of_s.remove(vertex2)
            clique.append(vertex2)

            if self.isClique(clique):
                if neighbors_of_s:
                    clique.remove(clique[randint(0, len(clique) - 1)])  # We take of a random vertex
            else:
                clique = clique[:-2]  # We remove added vertices

            iteration += 1

        return clique, self.getCliqueWeight(clique)

