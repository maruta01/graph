
INF = float("inf")

# ===============================#
#        Find Path shostest      #
# ===============================#
def ShortestFind(startNode, endNode, nodes, nearbyList):

    unvisitedNodes = nodes.copy()
    distanceFromStart = {
        node: (0 if node == startNode else INF) for node in nodes
    }
    previousNode = {node: None for node in nodes}
    while unvisitedNodes:

        currentNode = min(
            unvisitedNodes, key=lambda node: distanceFromStart[node]
        )
        unvisitedNodes.remove(currentNode)

        if distanceFromStart[currentNode] == INF:
            break
        for neighbor, distance in nearbyList[currentNode]:
            newPath = distanceFromStart[currentNode] + distance

            if newPath < distanceFromStart[neighbor]:
                distanceFromStart[neighbor] = newPath
                previousNode[neighbor] = currentNode
        if currentNode == endNode:
            break

    path = []
    currentNode = endNode
    while previousNode[currentNode] is not None:
        path.append(currentNode)
        currentNode = previousNode[currentNode]
    path.append(startNode)
    path.reverse()
    return path, distanceFromStart[endNode]

# ===============================#
#           INPUT FILE           #
# ===============================#
def Graph(fileName):
    graphEdges = []
    with open(fileName) as fhandle:
        for line in fhandle:
            edgeFrom, edgeTo, cost, *_ = line.strip().split(",")
            graphEdges.append((edgeFrom.upper(), edgeTo.upper(), float(cost)))
    nodes = set()
    for edge in graphEdges:
        nodes.update([edge[0], edge[1]])
    nearbyList = {node: set() for node in nodes}

    for edge in graphEdges:
        nearbyList[edge[0]].add((edge[1], edge[2]))
        nearbyList[edge[1]].add((edge[0], edge[2]))
    return nodes, nearbyList

# ==================================#
#               Main                #
#===================================#

check_find = True
while check_find:
    fileName = input("graph file name ? : ")
    try:
        nodes, nearbyList = Graph(fileName)
        check_find = False
        print("Input file compleate")
    except:
        print("!! Can't find this file or Incorrect data . Please check again. !!")

    print("***********************************************************************")

while True:
    startNode = input("node start : ").upper()
    endNode = input("node end : ").upper()

    try:
        path, distance = ShortestFind(startNode, endNode, nodes, nearbyList)
        showPath = ""
        i = 0
        for pathNow in path:
            showPath += pathNow
            if (i+1) < len(path):
                showPath += " -> "
            i += 1
        if distance != INF :
            print("Path form ", startNode, " to ", endNode, " : [ ", showPath, " ] and have cost ", distance)
        else :
            print("Path form ", startNode, " to ", endNode, " : No path .")

    except Exception as e:
        print("!! This node ", e, " information is not available. !!")
    print("=======================================================================")
