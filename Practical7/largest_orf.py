seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'
start_codon = 'AUG'
stop_codons = ['UAA', 'UAG', 'UGA']
orf_dirct={}
for i in range(len(seq)-2):
    codon = seq[i:i+3]
    if codon == start_codon:
        for j in range(i+3, len(seq)-2, 3):
            stop_codon = seq[j:j+3]
            if stop_codon in stop_codons:
                orf_dirct[i] = j
                break
if orf_dirct:
    longest_orf=max(orf_dirct.items(), key=lambda x: x[1])
    print(f"The longest ORF starts at position {longest_orf[0]}")
    print(f"Nucleotide length of the longest ORF: {longest_orf[1]}")
else:
    print("No ORF found in the sequence.")