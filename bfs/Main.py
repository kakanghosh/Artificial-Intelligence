from queue import Queue
class Node:
    def __init__(self,parent,name,visited):
        self.parent = parent
        self.name = name
        self.visited = visited

class Graph:

    def __init__(self,graph,start,goal):
        self.nodeList = []
        for node in graph:
            self.nodeList.append(Node(None,node,False))
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

def BFS(grp):
    queue = Queue()
    node = grph.getNode(grph.start)
    queue.put(node)
    node.visited =True
    found = False
    while queue.empty() is not True:
        node = queue.get()
        for nextNode in grp.graph[node]:
            if nextNode.visited is False:
                nextNode.parent = node
                if nextNode.name is grp.goal:
                    found = True
                    break
                queue.put(nextNode)
                nextNode.visited =True
        if found is True:
            break



gp = {
    '0': ['1','3','8'],
    '1': ['0','7'],
    '2': ['3','5','7'],
    '3': ['0','2','4'],
    '4': ['3','8'],
    '5': ['2','6'],
    '6': ['5'],
    '7': ['1','2'],
    '8': ['0','4']
}

grph = Graph(gp,'0','6')
BFS(grph)
grph.printResult()