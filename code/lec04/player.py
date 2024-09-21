'''
 表示玩家的类，记录玩家的名字和成绩；
'''
import random
class Player:
    def __init__(self,name = None, score=0):
        self.name = "玩家"                             #玩家的姓名，默认为“玩家”
        self.score = score                              #玩家的得分
        
    def play_action(self ):             #方法用于打印玩家猜拳的动作
        option = random.randint(1,3)
        print('player action : {0}'.format(option))
        
        if option == 1:
            print(f"{self.name}出石头")
        elif option == 2:
            print(f"{self.name}出剪刀")
        elif option == 3:
            print(f"{self.name}出布")
        return option