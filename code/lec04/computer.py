'''
 表示电脑的类，记录电脑和成绩；
'''
import random
class Computer:
    def __init__(self, score=0):
        self.cname = "电脑"                             #玩家的姓名，默认为“电脑”
        self.score = score                              #玩家的得分
        self.level = 0
        
    def play_action(self):             #方法用于打印玩家猜拳的动作
        option = random.randint(1,3)
        print('player action : {0}'.format(option))
        if option == 1:
            print(f"{self.cname}出石头")
        elif option == 2:
            print(f"{self.cname}出剪刀")
        elif option == 3:
            print(f"{self.cname}出布")
        return option