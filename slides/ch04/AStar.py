'''
A*算法求解八数码问题, 以不在目标位置到的数字的数量为h(x)
'''
import numpy as np


class StateNode :
    '''
    状态图
    '''
    def __init__(self, state_data, symbol = 0, parent = None, invalidDirect= None):
        self.state_data = state_data
        self.parent = parent
        self.depth = parent.depth  +1 if parent is not None else 1
        self.boarder = len(self.state_data) -1 # 行和列索引的边界值
        self.symbol = symbol
        self.direction = ['left', 'up', 'right', 'down']
        self.operation_index = 0
        if invalidDirect :
            self.direction.remove(invalidDirect)

        self.G = 0
        self.H = 0
        self.F = self.G + self.H

    def getParent(self):
        return self.parent

    def setParent(self, parent):
        self.parent = parent

    def getEmptyPos(self):
        #返回空格的位置（索引）
        postion = np.where(self.state_data == self.symbol)

        return postion

    def get_G(self):
        return self.G


    def get_F(self, target_state):
        return self.get_G() + self.set_H(target_state)

    def getDirection(self):
        return self.direction

    def set_G(self, value):
        self.G = value

    def set_H(self, targetStateNode):
        '''
        计算当前状态与目标状态的9空格各个位置上不相同数字的数量；
        :param targetStateNode:
        :return:
        '''
        # 比较两个矩阵的不相同元素
        diff = np.argwhere(self.state_data != targetStateNode.state_data)
        self.H = len(diff)

    def get_H(self):
        return self.H

    def set_F(self, targetNode):
        self.set_H(targetNode)
        self.F = self.get_G() + self.get_H()


    def get_F(self):
        return self.F


    def generateSubNodes(self):
        '''
        根据预先设定的操作符顺序扩展子节点
        :return: 子节点列表
        '''
        if not self.direction:
            return []

        subStates = []  # 子节点列表
        boarder = len(self.state_data) - 1 # 在八数码问题中，该值等于2，即九空格行索引的上界。
        row, col = self.getEmptyPos()
        #以下代码规定了 操作符的处理顺序为 up , down, left, right,
        if 'up' in self.direction and row > 0:  #如果向上移动是合法操作符，
            s = self.state_data.copy()
            temp = s.copy()
            s[row, col] = s[row - 1, col]
            s[row - 1, col] = temp[row, col]
            news = StateNode(s, parent=self, invalidDirect='down')
            subStates.append(news)
        if 'down' in self.direction and row < boarder:  #如果向右移动是合法操作符，
            s = self.state_data.copy()
            temp = s.copy()
            s[row, col] = s[row + 1, col]
            s[row + 1, col] = temp[row, col]
            news = StateNode(s, parent=self, invalidDirect='up')
            subStates.append(news)
        if 'left' in self.direction and col > 0:  #如果向左移动是合法操作符，
            s = self.state_data.copy()
            temp = s.copy()
            # 以下两句完成 本节点与左侧节点的交换位置；
            s[row, col] = s[row, col - 1]
            s[row, col - 1] = temp[row, col]
            #根据当前状态生成新的状态子图
            news = StateNode(s, parent=self, invalidDirect='right')
            subStates.append(news)

        if self.direction.count('right') and col < boarder:  #如果向下移动是合法操作符，
            s = self.state_data.copy()
            temp = s.copy()
            s[row, col] = s[row, col + 1]
            s[row, col + 1] = temp[row, col]
            news = StateNode(s, parent=self, invalidDirect='left')
            subStates.append(news)
        return subStates

    def get_identity(self):
        identity = ''
        for row in range(3):
            for col in range(3):
                identity += str(self.state_data[row, col])
        return identity

    def printState(self):

        print(self.state_data)
        print('当前节点的深度：{}, 代价 F= G+ H （{} = {} + {}） '.format( self.depth, self.get_F(), self.get_G(),self.get_H()))
        print('*' * 20, '\n')


def is_node_in_table(state_node, list ):
    # 判断节点是否已在列表中；
    for item in list:
        if (item.state_data == state_node.state_data).all():
            return True
    return False


