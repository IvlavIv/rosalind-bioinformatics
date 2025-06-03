from Bio import SeqIO

if __name__ == "__main__":
    fasta_file = input("Enter path: ").strip()
    records = list(SeqIO.parse(fasta_file, "fasta"))
    if not records:
        print("Файл пуст или неверный формат")
    else:
        print(records[0].id)
        print(records[0].seq)
        print(records[-1].id)
        print(records[-1].seq)
