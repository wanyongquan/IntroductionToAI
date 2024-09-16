class Dog():
    def __init__(self,name,breed,age):
        """初始化属性name、breed和age"""
        self.name = name
        self.breed = breed
        self.age = age
    def eat(self):
        """小狗正在吃狗粮"""
        print(f"{self.name}正在吃狗粮")
    def run(self):
        """小狗正在奔跑"""
        print(f"{self.name}在奔跑玩耍")


if __name__ == '__main__':
    d1 = Dog("小巴","哈巴狗",4)          #创建实例对象

    print(f"狗狗的姓名是{d1.name}")       #访问name属性
    print(f"狗狗的品种是{d1.breed}")      #访问breed属性
    print(f"狗狗的品种是{d1.age}")        #访问age属性
    d1.eat()
    d1.run()

    d2 = Dog("小柴","柴犬",1)       #创建一个实例对象d2
    print(f"{d2.name}的品种是{d2.breed}，年龄是{d2.age}")
    d2.run()
