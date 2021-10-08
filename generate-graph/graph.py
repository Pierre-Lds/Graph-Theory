import numpy as np
import random


class Graph:
    def __init__(self, nb_of_vertices, purcentage_of_edges):
        self.graph = np.zeros((nb_of_vertices, nb_of_vertices))
        self.n = nb_of_vertices
        self.m = purcentage_of_edges
        self.nbOfEdges = 0

    def addEdge(self, i, j, weight):
        self.graph[i][j] = weight
        self.graph[j][i] = weight
        self.nbOfEdges += 1

    def isConnex(self, DFS_BFS):
        color = [0] * self.n
        if DFS_BFS:
            self.DFS_visit(0, color)
        else:
            self.BFS_visit(0, color)
        if 0 in color:
            return False
        return True

    def DFS_visit(self, vertex, color):
        color[vertex] = 1
        for neighbor in range(self.n):
            if self.areConnected(vertex, neighbor) and color[neighbor] == 0:
                self.DFS_visit(neighbor, color)

    def BFS_visit(self, vertex, color):
        queue = []
        color[vertex] = 1
        queue.append(vertex)
        while queue:
            current = queue.pop()
            for neighbor in range(self.n):
                if self.areConnected(current, neighbor) and color[neighbor] == 0:
                    color[neighbor] = 1
                    queue.append(neighbor)

    def getWeight(self, i, j):
        return self.graph[i][j]

    def areConnected(self, i, j):
        if self.graph[i][j]:
            return True
        return False

    # def fillGraph(self, n, m):
    #     for i in range(n):
    #         for j in range(i + 1, n):
    #             if secrets.randbelow(101) < m:
    #                 self.addEdge(i, j, secrets.randbelow(101))

    def fillGraph(self, n, m):
        for i in range(n):
            for j in range(i + 1, n):
                if random.randint(1, 100) <= m:
                    self.addEdge(i, j, random.randint(1, 100))

    def writeInFile(self):
        f = open(str(self.n) + "_" + str(self.m) + ".in", "w")
        f.write(str(self.n) + " " + str(self.nbOfEdges) + "\n")
        for i in range(self.n):
            for j in range(i + 1, self.n):
                if self.areConnected(i, j):
                    f.write(str(i + 1) + " " + str(j + 1) + " " + str(int(self.getWeight(i, j))) + "\n")
        f.close()

    def userGraphGenerated(self):
        print("Le graphe est généré, je suis en train d'écrire mon lapin")

    def userFinished(self):
        print("Ca y est c'est fini :D")
        print("Le fichier généré s'appelle : " + str(self.n) + "_" + str(self.m) + ".in")

    def resetGraph(self):
        self.nbOfEdges = 0
        self.graph = np.zeros((self.n, self.n))
