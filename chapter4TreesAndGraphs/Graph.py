class Graph():
    def __init__(self, directed = False):
        self.V = {}
        self.directed = directed

    def addVertex(self, vertex):
        if vertex not in self.V:
            self.V[vertex] = []

    def addEdge(self, v1, v2):
        self.addEdgeHelper(v1,v2)
        #if undirected graph, add reversed path v2->v1
        if not self.directed:
            self.addEdgeHelper(v2,v1)
    
    def addEdgeHelper(self, start, end):
        if start in self.V:
            self.V[start].append(end)
        else:
            self.V[start] = end


class Node():
    def __init__(self, data):
        self.data = data

class NodeWithEdges():
    def __init__(self, data, edges):
        self.data = data
        # assumes at most one edge in each direction between nodes
        self.edges = set()

class GraphNodeWithEdges():
    def __init__(self, directed = False):
        # because we add node objects into this graph implementation, each node
        # will have unique address in memory, thus we do not need set
        self.nodes = []
        self.directed = directed

    def addNode(self, node):
        self.nodes.append(node)

    def addEdge(self, node1, node2):
        self.addEdgeHlper(node1, node2)
        if not self.directed:
            self.addEdgeHlper(node2, node1)

    def addEdgeHlper(self, start, end):
        if end in start.edges:
            print "edge already exists"
        else:
            start.edges.add(end) 