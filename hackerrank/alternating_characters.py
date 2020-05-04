
def alternatingCharacters(s):
    i = k = 0
    j = 1
    n = len(s)
    while j < n:
        if s[i] == s[j]:
            k += 1
        else:
            i = j
        j += 1
    return k

if __name__ == '__main__':
    q = int(input())
    for _ in range(q):
        s = input()

        result = alternatingCharacters(s)
        print(result)
