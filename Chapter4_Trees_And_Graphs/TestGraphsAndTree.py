import unittest
from Graph import Graph
from Tree import Tree
from Tree import BinaryNode
from checkSubtree import isSubTree


class Tests(unittest.TestCase):
    def setUp(self):
        pass

    def testGraphInit(self):
        graph = Graph()
        self.assertEqual(graph.V, {})

    def testAddVertex(self):
        graph = Graph()
        graph.addVertex(1)
        self.assertEqual(graph.V, {1: set()})

    def testAddEdge(self):
        graph = Graph()
        graph.addVertex(1)
        graph.addVertex(2)
        graph.addEdge(1, 2)
        self.assertEqual(graph.V, {1: set([2]), 2: set([1])})

    def testAddEdgeDirected(self):
        graph = Graph(directed=True)
        graph.addVertex(1)
        graph.addVertex(2)
        graph.addEdge(1, 2)
        self.assertEqual(graph.V, {1: set([2]), 2: set()})

    def test10CheckSubtree(self):
        t1RootNode = BinaryNode(1)
        t1Node2 = BinaryNode(2)
        t1Node3 = BinaryNode(3)
        t1Node4 = BinaryNode(4)
        t1Node5 = BinaryNode(5)
        t1Node6 = BinaryNode(6)
        t1RootNode.left = t1Node2
        t1RootNode.right = t1Node3
        t1Node3.left = t1Node4
        t1Node3.right = t1Node5
        t1Node5.left = t1Node6
        
        t2RootNode = BinaryNode(3)
        t2Node4 = BinaryNode(4)
        t2Node5 = BinaryNode(5)
        t2Node6 = BinaryNode(6)
        t2RootNode.left = t2Node4
        t2RootNode.right = t2Node5
        t2Node5.left = t2Node6
        
        t1 = Tree(t1RootNode)
        t2 = Tree(t2RootNode)

        self.assertEqual(isSubTree(t1.root,t2.root
                                   ), True)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