def AStart(init_node, target_node):
    openTable = []  # 存放待搜索的节点
    closedTable = [] # 存放已搜索的节点


    findTarget = False
    steps=0
    # 第一步： # 节点加入Open表

    init_node.set_F(target_state)
    openTable.append(init_node)

    # 第二步： 重复以下过程，若open表为空则算法失败；
    while len(openTable) >0:
        # 第三步： 取出当前open表的F值最小节点作为当前最优节点，继续进行下一步处理，并把其放入到closed表
        openTable.sort(key=lambda x: x.get_F())
        curr_node = openTable.pop(0)
        closedTable.append(curr_node)
        steps += 1
        curr_node.printState()

        # 第四步: 判断是否是目标状态，若是， 成功得到一个解；
        if (curr_node.state_data == target_state.state_data).all():
            findTarget = True
            break
        else:
            # 第5步： 若不是目标状态，则 根据 算符优先规则， 为该节点扩展子节点，产生后续待处理节点；
            substates = curr_node.generateSubNodes()
            # 第6步： 对待处理节点，进行下列过程：
            for child in substates:
                # 6-a建立 child 和curr_node之间的父子关系
                child.setParent(curr_node)
                # 6-b更新计算child的G值： child.G = curr.G + g(curr, child)
                child.set_G(curr_node.get_G() + 1)
                # 6-c # 检查child节点是否已在open表中，若是，则称其为old， 并把它加到curr的后继节点中
                if is_node_in_table(child, openTable):
                    old = openTable[openTable.index(child)]
                    # 6-d 比较新旧两条路径的代价。 如果g(child) < g(old) ，则重新确定old的父节点为curr_node。
                    # 记下较小的代价g(old)，更新f(old)值
                    if child.get_G() < old.get_G():
                        old.setParent(curr_node)
                        old.set_G(child.get_G())
                    else:
                        # 6-e 若到old节点的代价更低或相同，则停止扩展该节点
                        pass

                elif is_node_in_table(child , closedTable):#  6-f 检查该子节点是否已在close的表中，
                    # 6-g 在closed表中，比较新旧路径代价； 如果 g(child) < g(old) ,则重新确立old的父节点为curr_node,
                    # 记下较小的g(old) ，更新f(old), 将old从closed表移出，重新放入open表
                    old = closedTable[closedTable.index(child)]
                    if child.get_G() < old.get_G():
                        old.setParent(curr_node)
                        old.set_G(child.get_G())
                        closedTable.pop(old) # 从closed表移出， 重新加入Open表
                        openTable.append(old)
                else:
                    # 6-h 既不在open表，也不在closed表， 把它放入open表，添加为curr_node的子节点，转到第7步
                    openTable.append(child)

                # 第7步, 计算f值
                child.set_F(target_node)

    # 从当前节点逆序构建搜索路径
    if findTarget:
        path = []
        # path.append(targetNode)
        while curr_node.parent :  # 倒序构建当前节点到初始状态的路径；
            path.append(curr_node)
            curr_node = curr_node.parent
        path.append(curr_node) #把根节点加进来；
        path.reverse()  # 列表倒置

        return path, steps

if __name__ == '__main__':
    symbolOfEmpty = 0  # 空格用0表示

    # 定义初始状态，
    s1 = StateNode(np.array([[2, symbolOfEmpty, 3], [1, 8, 4], [7, 6, 5]]))
    # 定义目标状态
    target_state = StateNode(np.array([[1, 2, 3], [8, symbolOfEmpty, 4], [7, 6, 5]]))



    # path, steps = s1.solve()
    print("A* 算法 （宽度优先）求解八数码问题")
    # 初始化当前节点的G和H
    s1.set_G(0)
    s1.set_H(target_state)
    print('=' * 10, "宽度优先求解八数码问题，搜索过程是", '=' * 10)
    path, steps = AStart(s1, target_state)
    print("求解路径: ")
    if path:
        for node in path:
            # node.showInfo()
            node.printState()

    print("总共搜索步骤是 %d, 解决方案移动步骤是%d" % (steps, len(path)-1))




