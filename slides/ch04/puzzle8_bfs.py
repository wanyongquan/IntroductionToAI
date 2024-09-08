import numpy as np


class State:
    '''
    状态图算法
    '''
    def __init__(self, state, directionFlag=None, parent=None):
        self.state = state  # 当前状态

        self.direction = ['up', 'down', 'right', 'left']  # 操作符
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

    def getEmptyPos(self):
        #返回空格的位置（索引）
        postion = np.where(self.state == self.symbol)

        return postion

    def generateSubStates(self):
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

    def solve(self):
        openTable = []

        closeTable = []
        openTable.append(self)
        steps = 1


        while len(openTable) > 0:
            n = openTable.pop(0) # 从opentable弹出一个节点进行处理
            closeTable.append(n)   # 把该节点加入ClosedTable
            print(n.state) # 答应当前节点
            print('-'*20)
            subStates = n.generateSubStates()
            path = []
            for s in subStates: #以宽度优先的方式遍历子节点
                if (s.state == s.answer).all():  #找到目标节点
                    while s.parent and s.parent != originState:  # 倒序构建当前节点到初始状态的路径；
                        path.append(s.parent)
                        s = s.parent
                    path.reverse()  # 列表倒置
                    return path, steps + 1
            openTable.extend(subStates)  # 未找到目标节点，把子节点加入到openTable，继续处理openTable中的其他节点。
            steps += 1
        else:
            return None, None


if __name__ == '__main__':
    symbolOfEmpty = 0 # 空格用0表示
    State.symbol = symbolOfEmpty
    #定义初始状态，
    originState = State(np.array([[2, symbolOfEmpty, 3], [1, 8, 4], [7, 6, 5]]))
    #定义目标状态
    State.answer = np.array([[1, 2, 3], [8, State.symbol, 4], [7, 6, 5]])

    s1 = State(state=originState.state)
    path, steps = s1.solve()
    if path:
        for node in path:
            node.showInfo()
    print(State.answer)
    print("Total steps is %d" % steps)
