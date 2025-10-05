shopping_list = ["风之旅人","黑神话：悟空"]#列表
shopping_list.append("最终幻想VII")
shopping_list.append("GRIS")
shopping_list.remove("风之旅人")
shopping_list[1] = "崩坏大陆"#直接顶替

print(shopping_list)
print(len(shopping_list))
print(shopping_list[0])#查找对应顺序上的游戏
print(shopping_list[1])

price = [268,10,11]
max_price = max(price)
min_price = min(price)
sortef_price = sorted(price)
print(max_price)
print(min_price)
print(sortef_price)
