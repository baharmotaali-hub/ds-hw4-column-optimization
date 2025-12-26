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

    base_map = {}

    for x, y, z, idx in blocks:
        if z > best_diameter:
            best_diameter = z
            best_blocks = [idx]

        key = (x, y)
        if key not in base_map:
            base_map[key] = []
        base_map[key].append((z, idx))

    for (x, y), lst in base_map.items():
        if len(lst) < 2:
            continue

        lst.sort(reverse=True)

        z1, i1 = lst[0]
        z2, i2 = lst[1]

        combined_height = z1 + z2
        diameter = min(y, combined_height)

        if diameter > best_diameter:
            best_diameter = diameter
            best_blocks = sorted([i1, i2])

    with open("output.txt", "w") as f:
        f.write(str(len(best_blocks)) + "\n")
        f.write(" ".join(map(str, best_blocks)) + "\n")
        f.write(str(best_diameter) + "\n")


if __name__ == "__main__":
    main()
