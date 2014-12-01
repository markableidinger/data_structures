import unittest
from simple_graph import *


class SimpleGraphTestCase(unittest.TestCase):
    '''Tests for simple_graph.py'''

    #Happy test cases

    def test_constructor(self):
        '''Tests that the constructor creates the correct object'''
        test_graph = Graph()
        self.assertIsInstance(test_graph, Graph)

    def test_add_vertex(self):
        '''Tests that add_vertex adds a vertex as expected'''
        test_graph = Graph()
        test_graph.add_vertex('value')
        self.assertTrue(len(test_graph.vertices) == 1)
        self.assertIsInstance(test_graph.vertices[0], Vertex)
        self.assertTrue(test_graph.vertices[0].value == 'value')

    def test_has_vertex(self):
        '''Tests that has_vertex returns as expected'''
        test_graph = Graph()
        test_graph.add_vertex('value')
        self.assertTrue(test_graph.has_vertex('value'))
        self.assertTrue(test_graph.vertices[0].value == 'value')
        self.assertFalse(test_graph.has_vertex('wrong value'))

    def test_add_edge(self):
        '''Tests that add_edge adds an edge between existing vertices'''
        test_graph = Graph()
        test_graph.add_vertex(1)
        test_graph.add_vertex(2)
        vert_1, vert_2 = test_graph.vertices[0], test_graph.vertices[1]
        test_graph.add_edge(vert_1, vert_2)
        edge = test_graph.edges[0]
        self.assertIsInstance(edge, Edge)
        self.assertTrue(edge.connections == (vert_1, vert_2))

    def test_add_edge_new_vertices(self):
        '''Tests that add_edge adds vertices to the graph
                    if not already present'''
        test_graph = Graph()
        v_1 = Vertex(1)
        v_2 = Vertex(2)
        test_graph.add_edge(v_1, v_2)
        self.assertTrue(test_graph.vertices == [v_1, v_2])
        self.assertTrue(len(test_graph.edges) == 1)
        self.assertTrue(test_graph.edges[0].connections == (v_1, v_2))

    def test_find_edge(self):
        '''Tests that find_edge returns an Edge object when an edge exists
                    and False when it does not'''
        test_graph = Graph()
        v_1 = Vertex(1)
        v_2 = Vertex(2)
        test_graph.add_edge(v_1, v_2)
        self.assertIsInstance(test_graph.find_edge(v_1, v_2), Edge)

    def test_find_vertex_edges(self):
        '''Tests that find_vertex_edges returns a list of edges that attach
                    to the node passed in'''
        test_graph = Graph()
        v_1 = Vertex(1)
        v_2 = Vertex(2)
        v_3 = Vertex(3)
        v_4 = Vertex(4)
        test_graph.add_edge(v_1, v_2)
        test_graph.add_edge(v_1, v_3)
        test_graph.add_edge(v_1, v_4)
        self.assertTrue(len(test_graph.find_vertex_edges(v_1)) == 3)
        self.assertTrue(test_graph.find_vertex_edges(v_1) == test_graph.edges)

    def test_delete_vertex(self):
        '''Tests that deleting a vertex removes the vertex
                    and all connected edges'''
        test_graph = Graph()
        v_1 = Vertex(1)
        v_2 = Vertex(2)
        v_3 = Vertex(3)
        v_4 = Vertex(4)
        test_graph.add_edge(v_1, v_2)
        test_graph.add_edge(v_1, v_3)
        test_graph.add_edge(v_1, v_4)
        self.assertTrue(v_1 in test_graph.vertices)
        test_graph.delete_vertex(v_1)
        self.assertTrue(v_1 not in test_graph.vertices)
        self.assertTrue(len(test_graph.edges) == 0)

    def test_delete_edge(self):
        '''Tests that deleting an edge deletes the appropriate edge'''
        test_graph = Graph()
        v_1 = Vertex(1)
        v_2 = Vertex(2)
        v_3 = Vertex(3)
        v_4 = Vertex(4)
        test_graph.add_edge(v_1, v_2)
        test_graph.add_edge(v_1, v_3)
        test_graph.add_edge(v_1, v_4)
        self.assertTrue(test_graph.edges[0].connections == (v_1, v_2))
        self.assertTrue(len(test_graph.edges) == 3)
        test_graph.delete_edge(v_1, v_2)
        self.assertFalse(test_graph.edges[0].connections == (v_1, v_2))
        self.assertTrue(len(test_graph.edges) == 2)

    def test_adjacent(self):
        '''Tests that adjacent returns true for linked vertices
                    and false for unlinked'''
        test_graph = Graph()
        v_1 = Vertex(1)
        v_2 = Vertex(2)
        v_3 = Vertex(3)
        v_4 = Vertex(4)
        test_graph.add_edge(v_1, v_2)
        test_graph.add_edge(v_1, v_3)
        test_graph.add_edge(v_1, v_4)
        self.assertTrue(test_graph.adjacent(v_1, v_2))
        self.assertFalse(test_graph.adjacent(v_2, v_3))

    def test_neighbors(self):
        '''Tests that neighbors returns a list of vertices linked by edges
                    to the vertex passed in'''
        test_graph = Graph()
        v_1 = Vertex(1)
        v_2 = Vertex(2)
        v_3 = Vertex(3)
        v_4 = Vertex(4)
        test_graph.add_edge(v_1, v_2)
        test_graph.add_edge(v_1, v_3)
        test_graph.add_edge(v_1, v_4)
        self.assertTrue(v_2 in test_graph.neighbors(v_1))
        self.assertTrue(v_3 in test_graph.neighbors(v_1))
        self.assertTrue(v_4 in test_graph.neighbors(v_1))
        self.assertTrue(v_1 in test_graph.neighbors(v_2))
        self.assertFalse(v_2 in test_graph.neighbors(v_3))

    def test_depth_first(self):
        test_graph = Graph()
        v_1 = Vertex(1)
        v_2 = Vertex(2)
        v_3 = Vertex(3)
        v_4 = Vertex(4)
        v_5 = Vertex(5)
        v_6 = Vertex(6)
        v_7 = Vertex(7)
        v_8 = Vertex(8)
        test_graph.add_edge(v_1, v_4)
        test_graph.add_edge(v_2, v_3)
        test_graph.add_edge(v_2, v_4)
        test_graph.add_edge(v_2, v_5)
        test_graph.add_edge(v_3, v_5)
        test_graph.add_edge(v_5, v_7)
        test_graph.add_edge(v_5, v_8)
        test_graph.add_edge(v_6, v_8)
        self.assertTrue(test_graph.breadth_first_unweighted(v_2) ==
            [v_2, v_3, v_4, v_5, v_1, v_7, v_8, v_6])
        self.assertTrue(test_graph.breadth_first_unweighted(v_5) ==
            [v_5, v_2, v_3, v_7, v_8, v_4, v_6, v_1])
        self.assertTrue(test_graph.depth_first_unweighted(v_2) ==
            [v_2, v_5, v_8, v_6, v_7, v_3, v_4, v_1])
        self.assertTrue(test_graph.depth_first_unweighted(v_5) ==
            [v_5, v_8, v_6, v_7, v_3, v_2, v_4, v_1])

    # Ugly test cases

    def test_empty_graph(self):
        '''Tests that delete_vertex, delete_edge, neighbors, and adjacent
                raise the correct errors if called on an empty graph'''
        test_graph = Graph()
        v_1 = Vertex(1)
        v_2 = Vertex(2)
        self.assertTrue(test_graph.vertices == [])
        self.assertTrue(test_graph.edges == [])
        self.assertFalse(test_graph.has_vertex(v_1))
        with self.assertRaises(ValueError) as context:
            test_graph.delete_vertex(v_1)
        with self.assertRaises(ValueError) as context:
            test_graph.delete_edge(v_1, v_2)
        with self.assertRaises(ValueError) as context:
            test_graph.neighbors(v_1)
        with self.assertRaises(ValueError) as context:
            test_graph.adjacent(v_1, v_2)

    def test_double_add(self):
        '''Tests that add_edge and add_vertex don't allow duplicates'''
        test_graph = Graph()
        v_1 = Vertex(1)
        v_2 = Vertex(2)
        test_graph.add_edge(v_1, v_2)
        with self.assertRaises(ValueError) as context:
            test_graph.add_vertex(2)
        with self.assertRaises(ValueError) as context:
            test_graph.add_edge(v_1, v_2)

    def test_ouroboros(self):
        '''Tests that you can't have an edge pointing
                back to the same vertex'''
        test_graph = Graph()
        test_graph.add_vertex(1)
        with self.assertRaises(ValueError) as context:
            test_graph.add_edge(test_graph.vertices[0], test_graph.vertices[0])

    def test_dijkstras(self):
        '''Tests that dijkstras works on a sample graph'''
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
        paths = test_graph.dijkstras(v_1)
        self.assertTrue(paths[v_1] == 0)
        self.assertTrue(paths[v_4] == 1)
        self.assertTrue(paths[v_2] == 8)
        self.assertTrue(paths[v_3] == 13)
        self.assertTrue(paths[v_5] == 16)
        self.assertTrue(paths[v_7] == 18)
        self.assertTrue(paths[v_8] == 35)
        self.assertTrue(paths[v_6] == 36)
        paths2 = test_graph.dijkstras(v_3)
        self.assertTrue(paths2[v_3] == 0)
        self.assertTrue(paths2[v_5] == 3)
        self.assertTrue(paths2[v_2] == 5)
        self.assertTrue(paths2[v_7] == 5)
        self.assertTrue(paths2[v_4] == 12)
        self.assertTrue(paths2[v_1] == 13)
        self.assertTrue(paths2[v_8] == 22)
        self.assertTrue(paths2[v_6] == 23)
