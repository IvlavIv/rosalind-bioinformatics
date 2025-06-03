from Bio.Seq import Seq

DNA = "..."
my_DNA = Seq(DNA)
reversed_complement_DNA = str(my_DNA.reverse_complement())
list_of_orfs = []

#Helps to create all posible frames
frames = [
    [DNA[i:i + 3] for i in range(frame, len(DNA) - 2, 3)]
    for frame in range(3)
] + [
    [reversed_complement_DNA[i:i + 3] for i in range(frame, len(reversed_complement_DNA) - 2, 3)]
    for frame in range(3)
]

start_codons = "ATG"
stop_codons = {"TAA", "TAG", "TGA"}

for frame in frames:
    start = 0
    while start < len(frame):
        if frame[start] in start_codons:
            for stop in range(start + 1, len(frame)):
                if frame[stop] in stop_codons:
                    list_of_orfs.append(frame[start:stop + 1])
                    start = stop + 1
                    break
            else:
                start += 1
        else:
            start += 1
if list_of_orfs:
    max_orf = max(list_of_orfs, key=len)
    my_max_orf = Seq("".join(max_orf))
    print(my_max_orf.translate(to_stop=True))
else:
    print("No ORFs found.")
