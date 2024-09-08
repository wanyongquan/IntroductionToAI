'''
宽度优先算法求解八数码问题；
'''
import numpy as np



class State:
    '''
    状态图
    '''
    def __init__(self, state, directionFlag=None, parent=None):
        self.state = state  # 当前状态
        self.depth = parent.depth + 1 if parent is not None else 0

        self.direction = ['up', 'down', 'right', 'left']  # 操作符 , 顺序即操作符运算顺序；
        if directionFlag:  # 被禁止的操作符（如果使用该操作符，会回到父亲节点，导致死循环）
            self.direction.remove(directionFlag)
        self.parent = parent  # 父节点
        self.symbol = 0  # 空格

    def getDirection(self):
        return self.direction

    def showInfo(self):
        for i in range(3):
            for j in range(3):
                print(self.state[i, j], end=' ')
            print("\n")

        print('->\n')
        return

    def printState(self):
        print('当前节点的深度：', self.depth)
        print(self.state)
        print('*'*20,'\n')

    def getEmptyPos(self):
        #返回空格的位置（索引）
        postion = np.where(self.state == self.symbol)

        return postion

    def generateSubNodes(self):
        '''
        根据余弦设定的操作符顺序扩展子节点
        :return: 子节点列表
        '''
        if not self.direction:
            return []

        subStates = []  # 子节点列表
        boarder = len(self.state) - 1 # 在八数码问题中，该值等于2，即九空格行索引的上界。
        row, col = self.getEmptyPos()
        #以下代码规定了 操作符的处理顺序为 up , down, left, right,
        if 'up' in self.direction and row > 0:  #如果向上移动是合法操作符，
            s = self.state.copy()
            temp = s.copy()
            s[row, col] = s[row - 1, col]
            s[row - 1, col] = temp[row, col]
            news = State(s, directionFlag='down', parent=self)
            subStates.append(news)
        if 'down' in self.direction and row < boarder:  #如果向右移动是合法操作符，
            s = self.state.copy()
            temp = s.copy()
            s[row, col] = s[row + 1, col]
            s[row + 1, col] = temp[row, col]
            news = State(s, directionFlag='up', parent=self)
            subStates.append(news)
        if 'left' in self.direction and col > 0:  #如果向左移动是合法操作符，
            s = self.state.copy()
            temp = s.copy()
            # 以下两句完成 本节点与左侧节点的交换位置；
            s[row, col] = s[row, col - 1]
            s[row, col - 1] = temp[row, col]
            #根据当前状态生成新的状态子图
            news = State(s, directionFlag='right', parent=self)
            subStates.append(news)

        if self.direction.count('right') and col < boarder:  #如果向下移动是合法操作符，
            s = self.state.copy()
            temp = s.copy()
            s[row, col] = s[row, col + 1]
            s[row, col + 1] = temp[row, col]
            news = State(s, directionFlag='left', parent=self)
            subStates.append(news)
        return subStates


def BFS(init_node, target_state):
    openTable = []
    closedTable = []
    openTable.append(init_node)
    steps =1
    findTarget = False

    while len(openTable) > 0:
        current_node = openTable.pop(0)
        closedTable.append(current_node)
        current_node.printState()
        subStates = current_node.generateSubNodes()
        path = []
        for child in subStates:
            if (child.state == target_state).all():
                findTarget = True
                targetNode = child
                break

        if findTarget == True:
            break
        openTable.extend(subStates)
        steps+=1
    else:
        return None, None
    if findTarget:

        # path.append(targetNode)
        while targetNode.parent :  # 倒序构建当前节点到初始状态的路径；
            path.append(targetNode)
            targetNode = targetNode.parent
        path.append(targetNode) #把根节点加进来；
        path.reverse()  # 列表倒置
        return path, steps + 1

if __name__ == '__main__':
    symbolOfEmpty = 0 # 空格用0表示
    State.symbol = symbolOfEmpty
    #定义初始状态，
    originNode = State(np.array([[2, symbolOfEmpty, 3], [1, 8, 4], [7, 6, 5]]))
    #定义目标状态
    target_state = np.array([[1, 2, 3], [8, State.symbol, 4], [7, 6, 5]])

    s1 = State(state=originNode.state)

    # path, steps = s1.solve()

    print('=' * 10, "宽度优先求解八数码问题，搜索路径是", '=' * 10)
    path, steps = BFS(originNode, target_state)
    if path:
        for node in path:
            # node.showInfo()
            node.printState()

    print("总共搜索步骤是 %d, 解决方案移动步骤是%d" % (steps, len(path)-1))