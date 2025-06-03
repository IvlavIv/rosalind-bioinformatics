def find_peptide_positions(protein, peptide):
    positions = []
    for i in range(len(protein) - len(peptide) + 1):
        if protein[i:i+len(peptide)] == peptide:
            positions.append(i + 1)
    return positions

if __name__ == "__main__":
    protein = input("Enter protein: ").strip()
    peptide = input("Enter peptide: ").strip()
    positions = find_peptide_positions(protein, peptide)
    print(' '.join(map(str, positions)))
