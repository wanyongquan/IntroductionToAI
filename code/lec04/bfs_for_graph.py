from data import Node, graph, solution_path

# BFS 搜索
def BFS(graph, initState, goalState ):
    
    # open 表
    open_table = []
    closed_table = [] # closed表
    print_data(open_table, closed_table)
    
    open_table.append(initState)
    print_data(open_table, closed_table)
    
    while len(open_table) != 0:
        currentNode = open_table.pop(0)
        closed_table.append(currentNode)
        print_data(open_table, closed_table)
        
        if graph[currentNode].state == goalState:
            return solution_path(graph, initState, goalState)
        
        for sub_node in graph[currentNode].actions:
            if sub_node not in open_table and sub_node not in closed_table:
                graph[sub_node].parent = currentNode
                open_table.append(sub_node)
        print_data(open_table, closed_table)
        

def print_data(open, closed):
    print('open : {0}'.format(open))
    # print(open )
    print('closed : {0}'.format(closed))
    # print(closed)
    print('='*50)
    
if __name__ == '__main__':
    # 用字典来表示图
    # graph = { 'S': Node('S', None, ['A', 'D']),
    #           'A':Node('A',None,['B']),
    #           'D':Node('D',None,['G']),
    #           'B':Node('B',None,['C','G']),
    #           'G':Node('G',None,[]),
    #           'C':Node('C',None,['G'])}
    solution = BFS(graph, 'S', 'G')
    print(solution)
    