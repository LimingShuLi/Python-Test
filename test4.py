user_BMI = float(input("请输入你的BMI值（BMI = 体重/身高的二次方）:"))
if user_BMI < 18.5:
    print("你的身型偏瘦，需要加强营养摄入了")
elif 18.5 <= user_BMI < 25:
    print("你的身型正常")
elif user_BMI >= 25 and user_BMI < 30:
    print("你的身型偏胖")
else :
    print("你的身型肥胖，需要注意饮食节制了")