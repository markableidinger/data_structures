import Queue


class Vertex:
    def __init__(self, value):
        self.value = value


class Edge:
    def __init__(self, vertex1, vertex2, weight=1):
        self.connections = (vertex1, vertex2)
        self.weight = weight


class Graph:
    def __init__(self):
        self.vertices = []
        self.edges = []

    def vertices(self):
        '''returns a list of vertices'''
        return self.vertices

    def edges(self):
        '''returns a list of edges'''
        return self.edges

    def has_vertex(self, value):
        '''checks if a value is represented as a vertex in the graph'''
        for vertex in self.vertices:
            if vertex.value == value:
                return True
        return False

    def add_vertex(self, value):
        '''adds a vertex with the value passed in'''
        if self.has_vertex(value):
            raise ValueError('That vertex already exists')
        self.vertices.append(Vertex(value))

    def find_edge(self, vertex1, vertex2):
        for edge in self.edges:
            if vertex1 in edge.connections and vertex2 in edge.connections:
                return edge
        return None

    def add_edge(self, vertex1, vertex2, weight=1):
        '''adds an edge between the two vertices passed in'''
        if vertex1 == vertex2:
            raise ValueError('You can\'t link a vertex to itself, idiot.')
        if self.find_edge(vertex1, vertex2) is None:
            if not self.has_vertex(vertex1.value):
                self.vertices.append(vertex1)
            if not self.has_vertex(vertex2.value):
                self.vertices.append(vertex2)
            self.edges.append(Edge(vertex1, vertex2, weight))
        else:
            raise ValueError('That edge already exists')

    def find_vertex_edges(self, vertex):
        '''returns a list of all edges attached to the current vertex'''
        vertex_edges = []
        if not self.has_vertex(vertex.value):
            return vertex_edges
        for edge in self.edges:
            if edge.connections[0] == vertex:
                vertex_edges.append(edge)
            elif edge.connections[1] == vertex:
                vertex_edges.append(edge)
        return vertex_edges

    def delete_vertex(self, vertex):
        '''removes a vertex and all of the edges attached to it'''
        if not self.has_vertex(vertex.value):
            raise ValueError('That vertex doesn\'t exist, stupid.')
        else:
            for edge in self.find_vertex_edges(vertex):
                self.edges.remove(edge)
            for el in self.vertices:
                if el == vertex:
                    self.vertices.remove(el)

    def delete_edge(self, vertex1, vertex2):
        '''deletes an edge between the 2 vertices passed in'''
        for edge in self.edges:
            if vertex1 in edge.connections and vertex2 in edge.connections:
                self.edges.remove(edge)
                break
        else:
            raise ValueError('That edge doesn\'t exist, idiot')

    def adjacent(self, vertex1, vertex2):
        '''returns true if the 2 vertices are linked by an edge
                    and false otherwise'''
        if vertex1 not in self.vertices or vertex2 not in self.vertices:
            raise ValueError("That vertex doesn't exist, stupid.")
        for edge in self.edges:
            if vertex1 in edge.connections and vertex2 in edge.connections:
                return True
        return False

    def neighbors(self, vertex):
        '''returns a list of all vertices connected by edges'''
        if vertex not in self.vertices:
            raise ValueError('That vertex doesn\'t exist, stupid')
        neighbors = []
        for edge in self.edges:
            if edge.connections[0] == vertex:
                neighbors.append(edge.connections[1])
            elif edge.connections[1] == vertex:
                neighbors.append(edge.connections[0])
        return neighbors

    def neighbors_weighted(self, vertex):
        if vertex not in self.vertices:
            raise ValueError('That vertex doesn\'t exist, stupid')
        neighbors = []
        for edge in self.edges:
            if edge.connections[0] == vertex:
                neighbors.append((edge.weight, edge.connections[1]))
            elif edge.connections[1] == vertex:
                neighbors.append((edge.weight, edge.connections[0]))
        return neighbors

    def breadth_first_unweighted(self, start):
        traversed = []
        queue = [start]
        while len(queue) > 0:
            current = queue.pop()
            if current in traversed:
                pass
            else:
                traversed.append(current)
                for vert in self.neighbors(current):
                    queue.insert(0, vert)
                print(current.value)
        return traversed

    def depth_first_unweighted(self, start):
        traversed = []
        queue = [start]
        while len(queue) > 0:
            current = queue.pop()
            if current in traversed:
                pass
            else:
                traversed.append(current)
                for vert in self.neighbors(current):
                    queue.append(vert)
        return traversed

    def dijkstras(self, start):
        pqueue = Queue.PriorityQueue()
        pqueue.put((0, start))
        visited = []
        paths = {start: 0}
        while not pqueue.empty():
            current = pqueue.get()
            current_weight = paths[current[1]]
            nbrs = self.neighbors_weighted(current[1])
            for node in nbrs:
                if node[1] in visited:
                    pass
                elif paths.get(node[1], None) is None:
                    paths[node[1]] = node[0] + current_weight
                    pqueue.put((node[0] + current_weight, node[1]))
                elif paths[node[1]] > node[0] + current_weight:
                    paths[node[1]] = node[0] + current_weight
            visited.append(current[1])
        return paths
# use put/get

    def bellman_ford(self, start):
        INF = float('inf')
        path_weight = {}
        predecessor = {}
        for v in self.vertices:
            path_weight[v] = INF
            predecessor[v] = None
        path_weight[start] = 0
        for i in range(len(self.vertices) - 1):
            for v1 in self.vertices:
                for v2 in self.neighbors_weighted(v1):
                    if path_weight[v2[1]] > v2[0] + path_weight[v1]:
                        path_weight[v2[1]] = path_weight[v1] + v2[0]
                        predecessor[v2[1]] = v1
        return path_weight, predecessor

test_graph = Graph()
v_1 = Vertex(1)
v_2 = Vertex(2)
v_3 = Vertex(3)
v_4 = Vertex(4)
v_5 = Vertex(5)
v_6 = Vertex(6)
v_7 = Vertex(7)
v_8 = Vertex(8)
test_graph.add_edge(v_1, v_4, 1)
test_graph.add_edge(v_2, v_3, 5)
test_graph.add_edge(v_2, v_4, 7)
test_graph.add_edge(v_2, v_5, 9)
test_graph.add_edge(v_3, v_5, 3)
test_graph.add_edge(v_5, v_7, 2)
test_graph.add_edge(v_5, v_8, 19)
test_graph.add_edge(v_6, v_8, 1)
bf = test_graph.bellman_ford(v_1)
weights = [(vert.value, val) for vert, val in bf[0].items()]
predecessors = [(vert.value, val) for vert, val in bf[1].items()]
print weights
print predecessors
