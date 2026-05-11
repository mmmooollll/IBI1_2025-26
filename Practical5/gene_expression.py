import numpy as np
import matplotlib.pyplot as plt
activity=1.0
gene_dic={
    "TP53": 12.4,
    "EGFR": 15.1,
    "BRCA1": 8.2,
    "PTEN": 5.3,
    "ESR1": 10.7
}
# 2. 无效输入检查（activity必须是正数）
if not isinstance(activity, (int, float)) or activity <= 0:
    raise ValueError("activity must be a positive number (e.g., 0.5, 1.0, 1.5)")

# 根据activity计算最终表达值
final_expression = {gene: base * activity for gene, base in gene_dic.items()}

print("Initial gene dictionary (base expression):")
print(gene_dic)

print(f"\nFinal gene expression (activity = {activity}):")
print(final_expression)

gene_dic["MYC"]=11.6
print ("final dictionary:")
print(gene_dic)

genes= list (gene_dic.keys())
value= list(gene_dic.values())

plt.bar(genes, value)
plt.title("Gene Expression")
plt.xlabel("Genes")
plt.ylabel("Expression Value")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()