def reverse_complement(dna_sequence):
    complement = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    dna_sequence = dna_sequence.upper()
    try:
        return ''.join(complement[base] for base in reversed(dna_sequence))
    except KeyError as e:
        raise ValueError(f"Wrong nucleotide in a sequence: {e}")

if __name__ == "__main__":
    dna_seq = input("Enter DNA: ").strip()
    try:
        print(reverse_complement(dna_seq))
    except ValueError as e:
        print(f"Error: {e}")
