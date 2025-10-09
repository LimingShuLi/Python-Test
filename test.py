greet = "Hello!"
greet_english = greet
greet = "你好！"
print(greet_english + "张三")
print(greet + "李四")
print("She said:\"Let's go!\"")

import math# 引入函数库
a = 1
b = 3
c = 2
alpha=b**2 - 4*a*c
print((-b + math.sqrt(alpha) )/2*a)
print((-b - math.sqrt(alpha) )/2*a)
# 这是一行没用的注释
"""这也是一行没用的注释
不对，这有多行"""
print((-b + (alpha)**(1/2) )/2*a)

print(len(" l!\n"))# len函数可以返还字符串的长度
# 注意空格也算一个长度，\n只算一个长度
print("6 l!\n"[0])# 字符索引从零开始
print("6 l!\n"[len(" l!\n") -1])
# type函数可以返还该数据的类型，比如str即为字符串
print(type("Hello"))
print(type(2))
print(type(2.0))
b1=True
b2=False
n=None
print(type(b1))# 布尔类型
print(type(b2))# 布尔类型
print(type(n))# 空值类型
