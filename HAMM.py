def hamming_distance(s1, s2):
    if len(s1) != len(s2):
        raise ValueError("Length of the strings must be equal")
    return sum(c1 != c2 for c1, c2 in zip(s1.upper(), s2.upper()))

if __name__ == "__main__":
    s1 = input("First string: ").strip()
    s2 = input("Second string: ").strip()
    print(hamming_distance(s1, s2))
