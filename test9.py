from ctypes import HRESULT

print("Hellow!我是一个求平均值的程序")
total = 0
count = 0
user_input = input("请输入数字（当你没有要输入的数字时，输入q终止程序）：")
while user_input != "q":
    number = float(user_input)
    total += number# 等于total = totla + number
    count += 1# 等于count = count + number
    user_input = input("请输入数字（当你没有要输入的数字时，输入q终止程序）：")
if count == 0:
   result = 0
else:
    result = total / count
print(str(result))