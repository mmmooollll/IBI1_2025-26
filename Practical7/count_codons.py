start_codons_dna = 'ATG'
stop_codons_dna = ['TAA', 'TAG', 'TGA']
import matplotlib.pyplot as plt
# 设置matplotlib中文显示（避免饼图标注乱码）
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
input_fasta = "Practical7/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
piechart_output = 'codon_distribution.png'
# 复制FASTA读取函数和stop_codons.py中的完全一致
def read_fasta(fasta_file):
    fasta_dict = {}
    current_header = ''
    current_seq = ''
    with open(fasta_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.startswith('>'):
                if current_header:
                    fasta_dict[current_header] = current_seq
                current_header = line
                current_seq = ''
            else:
                current_seq += line
        if current_header:
            fasta_dict[current_header] = current_seq
    return fasta_dict

# 步骤2.1：用户输入并校验
user_stop = input("请输入终止密码子（仅支持TAA/TAG/TGA）：").strip().upper()
if user_stop not in stop_codons_dna:
    print("输入错误！仅允许输入TAA、TAG、TGA中的一种。")
    exit()  # 输入错误，退出程序

# 步骤2.2：读取FASTA文件
fasta_data = read_fasta(input_fasta)
# 存储所有符合条件的上游密码子
all_upstream_codons = []

for header, seq in fasta_data.items():
    # 步骤3.1：找第一个ATG起始位置，无则跳过
    start_pos = seq.find(start_codons_dna)
    if start_pos == -1:
        continue
    # 步骤3.2：读框内找所有目标终止密码子的位置，存入列表
    target_stop_positions = []
    for i in range(start_pos + 3, len(seq) - 2, 3):
        if seq[i:i+3] == user_stop:
            target_stop_positions.append(i)
    if not target_stop_positions:
        continue  # 无目标终止密码子，跳过
    # 步骤3.3：计算每个终止密码子对应的ORF长度，取最长的那个终止位置
    # ORF长度：从ATG到终止密码子的最后一个字符
    stop_len_dict = {}
    for stop_pos in target_stop_positions:
        orf_len = stop_pos + 3 - start_pos
        stop_len_dict[stop_pos] = orf_len
    longest_stop_pos = max(stop_len_dict.items(), key=lambda x: x[1])[0]
    # 步骤3.4：提取该终止密码子上游的所有读框内密码子（ATG到终止前）
    for i in range(start_pos, longest_stop_pos, 3):
        codon = seq[i:i+3]
        all_upstream_codons.append(codon)
        # 步骤4.1：统计密码子频率
codon_count = {}
for codon in all_upstream_codons:
    codon_count[codon] = codon_count.get(codon, 0) + 1

# 步骤4.2：输出统计结果
print(f"===== 终止密码子{user_stop}上游密码子统计结果 =====")
for codon, count in sorted(codon_count.items(), key=lambda x: x[1], reverse=True):
    print(f"{codon}: {count}次")
if not codon_count:
    print(f"未找到含{user_stop}的基因，无统计结果")
    exit()
    # 步骤5.1：拆分密码子和数量为列表
codons = list(codon_count.keys())
counts = list(codon_count.values())

# 步骤5.2：绘制饼图
fig, ax = plt.subplots(figsize=(12, 8))  # 设置饼图大小
# 画饼图：autopct显示占比，startangle设置起始角度，wedgeprops设置饼图间距
wedges, texts, autotexts = ax.pie(counts, labels=codons, autopct='%1.1f%%',
                                  startangle=90, wedgeprops=dict(width=0.6))
# 设置饼图标题
ax.set_title(f'终止密码子{user_stop}上游读框内密码子分布', fontsize=16, pad=20)
# 设置标签和占比的字体大小
for text in texts:
    text.set_fontsize(8)
for autotext in autotexts:
    autotext.set_fontsize(6)
    autotext.set_color('white')
    autotext.set_weight('bold')
# 步骤5.3：保存饼图到文件，关闭画布（避免屏幕显示）
plt.tight_layout()
plt.savefig(piechart_output, dpi=300, bbox_inches='tight')
plt.show()  # 显示饼图
plt.close()

print(f"饼图已保存为{piechart_output}")