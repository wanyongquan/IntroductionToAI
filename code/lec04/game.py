from player import Player
from computer import Computer        #从game模块中导入Player类
p1 = Player("张三")                   #创建Player类的实例对象
print(p1.name)                  #访问实例属性
p1.play_action()              #访问实例方法
c1 = Computer()                      #创建Computer类的实例对象
print(c1.cname)
c1.play_action()

'''
学有余力的同学可以写一个人机猜拳的游戏；
'''
