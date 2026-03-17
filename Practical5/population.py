# 人口数据（百万）
population = {
    "UK": [66.7, 69.2],
    "China": [1426, 1410],
    "Italy": [59.4, 58.9],
    "Brazil": [208.6, 212.0],
    "USA": [331.6, 340.1]
}
# 1. 计算变化百分比
growth = {}
for country, data in population.items():
    pop2020 = data[0]
    pop2024 = data[1]
    change = ((pop2024 - pop2020) / pop2020) * 100
    growth[country] = round(change, 2)

print("各国人口变化率：")
for c, g in growth.items():
    print(c, g, "%")
    # 2. 降序排列
sorted_growth = sorted(growth.items(), key=lambda x:x[1], reverse=True)

print("\n降序排列：")
for country, val in sorted_growth:
    print(country, val)

max_country = sorted_growth[0][0]
min_country = sorted_growth[-1][0]
print("\n增长最大：", max_country)
print("下降最大：", min_country)
import matplotlib.pyplot as plt

countries = [x[0] for x in sorted_growth]
values = [x[1] for x in sorted_growth]

plt.bar(countries, values)
plt.title("Population Change Rate 2020-2024")
plt.ylabel("Change %")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()