# 定一个类表示状态空间的节点。

class Node:
    
    def __init__(self, state, parent, actions):
        self.state = state
        self.parent = parent
        self.actions = actions
        

def solution_path(graph, init, goal):
    #返回解路径。 从goal节点反溯parent，直到到达init节点。
    path = [goal]
    current_parent = graph[goal].parent
    while current_parent!= None:
        path.append(current_parent)
        current_parent = graph[current_parent].parent
    path.reverse()
    
    return path

graph = { 'S': Node('S', None, ['A', 'D']),
          'A':Node('A',None,['B']),
          'D':Node('D',None,['G']),
          'B':Node('B',None,['C','G']),
          'G':Node('G',None,[]),
          'C':Node('C',None,['G'])}