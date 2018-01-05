import math
class Node:
    def __init__(self,parent,name,heuristicCost,visited):
        self.parent = parent
        self.name = name
        self.heuristicCost = heuristicCost
        self.visited = visited

class Graph:

    def __init__(self,graph,heuristic,start,goal):
        self.nodeList = []
        for node in graph:
            self.nodeList.append(Node(None,node,heuristic[node],False))
        self.graph = self.convertedGraph(graph)
        self.start = start
        self.goal = goal

    def convertedGraph(self,graph):
        new_map = {}
        for node in graph:
            ls = []
            for leaf in graph[node]:
                ls.append(self.getNode(leaf))
            new_map[self.getNode(node)] = ls
        return new_map


    def getNode(self,name):
        for node in self.nodeList:
            if node.name is name:
                return node

    def printResult(self):
        res = []
        node = self.getNode(self.goal)
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
        if node.heuristicCost < maxValue:
            priorityNode = node
            maxValue = node.heuristicCost
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


def GBFS(grp):
    openSet = []
    closedSet = []
    succes = False
    node = grp.getNode('S')
    openSet.append(node)
    while isEmpty(openSet) is not True:
        node = getPriorityNode(openSet)
        if node.name is grp.goal:
            succes = True
            break
        closedSet.append(node)
        for mNode in grp.graph[node]:
            if chechExistenceInOpen(openSet,mNode) is not True and chechExistenceInClosed(closedSet,mNode) is not True:
                mNode.parent = node
                openSet.append(mNode)
    if succes:
        grph.printResult()
    else:
        print('Path Not Found')


gp = {
    'A':['B','C'],
    'B':['D'],
    'C':['D','G'],
    'D':['G'],
    'G':[],
    'S':['A','G']
}
heuristic_Cost = {'A':15,'B':7,'C':8,'D':6,'G':0,'S':20}
grph = Graph(gp,heuristic_Cost,'S','D')
GBFS(grph)
