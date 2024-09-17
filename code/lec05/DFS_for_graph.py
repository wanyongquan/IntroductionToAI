
'''
 DFS for graph
'''
class Node:
    
    def __init__(self, state, parent=None ):
        self.state = state
        self.parent = parent
        self.sub_nodes = []
        
    def setParent(self, parent):
        self.parent = parent
    
    def add_child(self, child_list):
        
        for child in child_list:
            self.sub_nodes.append(child)
            child.setParent(self)
    
    def get_child(self):
        return self.sub_nodes
    
    
def DFS( s, g):
    open_table = [s]
    closed_table = []
    
    return DFS_search(open_table, closed_table, g)

def DFS_search( open_table, closed_table, goal):
    current_node = open_table.pop(len(open_table) -1)
    print(current_node.state)
    if current_node.state == goal.state :
        return solution_path(g)
    
    closed_table.append(current_node)
    
    # 嵌套遍历图的顶点
    for child in current_node.get_child():
        if child not in closed_table:
            open_table.append(child)
            solution = DFS_search( open_table, closed_table,goal)
            if solution is not None:
                return solution
    
def solution_path( goal):
    #返回解路径。 从goal节点反溯parent，直到到达init节点。sssssssssssssssssssssssssssssssssssssssssssssssssssss 
    path = [goal.state]
    current_parent = goal.parent
    while current_parent!= None:
        path.append(current_parent.state)
        current_parent = current_parent.parent
    path.reverse()
    
    return path

if __name__ == '__main__':
    s = Node('s')
    b = Node('b')
    a = Node('a')
    c = Node('c')
    d = Node('d')
    g = Node('g')
    s.add_child([a,d])
    # s.add_child(d)
    a.add_child([b])
    d.add_child([g])
    b.add_child([c,g])
    # g.add_child(g)
    c.add_child([g])
    
    solution = DFS(s, g)
    print(solution)
    