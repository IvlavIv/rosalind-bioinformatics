from Bio import SeqIO

if __name__ == "__main__":
    gbk_file = input("Enter GenBank path: ").strip()
    for record in SeqIO.parse(gbk_file, "genbank"):
        print(f"ID: {record.id}")
        print(f"Description: {record.description}")
        print(f"Annotation: {record.annotations.get('comment', 'no comments')}")
