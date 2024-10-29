#鸢尾花识别
#根据鸢尾花的花瓣长度宽度，花萼长度宽度，以及对应的鸢尾花类别


#1.导入iris数据集
from sklearn import datasets

iris = datasets.load_iris()

#输出数据集规模
print(iris.data.shape)

#输出数据集介绍
#由数据描述可知，iris数据集中共有150个鸢尾花，每朵花都有四个特征值，并均匀分布在3个不同的亚种。
print(iris.DESCR)

X=iris.data
y=iris.target
print(X,y)

#2.数据集分割
# 将数据分为训练集和测试集，比例为70%  30%
from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3)

#3.训练模型
#设置k为3
from sklearn.neighbors import  KNeighborsClassifier

kNN = KNeighborsClassifier(n_neighbors=3)
kNN.fit(X_train,y_train)

#4.预测，输出正确率
kNN.predict(X_test)
print ('Accuracy of kNN:',kNN.score(X_test,y_test))

#5.针对新数据集进行预测

#类别名称
myclass = ["Iris-Setosa","Iris-Versicolour","Iris-Virginica"]

X_newtest = [[5.1,3.5,1.3,0.2],[6.2,3.4,5.3,2.2],[5.5,2.5,4.0,1.3]]
y_newtest = kNN.predict(X_newtest)

#输出预测结果
print("my predict result:")
for i in range(len(X_newtest)):
    print(X_newtest[i],":",myclass[y_newtest[i]])















