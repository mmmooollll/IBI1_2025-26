# pseudocode
# 1. store the value of a person's age, weight, gender and creatine concentration
# 2.check that the input value are within the correct range
#    - age：< 100；20kg < weight < 80kg
#    - Cr：0 < Cr < 100 µmol/l；gender：仅male/female
# 3. If	one	of these conditions is	not met, do	not	report CrCl but	instead	which input	variable needs corrected.
# 4. if all meet, calculate the CrCl（female*0.85)
# 5. output the CrCl that have been calculated
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
