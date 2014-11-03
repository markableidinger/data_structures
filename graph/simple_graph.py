class Vertex:
    def __init__(self, value):
        self.value = value


class Edge:
    def __init__(self, vertex1, vertex2):
        self.connections = (vertex1, vertex2)


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

    def add_edge(self, vertex1, vertex2):
        '''adds an edge between the two vertices passed in'''
        if vertex1 == vertex2:
            raise ValueError('You can\'t link a vertex to itself, idiot.')
        if self.find_edge(vertex1, vertex2) is None:
            if not self.has_vertex(vertex1.value):
                self.vertices.append(vertex1)
            if not self.has_vertex(vertex2.value):
                self.vertices.append(vertex2)
            self.edges.append(Edge(vertex1, vertex2))
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