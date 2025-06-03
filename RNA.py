def transcribe_dna_to_rna(dna):
    return dna.upper().replace('T', 'U')

if __name__ == "__main__":
    dna = input("Введите ДНК: ").strip()
    print(transcribe_dna_to_rna(dna))
