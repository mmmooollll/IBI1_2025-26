start_codons_dna = 'ATG'
stop_codons_dna = ['TAA', 'TAG', 'TGA']
input_fasta = "/Users/mol/Desktop/IBI/IBI1_2025-26/Practical7/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
output_fasta = "/Users/mol/Desktop/IBI/IBI1_2025-26/Practical7/stop_genes.fa"
def read_fasta(fasta_file):
        fasta_dict = {}
        current_header = ''
        current_seq = ''
        with open(fasta_file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()  # 去除换行/空格
                if not line:
                    continue  # 跳过空行
                if line.startswith('>'):
                    # 遇到新基因，保存上一个基因的信息
                    if current_header:
                        fasta_dict[current_header] = current_seq
                    current_header = line
                    current_seq = ''
                else:
                    # 拼接多行序列
                    current_seq += line
        # 保存最后一个基因
        if current_header:
            fasta_dict[current_header] = current_seq
        return fasta_dict

# 执行读取，得到fasta字典
fasta_data = read_fasta(input_fasta)
result_genes = {}

for header, seq in fasta_data.items():
    # 步骤3.1：提取基因名（ENS开头的ID，原标题行第一个空格前的内容）
    gene_name = header.split()[0][1:]  # [1:]去掉开头的>
    # 步骤3.2：寻找序列中的ATG起始位置（多个ATG取第一个，保证读框正确）
    start_pos = seq.find(start_codons_dna)
    if start_pos == -1:
        continue  # 无ATG，跳过
    # 步骤3.3：从ATG后按3步长遍历，寻找读框内的终止密码子
    found_stops = set()  # 存储该基因含有的终止密码子（去重）
    for i in range(start_pos + 3, len(seq) - 2, 3):
        current_codon = seq[i:i+3]
        if current_codon in stop_codons_dna:
            found_stops.add(current_codon)
    # 步骤3.4：仅保留含至少一个终止密码子的基因
    if found_stops:
        # 构造新标题行：>基因名 终止密码子1,终止密码子2...
        new_header = f">{gene_name} {','.join(sorted(found_stops))}"
        result_genes[new_header] = seq
        with open(output_fasta, 'w', encoding='utf-8') as f:
         for header, seq in result_genes.items():
             f.write(f"{header}\n")
             f.write(f"{seq}\n")

print(f"处理完成！符合条件的基因已写入{output_fasta}")
