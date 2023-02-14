import numpy as np


class Vertex:
    def __init__(self, key, x=None, y=None):
        self.key = key
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.key == other.key

    def __hash__(self):
        return hash(self.key)


class AdjacencyMatrix:
    def __init__(self):
        self.vertex_list = []
        self.vertex_dict = {}
        self.adjacency_matrix = [[]]

    def insert_vertex(self, vertex):
        self.vertex_dict[vertex] = self.order()
        if self.order() != 0:
            self.adjacency_matrix.append([None for _ in range(self.order())])
        for i in range(len(self.adjacency_matrix)):
            self.adjacency_matrix[i].append(None)
        self.vertex_list.append(vertex)

    def insert_edge(self, vertex1, vertex2, weight=1):
        self.adjacency_matrix[self.vertex_dict[vertex1]][self.vertex_dict[vertex2]] = weight

    def order(self):
        return len(self.vertex_list)

    def initialize_adjacency_matrix(self, graph):
        for i in graph:
            if Vertex(i[0]) not in self.vertex_list:
                self.insert_vertex(Vertex(i[0]))
            if Vertex(i[1]) not in self.vertex_list:
                self.insert_vertex(Vertex(i[1]))
            self.insert_edge(Vertex(i[0]), Vertex(i[1]), 1)
            self.insert_edge(Vertex(i[1]), Vertex(i[0]), 1)

    def matrix_to_np(self):
        size = len(self.adjacency_matrix)
        numpy_matrix = np.ndarray((size, size))
        for i in range(size):
            for j in range(size):
                if self.adjacency_matrix[i][j] is None:
                    numpy_matrix[i][j] = 0
                else:
                    numpy_matrix[i][j] = self.adjacency_matrix[i][j]
        return numpy_matrix


def is_isomorphism(M, P, G):
    mg = M @ G
    tran_mg = mg.transpose()
    is_P = M @ tran_mg
    for i in range(len(is_P)):
        for j in range(len(is_P)):
            if P[i][j] != is_P[i][j]:
                return False
    return True

# W celu sprawienia, aby podstawa ullman'a zadziałała potrzebowałem delikatnej pomocy, ale pozostałe wersje ullman'a oraz funkcje do nich potrzebne zostały napisane samodzielnie.
def ullman_v1(G, P, used_columns=[], current_row=0, M=None):
    if M is None:
        M = np.ones((P.shape[0], G.shape[0]))
    if current_row == len(M):
        if is_isomorphism(M, P, G):
            return 1, 0
        return
    n0_of_isomorphisms = 0
    n0_of_recursions = 0
    index_list = []
    for j in range(M.shape[1]):
        if (j not in used_columns) and M[current_row, j] == 1:
            index_list.append(j)
    for i in index_list:
        used_columns_copy = used_columns.copy()
        used_columns_copy.append(i)
        M_copy = M.copy()
        row = np.array([0 for _ in range(len(M[current_row, :]))])
        row[i] = 1
        M_copy[current_row, :] = row
        next_step = ullman_v1(G, P, used_columns_copy, current_row + 1, M_copy)
        n0_of_recursions += 1
        if next_step is not None:
            n0_of_isomorphisms += next_step[0]
            n0_of_recursions += next_step[1]
    if n0_of_isomorphisms != 0:
        return n0_of_isomorphisms, n0_of_recursions
    return 0, n0_of_recursions


def M0(G, P):
    M = np.zeros((G.shape[0], P.shape[0]))
    for i in range(P.shape[0]):
        for j in range(G.shape[0]):
            if P[i].sum() >= G[j].sum():
                M[j, i] = 1
    return M


def ullman_v2(G, P, used_columns=[], current_row=0, M=None):
    if M is None:
        M = M0(P, G)
    if current_row == len(M):
        if is_isomorphism(M, P, G):
            return 1, 0
        return
    n0_of_isomorphisms = 0
    n0_of_recursions = 0
    index_list = []
    for j in range(M.shape[1]):
        if (j not in used_columns) and M[current_row, j] == 1:
            index_list.append(j)
    for i in index_list:
        used_columns_copy = used_columns.copy()
        used_columns_copy.append(i)
        M_copy = M.copy()
        row = np.array([0 for _ in range(len(M[current_row, :]))])
        row[i] = 1
        M_copy[current_row, :] = row
        next_step = ullman_v2(G, P, used_columns_copy, current_row + 1, M_copy)
        n0_of_recursions += 1
        if next_step is not None:
            n0_of_isomorphisms += next_step[0]
            n0_of_recursions += next_step[1]
    if n0_of_isomorphisms != 0:
        return n0_of_isomorphisms, n0_of_recursions
    return 0, n0_of_recursions


def prune(M, G, P, current_row):
    for i in range(current_row, len(M)):
        for j in range(len(M[0])):
            if M[i, j] == 1:
                for x in range(len(P[i])):
                    if P[i][x] != 0:
                        for y in range(len(G[j])):
                            if G[j][y] != 0:
                                if M[x][y] == 1:
                                    break
                        else:
                            M[i, j] = 0
    return M


def ullman_v3(G, P, used_columns=[], current_row=0, M=None):
    if M is None:
        M = M0(P, G)
    if current_row == len(M):
        if is_isomorphism(M, P, G):
            return 1, 0
        return
    M_prim = M.copy()
    M_pruned = prune(M_prim, G, P, current_row)
    n0_of_isomorphisms = 0
    n0_of_recursions = 0
    index_list = []
    for j in range(M.shape[1]):
        if (j not in used_columns) and M_pruned[current_row, j] == 1:
            index_list.append(j)
    for i in index_list:
        used_columns_copy = used_columns.copy()
        used_columns_copy.append(i)
        M_pruned_copy = M_pruned.copy()
        row = np.array([0 for _ in range(len(M[current_row, :]))])
        row[i] = 1
        M_pruned_copy[current_row, :] = row
        next_step = ullman_v3(G, P, used_columns_copy, current_row + 1, M_pruned_copy)
        n0_of_recursions += 1
        if next_step is not None:
            n0_of_isomorphisms += next_step[0]
            n0_of_recursions += next_step[1]
    if n0_of_isomorphisms != 0:
        return n0_of_isomorphisms, n0_of_recursions
    return 0, n0_of_recursions


graph_G = [('A', 'B', 1), ('B', 'F', 1), ('B', 'C', 1), ('C', 'D', 1), ('C', 'E', 1), ('D', 'E', 1)]
graph_P = [('A', 'B', 1), ('B', 'C', 1), ('A', 'C', 1)]

temp_G = AdjacencyMatrix()
temp_G.initialize_adjacency_matrix(graph_G)
adj_G = temp_G.matrix_to_np()
temp_P = AdjacencyMatrix()
temp_P.initialize_adjacency_matrix(graph_P)
adj_P = temp_P.matrix_to_np()

results_1 = ullman_v1(adj_G, adj_P)
print(str(results_1[0]) + "; " + str(results_1[1]))
results_2 = ullman_v2(adj_G, adj_P)
print(str(results_2[0]) + "; " + str(results_2[1]))
results_3 = ullman_v3(adj_G, adj_P)
print(str(results_3[0]) + "; " + str(results_3[1]))
