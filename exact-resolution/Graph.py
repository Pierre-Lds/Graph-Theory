import numpy as np


class Graph:
    def __init__(self, inputFile):
        with open(inputFile, 'r', encoding='utf-8') as infile:
            self.file = inputFile
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

    def getCliqueWeight(self, vertices):
        size = len(vertices)
        weight = 0
        for i in range(size):
            for j in range(i+1, size):
                weight += self.graph[vertices[i]][vertices[j]]
        return weight

    def isCliqueOld(self, k):
        length = len(k)
        for i in range(length):
            for j in range(i + 1, length):
                # If any edge is missing
                if self.graph[k[i]][k[j]] == 0:
                    print(str(k[i]) + " " + str(k[j]))
                    return False
        return True

    def isClique(self, k):
        for i in range(0, k-1):
            # If any edge is missing
            if self.graph[self.store[i]][self.store[k]] == 0:
                return False
        return True

    def isMaxClique(self, clique):  # Compare current clique to max clique (we have/stored)
        # if self.store[0] == 3 and self.store[1] == 7 and self.store[2] == 8:
        #     print(*self.store)
        newClique = self.store[:clique]
        cliqueWeight = self.getCliqueWeight(newClique)
        if self.maxClique[1] < cliqueWeight:
            self.maxClique[0] = newClique
            self.maxClique[1] = cliqueWeight

    def getMaxClique(self):
        return self.maxClique

    def findCliques(self, i, l):
        bigger = False
        for j in range(i+1, self.n):
            # Check if any vertices from i+1 can be inserted
            if self.degres[j] >= l and (self.graph[i][j] != 0 or i == -1):  # If the degree of the |vertex| is sufficient |s->l ?|
                self.store[l] = j  # Add the vertex to store
                # If the graph is not a clique of size k then it cannot be a clique by adding another edge
                if self.isClique(l):  # If the length of the clique is still less than the desired size
                    bigger = True
                    # if l < s:  # Recursion to add vertices
                    if not self.findCliques(j, l + 1):
                        self.isMaxClique(l + 1)
                    # else:  # Size is met
                # else:

        return bigger

    def printMaxClique(self):
        print(str(len(self.maxClique[0])) + " " + str(self.maxClique[1]))
        for i in range(len(self.maxClique[0])):
            print(self.maxClique[0][i] + 1, end=' ')
        print("")

    def writeInFile(self, path):
        # file = self.file
        # lastElem = len(file)
        file = self.file.split('/')[-1].split(".")[0]
        f = open("../" + path + "/" + file + "_exact.out", "w")
        f.write(str(len(self.maxClique[0])) + " " + str(self.maxClique[1]) + "\n")
        for i in range(len(self.maxClique[0])):
            f.write(str(self.maxClique[0][i] + 1) + " ")
        f.write("\n")
