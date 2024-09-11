# n = input('enter a number:')
# if int(n) % 2 == 0:
#         print('an even number')
#         print('hello')
# else :
#    print('a odd number')
#
# sum =0
# for i in [1,2,3,4,5,6,7,8,9,10]:
#     sum +=i
#
# print(sum)

'''
实战练习1-13 等级分转换
'''
score = input('please input your grade (1-100):')
# score = int(score)
score = int(float(score))
if score < 0 or score > 100:
    print('Invalid score. Please enter a score between 1 and 100.')
elif score < 50:
    print('F')
elif score <= 60:
    print('E')
elif score <= 70:
    print('D')
elif score <= 80:
    print('C')
elif score <= 90:
    print('B')
else:
    print('A')



'''
阶乘
'''
# 从用户获取数字
number = int(input("请输入一个整数数字: "))

# 初始化阶乘结果
factorial = 1

# 计算阶乘
for i in range(1, number + 1):
    factorial *= i

# 输出结果
print(f"{number} 的阶乘是 {factorial}")