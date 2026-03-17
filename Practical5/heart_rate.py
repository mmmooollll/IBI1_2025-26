# 心率数据
heart_rates = [72, 60, 126, 85, 90, 59, 76, 131, 88, 121, 64]

count = len(heart_rates)
avg_hr = sum(heart_rates) / count

print(f"患者总数：{count}")
print(f"平均心率：{avg_hr:.2f}")

low = 0
normal = 0
high = 0

for hr in heart_rates:
    if hr < 60:
        low +=1
    elif hr > 120:
        high +=1
    else:
        normal +=1

print("\n心率分类统计：")
print("偏低：", low)
print("正常：", normal)
print("偏高：", high)


categories = {"偏低":low, "正常":normal, "偏高":high}
max_category = max(categories, key=categories.get)
print("数量最多的类别：", max_category)
import matplotlib.pyplot as plt

# 3. 绘制饼图
labels = ["Low", "Normal", "High"]
sizes = [low, normal, high]
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Heart Rate Distribution")
plt.show()