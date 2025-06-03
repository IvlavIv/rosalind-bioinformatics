def rabbit_population(months, offspring_per_pair):
    mature = 1
    immature = 0
    for _ in range(2, months + 1):
        new_pairs = mature * offspring_per_pair
        mature, immature = mature + immature, new_pairs
    return mature + immature

if __name__ == "__main__":
    n = int(input("Enter the number of months: "))
    k = int(input("Enter the number of offspring for pair: "))
    print(rabbit_population(n, k))
