from Bio import SeqIO

def find_max_gc(fasta_path):
    max_gc = 0
    max_id = None
    for record in SeqIO.parse(fasta_path, "fasta"):
        seq = record.seq.upper()
        gc_content = float(seq.count('G') + seq.count('C')) / len(seq) * 100
        if gc_content > max_gc:
            max_gc = gc_content
            max_id = record.id
    return max_id, max_gc

if __name__ == "__main__":
    fasta_file = input("Enter path: ").strip()
    id_, gc = find_max_gc(fasta_file)
    print(id_)
    print(f"{gc:.6f}")
