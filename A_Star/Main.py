import math
class Node:
    def __init__(self,parent,name,g,h,visited):
        self.parent = parent
        self.name = name
        self.g = g
        self.h = h
        self.f = self.g + self.h
        self.visited = visited


class Graph:

    def __init__(self,graph,heuristicCost,start,goal):
        self.nodeList = []
        self.heuristicCost = heuristicCost
        for node in graph:
            self.nodeList.append(Node(None,node,math.inf,heuristic_cost[node],False))
        self.mGraph = self.convertedGraph(graph)
        self.start = start
        self.goal = goal

    def convertedGraph(self, graph):
        map1 = {}
        for node in graph:
            map2 = {}
            for n in graph[node]:
                map2[self.getNode(n)] = graph[node][n]
            map1[self.getNode(node)] = map2
        return map1


    def getNode(self,name):
        for node in self.nodeList:
            if node.name is name:
                return node

    def printResult(self):
        res = []
        node = self.getNode(self.goal)
        print('Minimum Cost Is: ',node.f)
        while node.parent is not None:
            res.append(node.name)
            node = node.parent
        res.append(self.getNode(self.start).name)
        res.reverse()
        print('Path: ',end='')
        for i in res:
            print(i,'-> ',end='')



def getPriorityNode(listOfNode):
    maxValue = math.inf
    priorityNode = None
    for node in listOfNode:
        if node.f < maxValue:
            priorityNode = node
            maxValue = node.f
    listOfNode.remove(priorityNode)
    return priorityNode

def isEmpty(ls):
    if  len(ls) is 0:
        return True
    return False

def chechExistenceInOpen(open,node):
    for n in open:
        if n.name is node.name:
            return True
    return False

def chechExistenceInClosed(closed,node):
    for n in closed:
        if n.name is node.name:
            return True
    return False


def A_Star(grp):
    openSet = []
    closedSet = []
    succes = False
    node = grp.getNode(grph.start)
    node.g = 0
    node.f = node.g + node.h
    openSet.append(node)
    while isEmpty(openSet) is False:
        node = getPriorityNode(openSet)
        closedSet.append(node)
        if node.name is grp.goal:
            succes = True
            break

        for mNode in grph.mGraph[node]:
            if chechExistenceInOpen(openSet,mNode) is False and chechExistenceInClosed(closedSet,mNode) is False:
                cost = grph.mGraph[node][mNode]
                mNode.g = cost + node.g
                mNode.f = mNode.g + mNode.h
                mNode.parent = node
                openSet.append(mNode)

            elif chechExistenceInOpen(openSet,mNode) is True or chechExistenceInClosed(closedSet, mNode) is True:
                cost = grph.mGraph[node][mNode]
                if  (node.g + cost + mNode.h) < mNode.f:
                    mNode.g = node.g + cost
                    mNode.f = mNode.g + mNode.h
                    mNode.parent = node
                    if chechExistenceInClosed(closedSet,mNode) is True:
                        closedSet.remove(mNode)
                        openSet.append(mNode)

    if succes:
        print("Success")
        grph.printResult()
    else:
        print("Path Not Found")

gp = {
    'A':{'B':3,'C':1},
    'B':{'D':3},
    'C':{'D':1,'G':2},
    'D':{'G':3},
    'G':{},
    'S':{'A':1,'G':12}
}
heuristic_cost = {'A':4,'B':5,'C':3,'D':4,'G':0, 'S':10}

grph = Graph(gp,heuristic_cost,'S','G')
A_Star(grph)