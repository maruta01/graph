import unittest


class TestGraph(unittest.TestCase):

    def setUp(self):
        self.nodes = set()
        self.fileName = "./graph.csv"
        self.startNode = 'A'
        self.endNode = 'G'
        self.INF = float('inf')
        self.answerPath = ['A', 'D', 'G']
        self.answerDistance = 9

    def test_input_graph(self):

        self.graphEdges = []
        with open(self.fileName) as fhandle:
            for line in fhandle:
                edgeFrom, edgeTo, cost, *_ = line.strip().split(",")
                self.graphEdges.append(
                    (edgeFrom.upper(), edgeTo.upper(), float(cost)))

        self.nodes = set()
        for edge in self.graphEdges:
            self.nodes.update([edge[0], edge[1]])
        self.nearbyList = {node: set() for node in self.nodes}

        for edge in self.graphEdges:
            self.nearbyList[edge[0]].add((edge[1], edge[2]))
            self.nearbyList[edge[1]].add((edge[0], edge[2]))

        print("TEST- 1 Check Node ")

        self.assertTrue(list(self.nodes).index("A") >= 0)
        self.assertTrue(list(self.nodes).index("B") >= 0)
        self.assertTrue(list(self.nodes).index("C") >= 0)
        self.assertTrue(list(self.nodes).index("D") >= 0)
        self.assertTrue(list(self.nodes).index("E") >= 0)
        self.assertTrue(list(self.nodes).index("F") >= 0)
        self.assertTrue(list(self.nodes).index("G") >= 0)
        self.assertTrue(list(self.nodes).index("H") >= 0)
        self.assertTrue(list(self.nodes).index("I") >= 0)
        print("........................Pass ")

        print("TEST - 2 Nearby Node")

        self.assertTrue(self.nearbyList['A'] == {('E', 4.0), ('B', 5.0), ('D', 3.0)})
        self.assertTrue(self.nearbyList['B'] == {('C', 4.0), ('A', 5.0)})
        self.assertTrue(self.nearbyList['C'] == {('B', 4.0), ('G', 2.0)})
        self.assertTrue(self.nearbyList['D'] == {('A', 3.0), ('G', 6.0)})
        self.assertTrue(self.nearbyList['E'] == {('F', 6.0), ('A', 4.0)})
        self.assertTrue(self.nearbyList['F'] == {('E', 6.0), ('H', 5.0)})
        self.assertTrue(self.nearbyList['G'] == {('C', 2.0), ('H', 3.0), ('D', 6.0)})
        self.assertTrue(self.nearbyList['H'] == {('G', 3.0), ('F', 5.0)})
        self.assertTrue(self.nearbyList['I'] == {('0', 0.0)})
        
        print("........................Pass ")

        unvisitedNodes = self.nodes.copy()
        distanceFromStart = {
            node: (0 if node == self.startNode else self.INF) for node in self.nodes
        }
        previousNode = {node: None for node in self.nodes}
        while unvisitedNodes:

            currentNode = min(
                unvisitedNodes, key=lambda node: distanceFromStart[node]
            )
            unvisitedNodes.remove(currentNode)

            if distanceFromStart[currentNode] == self.INF:
                break
            for neighbor, distance in self.nearbyList[currentNode]:
                newPath = distanceFromStart[currentNode] + distance

                if newPath < distanceFromStart[neighbor]:
                    distanceFromStart[neighbor] = newPath
                    previousNode[neighbor] = currentNode
            if currentNode == self.endNode:
                break

        path = []
        currentNode = self.endNode
        while previousNode[currentNode] is not None:
            path.append(currentNode)
            currentNode = previousNode[currentNode]
        path.append(self.startNode)
        path.reverse()
        print("TEST - 3 Chack Path ")
        self.assertEqual(path, self.answerPath)
        print("........................Pass ")

        print("TEST - 4 Chack COST ")
        self.assertEqual(distanceFromStart[self.endNode], self.answerDistance)
        print("........................Pass ")


if __name__ == '__main__':
    unittest.main()
