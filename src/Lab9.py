def count_paths(grid):
    h = len(grid)
    w = len(grid[0]) if h > 0 else 0

    if h == 0 or w == 0:
        return 0

    prev = [1] * h
    letter_sum = {}

    for r in range(h):
        letter = grid[r][0]
        letter_sum[letter] = letter_sum.get(letter, 0) + prev[r]

    for c in range(1, w):
        curr = [0] * h
        for r in range(h):
            letter_cur = grid[r][c]
            ways_from_left = prev[r]
            total_same = letter_sum.get(letter_cur, 0)

            letter_left = grid[r][c - 1]
            if letter_left == letter_cur:
                total_same -= prev[r]

            curr[r] = ways_from_left + total_same

        for r in range(h):
            letter = grid[r][c]
            letter_sum[letter] = letter_sum.get(letter, 0) + curr[r]

        prev = curr

    return prev[0] + prev[-1] if h > 1 else prev[0]


def main():
    with open("ijones.in", "r") as f:
        w, h = map(int, f.readline().split())
        grid = [f.readline().strip() for _ in range(h)]

    result = count_paths(grid)

    with open("ijones.out", "w") as f:
        f.write(str(result))


if __name__ == "__main__":
    main()
