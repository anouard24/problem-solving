def repeatedString(s, n):
    x = [0]
    a = 0
    for c in s:
        if c == "a":
            a += 1
        x.append(a)
    return n // (len(s)) * x[-1] + x[n % len(s)]


if __name__ == "__main__":

    s = input()
    n = int(input())

    print(repeatedString(s, n))
