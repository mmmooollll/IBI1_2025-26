import numpy as np
import matplotlib.pyplot as plt

gene_dic={
    "TP53": 12.4,
    "EGFR": 15.1,
    "BRCA1": 8.2,
    "PTEN": 5.3,
    "ESR1": 10.7
}
print("initial gene dictionary:")
print(gene_dic)
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