def calculate_protein_mass (consequence):
    mass={'G':57.02,
        'A':71.04,
        'S':87.03,
        'P':97.05,
        'V':99.07,
        'T':101.05,
        'C':103.01,
        'I':113.08,
        'L':113.08,
        'N':114.04,
        'D':115.03,
        'Q':128.06,
        'K':128.09,
        'E':129.04,
        'M':131.04,
        'H':137.06,
        'F':147.07,
        'R':156.10,
        'Y':163.06,
        'W':186.08}
    total_mass=0
    for i in consequence:
        if i not in mass:
            return "False"
        total_mass+=mass[i]
    return total_mass   
print(calculate_protein_mass("GAHL"))

class food_item:
    def __init__(self,name,cal, pro, carb, fat):
        self.name=name
        self.cal=cal
        self.pro=pro
        self.carb=carb
        self.fat=fat
apple=food_item("apple",60,0.3,15,0.5)
rice=food_item("rice",130,2.7,28,0.3)
def calculate_total(food_list):
        total_cal = 0
        total_pro = 0
        total_carb = 0
        total_fat = 0

        for food in food_list:
            total_cal += food.cal
            total_pro += food.pro
            total_carb += food.carb
            total_fat += food.fat

        print("总卡路里：", total_cal)
        print("总蛋白：", total_pro)
        print("总碳水：", total_carb)
        print("总脂肪：", total_fat)

    # 警告
        if total_cal > 2500:
         print("警告：卡路里超标！")
        if total_fat > 90:
         print("警告：脂肪超标！")