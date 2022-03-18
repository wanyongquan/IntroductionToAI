'''
深度优先算法求解八数码问题；
'''
import numpy as np


class State:
    '''
    状态图
    '''
    def __init__(self, state, directionFlag=None, parent=None):
        self.state = state  # 当前状态
        self.depth = parent.depth+1 if parent is not None else 1
        self.boarder = len(self.state) - 1 # 在八数码问题中，该值等于2，即九空格行索引的上界。

        self.direction = ['left', 'up', 'right',  'down']  # 操作符
        self.operation_index = 0 # 下一个可用的算符；
        if directionFlag:  # 被禁止的操作符（如果使用该操作符，会回到父亲节点，导致死循环）
            self.direction.remove(directionFlag)
        self.parent = parent  # 父节点
        self.symbol = 0  # 空格

    def getDirection(self):
        return self.direction

    def getNextOperation(self, operation_index):

        if operation_index >= len(self.direction): #合法的算符索引
            return None
        else :
            row, col = self.getEmptyPos()
            next_operation = self.direction[operation_index]
            if 'up' == next_operation and row > 0:

                return next_operation
            elif 'down' == next_operation and row < self.boarder:  # 如果向右移动是合法操作符，

                return next_operation
            elif 'left' == next_operation and col > 0:  # 如果向左移动是合法操作符，

                return next_operation
            elif 'right' == next_operation and col < self.boarder:  #如果向下移动是合法操作符，

                return next_operation

    def hasAvailableChild(self):
        # 是否还有子节点未扩展；
        return self.operation_index< len(self.direction)

    def getChildLength(self):
        return len(self.direction)

    def showInfo(self):
        for i in range(3):
            for j in range(3):
                print(self.state[i, j], end=' ')
            print("\n")

        print('->\n')


    def printState(self):
        print('当前节点的深度：', self.depth)
        print(self.state)
        print('*'*20,'\n')

    def getEmptyPos(self):
        #返回空格的位置（索引）
        postion = np.where(self.state == self.symbol)

        return postion

    def generateNextChildNode(self, index):
        '''
        根据余弦设定的操作符顺序扩展子节点
        :return: 子节点列表
        '''
        if not self.direction:
            return []


        next_operation = self.getNextOperation(index)

        if next_operation is None :
            return None
        subStates = []  # 子节点列表
        boarder = len(self.state) - 1 # 在八数码问题中，该值等于2，即九空格行索引的上界。
        row, col = self.getEmptyPos()
        #以下代码规定了 操作符的处理顺序为 up , down, left, right,

        if 'up' == next_operation and row > 0:  #如果向上移动是合法操作符，
            s = self.state.copy()
            temp = s.copy()
            s[row, col] = s[row - 1, col]
            s[row - 1, col] = temp[row, col]
            new_state = State(s, directionFlag='down', parent=self)
            # subStates.append(news)
            return new_state
        if 'down' == next_operation and row < boarder:  #如果向右移动是合法操作符，
            s = self.state.copy()
            temp = s.copy()
            s[row, col] = s[row + 1, col]
            s[row + 1, col] = temp[row, col]
            new_state = State(s, directionFlag='up', parent=self)
            # subStates.append(news)
            return new_state
        if 'left' == next_operation and col > 0:  #如果向左移动是合法操作符，
            s = self.state.copy()
            temp = s.copy()
            # 以下两句完成 本节点与左侧节点的交换位置；
            s[row, col] = s[row, col - 1]
            s[row, col - 1] = temp[row, col]
            #根据当前状态生成新的状态子图
            new_state = State(s, directionFlag='right', parent=self)
            # subStates.append(news)
            return new_state
        if 'right' == next_operation and col < boarder:  #如果向下移动是合法操作符，
            s = self.state.copy()
            temp = s.copy()
            s[row, col] = s[row, col + 1]
            s[row, col + 1] = temp[row, col]
            new_state = State(s, directionFlag='left', parent=self)
            # subStates.append(news)
            return new_state
        # return subStates

    def DFS_Search(self, target_state, deepthLimit):
        '''
        判断当前节点是否是目标节点
        :return: 返回目标节点 if reach target, otherwise False
        '''
        # 加上深度限制；
        if self.depth >= deepthLimit + 1 :
            return None

        print('当前状态：')
        self.printState()
        global searchSteps
        searchSteps += 1

        if (self.state == target_state).all():
            return self
        else:

            for idx in range(self.getChildLength()):
                # openTable.append(child)
                child = self.generateNextChildNode(idx)
                if child is None: # 不合法的算符不会扩展出节点；
                    continue

                findTarget =  child.DFS_Search(target_state, deepthLimit)
                # 如果当前子节点的扩展字数到达目标，则返回；否则继续for循环，遍历下一个子节点；
                if findTarget is not None :
                    return findTarget


def DFS(init_node, target_state, deepthLimit = 6):
    # openTable = []
    # closedTable = []
    # openTable.append(init_node)
    steps =0


    targetNode = init_node.DFS_Search(target_state, deepthLimit)
    if targetNode is None:
        print('没有找到解')
        return None, None
    else:
        # 打印搜索搜索路径；
        path = []
        while targetNode.parent :  # 倒序构建当前节点到初始状态的路径；
            path.append(targetNode)
            steps +=1
            targetNode = targetNode.parent
        path.append(targetNode)
        path.reverse()  # 列表倒置


    return path, steps + 1

if __name__ == '__main__':
    symbolOfEmpty = 0 # 空格用0表示
    State.symbol = symbolOfEmpty
    #定义初始状态，
    originNode = State(np.array([[2, 8, 3], [1, 6, 4], [7, symbolOfEmpty, 5]]))
    #定义目标状态
    target_state = np.array([[1, 2, 3], [8, State.symbol, 4], [7, 6, 5]])

    s1 = State(state=originNode.state)

    # path, steps = s1.solve()
    print("深度优先算法求解八数码问题")

    searchSteps = 0
    path, steps = DFS(originNode, target_state, deepthLimit = 5)
    print("深度优先算法求解八数码问题，解决方案的移动路径是：")
    if path:
        for node in path:
            node.printState()

    print("搜索步骤是 %d, 解决方案移动步骤是 %d" % ( searchSteps, steps-1))