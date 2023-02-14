import polska


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


class AdjacencyMatrix:
    def __init__(self):
        self.list = []
        self.dict = {}
        self.adj_matrix = []

    def insert_vertex(self, vertex):
        self.list.append(Vertex(vertex))
        self.adj_matrix.append([0])
        self.dict[vertex] = self.get_vertex_idx(vertex)
        for i in range(len(self.list)):
            self.adj_matrix[i] = [0 for vertex in self.list]

    def insert_edge(self, vertex1, vertex2, edge=1):
        self.adj_matrix[self.dict[vertex1]][self.dict[vertex2]] = edge
        self.adj_matrix[self.dict[vertex2]][self.dict[vertex1]] = edge

    def delete_vertex(self, vertex):
        del self.adj_matrix[self.get_vertex_idx(vertex)]
        for j in range(len(self.adj_matrix)):
            del self.adj_matrix[j][self.get_vertex_idx(vertex)]
        del self.list[self.get_vertex_idx(vertex)]
        del self.dict[vertex]
        for key in self.dict.keys():
            self.dict[key] = self.get_vertex_idx(key)

    def delete_edge(self, vertex1, vertex2):
        self.adj_matrix[self.get_vertex_idx(vertex1)][self.get_vertex_idx(vertex2)] = 0
        self.adj_matrix[self.get_vertex_idx(vertex2)][self.get_vertex_idx(vertex1)] = 0

    def get_vertex_idx(self, vertex):
        return self.list.index(vertex)

    def get_vertex(self, vertex_idx):
        return self.list[vertex_idx]

    def neighbours(self, vertex_idx):
        no_neighbours = []
        for j in range(len(self.adj_matrix[vertex_idx])):
            if self.adj_matrix[vertex_idx][j] != 0:
                no_neighbours.append(j)
        return no_neighbours

    def order(self):
        return len(self.list)

    def size(self):
        size = 0
        for j in self.adj_matrix:
            for k in j:
                if k != 0:
                    size += 1
        return size // 2

    def edges(self):
        edges = []
        index = 0
        for j in self.list:
            for k in range(len(self.adj_matrix[index])):
                if self.adj_matrix[index][k] != 0:
                    edges.append((j.key, self.list[k].key))
            index += 1
        return edges


class AdjacencyList:
    def __init__(self):
        self.list = []
        self.dict = {}
        self.adj_list = []

    def insert_vertex(self, vertex):
        self.list.append(Vertex(vertex))
        self.adj_list.append([])
        self.dict[vertex] = self.get_vertex_idx(vertex)

    def insert_edge(self, vertex1, vertex2, edge=0):
        if vertex2 not in self.adj_list[self.dict[vertex1]]:
            self.adj_list[self.dict[vertex1]].append(vertex2)
        if vertex1 not in self.adj_list[self.dict[vertex2]]:
            self.adj_list[self.dict[vertex2]].append(vertex1)

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
        for j in self.adj_list[vertex_idx]:
            no_neighbours.append(self.get_vertex_idx(j))
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


def main():
    amatrix = AdjacencyMatrix()
    for i in polska.slownik.keys():
        amatrix.insert_vertex(i)
    
    for i in polska.graf:
        x, y = i
        amatrix.insert_edge(x, y)
    
    amatrix.delete_vertex('K')
    amatrix.delete_edge('E', 'W')
    polska.draw_map(amatrix.edges())
    
    alist = AdjacencyList()
    for i in polska.slownik.keys():
        alist.insert_vertex(i)
    
    for i in polska.graf:
        x, y = i
        alist.insert_edge(x, y)
    
    alist.delete_vertex('K')
    alist.delete_edge('E', 'W')
    polska.draw_map(alist.edges())


main()
