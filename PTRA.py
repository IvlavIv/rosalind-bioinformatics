from Bio.Seq import Seq

def reverse_complement(dna):
    return str(Seq(dna).reverse_complement())

def translate_rna(rna):
    return str(Seq(rna).translate(to_stop=True))

def find_peptide_in_dna(dna, peptide):
    positions = []
    dna = dna.upper()
    pep_len = len(peptide)
    for strand, seq in [(+1, dna), (-1, reverse_complement(dna))]:
        for i in range(len(dna) - pep_len*3 + 1):
            codon_seq = seq[i:i+pep_len*3].replace('T', 'U')
            protein = translate_rna(codon_seq)
            if protein == peptide:
                if strand == 1:
                    positions.append(i+1)
                else:
                    positions.append(-(i+1))
    return positions

if __name__ == "__main__":
    dna_seq = input("Enter DNA: ").strip()
    peptide = input("Enter peptide: ").strip()
    pos = find_peptide_in_dna(dna_seq, peptide)
    print(' '.join(map(str, pos)))
