import os # 导入os模块以处理文件路径
import pandas as pd # 导入pandas库以处理数据
import matplotlib.pyplot as plt     # 导入matplotlib库以进行数据可视化
import numpy as np # 导入numpy库以进行数值计算
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv") # 读取CSV文件并将其存储在dalys_data变量中
print(dalys_data.head())
# 任务2：筛选津巴布韦的所有数据
zimbabwe = dalys_data.loc[dalys_data['Entity'] == 'Zimbabwe'] # 使用loc方法筛选出Entity列中值为'Zimbabwe'的行，并将结果存储在zimbabwe变量中
print("\n津巴布韦所有年份的DALYs数据：") 
print(zimbabwe[['Year', 'DALYs']]) # 打印出津巴布韦所有年份的DALYs数据，选择Year和DALYs两列进行显示
# 找出津巴布韦数据的最早和最晚年份
first_year = zimbabwe['Year'].min()
last_year = zimbabwe['Year'].max()
print("\n津巴布韦数据的起始年份：", first_year)
print("津巴布韦数据的结束年份：", last_year)
# 任务3：筛选2019年所有国家的数据
data_2019 = dalys_data.loc[dalys_data['Year'] == 2019] # 使用loc方法筛选出Year列中值为2019的行，并将结果存储在data_2019变量中
# 找出DALYs最高的国家
max_country = data_2019.loc[data_2019['DALYs'].idxmax(), 'Entity'] # 使用idxmax()方法找出DALYs列中的最大值的索引，然后使用loc方法获取对应的Entity值
# 找出DALYs最低的国家
min_country = data_2019.loc[data_2019['DALYs'].idxmin(), 'Entity'] # 使用idxmin()方法找出DALYs列中的最小值的索引，然后使用loc方法获取对应的Entity值
print("\n2019年DALYs最高的国家：", max_country)
print("2019年DALYs最低的国家：", min_country)
# 任务4：绘制2019年DALYs的柱状图
plt.figure(figsize=(12, 6)) # 设置图形的大小
plt.bar(data_2019['Entity'], data_2019['DALYs'], color='skyblue') # 绘制柱状图，x轴为国家名称，y轴为DALYs值，柱子的颜色为天蓝色
plt.xlabel('Country') # 设置x轴标签
plt.ylabel('DALYs') # 设置y轴标签
plt.title('DALYs by Country in 2019') # 设置图表标题
plt.xticks(rotation=90) # 将x轴的标签旋转90度以便更好地显示
plt.tight_layout() # 调整图表布局以防止标签重叠
plt.show() # 显示图表   

asia = ['China', 'India', 'Afghanistan', 'Japan']
europe = ['Switzerland', 'Germany', 'France', 'United Kingdom']
africa = ['Zimbabwe', 'Nigeria', 'Kenya', 'South Africa']
# 筛选2019年数据
data_2019 = dalys_data[dalys_data['Year'] == 2019]
# 计算各洲平均值
asia_mean = data_2019[data_2019['Entity'].isin(asia)]['DALYs'].mean()
europe_mean = data_2019[data_2019['Entity'].isin(europe)]['DALYs'].mean()
africa_mean = data_2019[data_2019['Entity'].isin(africa)]['DALYs'].mean()

print(f"亚洲平均：{asia_mean:.2f}")
print(f"欧洲平均：{europe_mean:.2f}")
print(f"非洲平均：{africa_mean:.2f}")





