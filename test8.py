for i in range(1,10,2):
# range表示整数数列，三个数字依次为起始值，结束值，步长
    print(i)

total = 0
for i in range(1,101):
    total  = total+i
    print(total)

temperature_dict = {"1":36.4,"2":36.6,"3":36.6,"4":36.7,"5":38.6,"6":36.6,"7":36.6,"8":37.2,"9":36.6,"10":36.6}
for staff_id,temperature in temperature_dict.items():
    if temperature >= 37.5:
        print(staff_id)
for temperature in temperature_dict.values():
    if temperature >= 37.5:
        print(temperature)
for staff_id in temperature_dict.keys():
    if int(staff_id)>9:
        print(staff_id)