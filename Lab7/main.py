def search(haystack, needle, base=256, prime=101):
    n = len(haystack)
    m = len(needle)
    result = []

    if m > n or m == 0:
        return result


    h = 1
    for _ in range(m - 1):
        h = (h * base) % prime


    p = 0
    t = 0
    for i in range(m):
        p = (base * p + ord(needle[i])) % prime
        t = (base * t + ord(haystack[i])) % prime


    for i in range(n - m + 1):
        if p == t:
            if haystack[i:i + m] == needle:
                result.append(i)

        if i < n - m:
            t = (base * (t - ord(haystack[i]) * h) + ord(haystack[i + m])) % prime
            if t < 0:
                t += prime

    return result


def main():
    haystack = "AABAACAADAABAABA"
    needle = "AABA"

    result = search(haystack, needle)

    print(f"Substring '{needle}' found at positions: {result}")


if __name__ == "__main__":
    main()
