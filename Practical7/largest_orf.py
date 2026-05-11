seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG' # example RNA sequence
start_codon = 'AUG' # start codon for translation
stop_codons = ['UAA', 'UAG', 'UGA'] # list of stop codons
orf_dirct={} # dictionary to store the positions of start codons and their corresponding stop codons
for i in range(len(seq)-2):
    codon = seq[i:i+3] # extract a codon (3 nucleotides) from the sequence
    if codon == start_codon:
        for j in range(i+3, len(seq)-2, 3): # search for stop codons in the same reading frame
            stop_codon = seq[j:j+3] #   extract a codon to check if it's a stop codon
            if stop_codon in stop_codons:
                orf_dirct[i] = j # store the position of the start codon and the position of the stop codon in the dictionary
                break
if orf_dirct:
    longest_orf=max(orf_dirct.items(), key=lambda x: x[1]) # find the longest ORF by comparing the positions of the stop codons
    print(f"The longest ORF starts at position {longest_orf[0]}")
    print(f"Nucleotide length of the longest ORF: {longest_orf[1]}")
else:
    print("No ORF found in the sequence.")