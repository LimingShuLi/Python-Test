def caculate_sector(central_angle,radius):
    # 括号里为定义的变量
    sector_area = central_angle / 360*3.14*radius**2
    print(f"此扇形面积为: {sector_area:.2f}")
    return sector_area

caculate_sector(90,2)

def caculate_BMI(weight,height):
    BMI = weight / (height * height)
    if BMI < 18.5:
        print("偏瘦")
    elif BMI <= 25:
        print("正常")
    elif BMI <= 30:
        print("偏胖")
    else:
        print("肥胖")
    return BMI
# 也可换为
# def caculate_BMI(weight,height):
#     BMI = weight / (height * height)
#     if BMI < 18.5:
#         category = "偏瘦"
#     elif BMI <= 25:
#         category = "正常"
#     elif BMI <= 30:
#         category = "偏胖"
#     else:
#         category = "肥胖"
#    print(f"您的BMI分类为：{category}")
#    return BMI

caculate_result = caculate_BMI(49,1.75)
print(caculate_result)
