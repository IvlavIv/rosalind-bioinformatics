def count_nucleotides(dna):
    dna = dna.upper()
    return {
        'A': dna.count('A'),
        'C': dna.count('C'),
        'G': dna.count('G'),
        'T': dna.count('T'),
    }

if __name__ == "__main__":
    seq = input("Enter DNA: ").strip()
    counts = count_nucleotides(seq)
    print(counts['A'], counts['C'], counts['G'], counts['T'])
