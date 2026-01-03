TABLE_SIZE = 200003

hash_table = [None] * TABLE_SIZE


def hash_func(x, y):
    return (x * 1000003 + y) % TABLE_SIZE


def insert(x, y, z, idx):
    h = hash_func(x, y)
    while True:
        if hash_table[h] is None:
            hash_table[h] = [x, y, [(z, idx)]]
            return
        if hash_table[h][0] == x and hash_table[h][1] == y:
            hash_table[h][2].append((z, idx))
            return
        h = (h + 1) % TABLE_SIZE


def main():
    with open("input.txt", "r") as f:
        n = int(f.readline().strip())
        blocks = []
        for i in range(n):
            dims = list(map(int, f.readline().split()))
            dims.sort(reverse=True)
            x, y, z = dims
            blocks.append((x, y, z, i + 1))

    best_diameter = 0
    best_blocks = []

    for x, y, z, idx in blocks:
        if z > best_diameter:
            best_diameter = z
            best_blocks = [idx]
        insert(x, y, z, idx)

    for entry in hash_table:
        if entry is None:
            continue
        x, y, lst = entry
        if len(lst) < 2:
            continue
        lst.sort(reverse=True)
        z1, i1 = lst[0]
        z2, i2 = lst[1]
        diameter = min(y, z1 + z2)
        if diameter > best_diameter:
            best_diameter = diameter
            best_blocks = sorted([i1, i2])

    with open("output.txt", "w") as f:
        f.write(str(len(best_blocks)) + "\n")
        f.write(" ".join(map(str, best_blocks)) + "\n")
        f.write(str(best_diameter) + "\n")


if __name__ == "__main__":
    main()
