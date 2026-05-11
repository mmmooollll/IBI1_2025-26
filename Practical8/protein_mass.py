# 氨基酸残基平均质量（不含水）
amino_acid_masses = {
    'A': 71.08, 'R': 156.19, 'N': 114.10, 'D': 115.09,
    'C': 103.15, 'E': 129.12, 'Q': 128.13, 'G': 57.05,
    'H': 137.14, 'I': 113.16, 'L': 113.16, 'K': 128.17,
    'M': 131.19, 'F': 147.18, 'P': 97.12, 'S': 87.08,
    'T': 101.11, 'W': 186.21, 'Y': 163.18, 'V': 99.13
}

def calculate_protein_mass(sequence):
    """
    计算蛋白质分子量
    :param sequence: 氨基酸序列字符串（大小写不敏感）
    :return: 蛋白质分子量（float）
    """
    # 转大写
    seq = sequence.upper()
    
    # 输入合法性检查
    for aa in seq:
        if aa not in amino_acid_masses:
            raise ValueError(f"Invalid amino acid: {aa}")
    
    # 计算总质量
    total_mass = sum(amino_acid_masses[aa] for aa in seq)
    # 加上末端水分子质量（18.02）
    total_mass += 18.02
    
    return round(total_mass, 2)

# 示例调用
if __name__ == "__main__":
    test_seq = "MALWMRLLP"
    print(f"Sequence: {test_seq}")
    print(f"Protein mass: {calculate_protein_mass(test_seq)} Da")