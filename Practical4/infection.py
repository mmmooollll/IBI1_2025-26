
total_people = 91  # 班级总人数
infected = 5       
growth_rate = 0.4  # 24小时感染增长率（40%）
day = 1            # 初始天数

# 输出第1天数据
print(f"第 {day} 天，感染人数：{infected} 人")

# 循环计算每日感染人数
while infected < total_people:
    # 计算次日感染人数
    infected = infected + infected * growth_rate
    day += 1  # 天数+1
    # 输出当天数据（保留1位小数，更直观）
    print(f"第 {day} 天，感染人数：{infected:.1f} 人")

# 循环结束，输出总天数
print(f"\n全部 {total_people} 人被感染，总共用了 {day} 天")