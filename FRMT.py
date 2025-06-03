from Bio import SeqIO

def format_fasta(input_file, output_file, line_length=60):
    with open(output_file, 'w') as out_handle:
        for record in SeqIO.parse(input_file, 'fasta'):
            SeqIO.write(record, out_handle, 'fasta')

if __name__ == "__main__":
    in_file = input("Input fasta path").strip()
    out_file = input("Output fasts path").strip()
    format_fasta(in_file, out_file)
    print("Completed")
