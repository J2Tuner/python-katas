def to_rna(dna):
    dna = dna.upper()
    rna = ''
    for i in range(len(dna)):
        if dna[i] == 'G':
            rna += 'C'
        elif dna[i] == 'C':
            rna += 'G'
        elif dna[i] == 'T':
            rna += 'A'
        elif dna[i] == 'A':
            rna += 'U'
        else:
            return ''

    return rna
