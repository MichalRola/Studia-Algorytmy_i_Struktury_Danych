import graf_mst
import string
from math import inf


class Vertex:
    def __init__(self, key):
        self.key = key

    def __hash__(self):
        return hash(self.key)

    def __eq__(self, other):
        return self.key == other

    def __str__(self):
        return str(self.key)


class Edge:
    def __init__(self, key1, key2, weight):
        self.key1 = key1
        self.key2 = key2
        self.weight = weight


class AdjacencyListWeighted:
    def __init__(self):
        self.list = []
        self.dict = {}
        self.adj_list = []
        self.weighted_list = []

    def insert_vertex(self, vertex):
        self.list.append(Vertex(vertex))
        self.adj_list.append([])
        self.dict[vertex] = self.get_vertex_idx(vertex)

    def insert_edge(self, vertex1, vertex2, weight=0):
        if vertex2 not in self.adj_list[self.dict[vertex1]]:
            self.adj_list[self.dict[vertex1]].append((vertex2, weight))
        if vertex1 not in self.adj_list[self.dict[vertex2]]:
            self.adj_list[self.dict[vertex2]].append((vertex1, weight))

    def delete_vertex(self, vertex):
        del self.adj_list[self.get_vertex_idx(vertex)]
        del self.list[self.get_vertex_idx(vertex)]
        del self.dict[vertex]
        for key in self.dict.keys():
            self.dict[key] = self.get_vertex_idx(key)
        for j in self.adj_list:
            for k in j:
                if k == vertex:
                    j.remove(vertex)

    def delete_edge(self, vertex1, vertex2):
        self.adj_list[self.get_vertex_idx(vertex1)].remove(vertex2)
        self.adj_list[self.get_vertex_idx(vertex2)].remove(vertex1)

    def get_vertex_idx(self, vertex):
        return self.list.index(vertex)

    def get_vertex(self, vertex_idx):
        return self.list[vertex_idx]

    def neighbours(self, vertex_idx):
        no_neighbours = []
        for (j, w) in self.adj_list[vertex_idx]:
            no_neighbours.append((self.get_vertex_idx(j), w))
        return no_neighbours

    def order(self):
        return len(self.list)

    def size(self):
        size = 0
        for j in self.adj_list:
            size += len(j)
        return size // 2

    def edges(self):
        edges = []
        index = 0
        for j in self.list:
            for k in self.adj_list[index]:
                edges.append((j.key, k))
            index += 1
        return edges


def printGraph(g):
    n = g.order()
    print("------GRAPH------",n)
    for i in range(n):
        v = g.get_vertex(i)
        print(v, end = " -> ")
        nbrs = g.neighbours(i)
        for (j, w) in nbrs:
            print(g.get_vertex(j), w, end="; ")
        print()
    print("-------------------") 


def primAlgorithm(g, s):
    sum = 0
    temp = AdjacencyListWeighted()
    in_tree = []
    distance = []
    parent = []

    for i in range(g.order()):
        temp.insert_vertex(string.ascii_uppercase[i])
        in_tree.append(0)
        distance.append(inf)
        parent.append(-1)

    v = temp.get_vertex_idx(s)

    while in_tree[v] == 0:
        in_tree[v] = 1
        nbrs = g.neighbours(v)
        for (j, w) in nbrs:
            if w < distance[j] and in_tree[j] == 0:
                distance[j] = w
                parent[j] = v

        min = inf

        for j in range(temp.order()):
            if in_tree[j] == 0 and distance[j] < min:
                min = distance[j]
                next = j
        if min == inf:
            return temp, sum
        temp.insert_edge(temp.get_vertex(next), temp.get_vertex(parent[next]), min)
        v = next
        sum += min

    return temp, sum


def main(): 
    walist = AdjacencyListWeighted()
    for i in range(10):     walist.insert_vertex(string.ascii_uppercase[i])
    for i in graf_mst.graf:
        v1, v2, weight = i
        walist.insert_edge(v1, v2, weight)
    prim, length = primAlgorithm(walist, "A")
    printGraph(prim)
    # print('"Dlugosc" drzewa rozpinajacego:', length)


main()
