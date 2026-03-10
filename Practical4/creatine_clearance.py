# fake code：
# 1. 定义变量存储用户数据：年龄age、体重weight、性别gender、肌酸浓度Cr
# 2. 输入校验：判断各变量是否在合法范围
#    - 年龄：< 100岁；体重：20kg < weight < 80kg
#    - 肌酸浓度：0 < Cr < 100 µmol/l；性别：仅male/female
# 3. 若校验不通过：输出提示，说明哪个变量需要修正，不计算CrCl
# 4. 若校验通过：根据性别计算CrCl（女性乘0.85，男性不乘）
# 5. 输出计算得到的CrCl值
age = int(input("age："))
weight = float(input("weight："))
gender =input("（male/female）：").lower()
Cr = float(input("Cr："))
is_valid=True
error_msg=""
if age>=100:
    is_valid=False
    error_msg='your age should be smaller than 100'
elif weight>=80 or weight<=20:
    is_valid=False
    error_msg="your weight should be between 20 to 100"
elif Cr <= 0 or Cr >= 100:
    is_valid = False
    error_msg = "Cr should be between 0 to 100"
elif gender not in ["male", "female"]:
    is_valid = False
    error_msg = "your gender should be male/female"
if is_valid:
    crcl = ((140 - age) * weight) / (72 * Cr)
    if gender == "female":
        crcl = crcl * 0.85
        print(f"CrCl：{crcl:.2f} ml/min")
else:
    print(f"incorrect input：{error_msg}")
