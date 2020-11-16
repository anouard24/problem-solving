t9 = [["2"], ["2"] * 2, ["2"] * 3]
t9.extend([["3"], ["3"] * 2, ["3"] * 3])
t9.extend([["4"], ["4"] * 2, ["4"] * 3])
t9.extend([["5"], ["5"] * 2, ["5"] * 3])
t9.extend([["6"], ["6"] * 2, ["6"] * 3])
t9.extend(
    [["7"], ["7"] * 2, ["7"] * 3, ["7"] * 4],
)
t9.extend([["8"], ["8"] * 2, ["8"] * 3])
t9.extend([["9"], ["9"] * 2, ["9"] * 3, ["9"] * 4])
t9.append("0")


def get_t9(c):
    global t9
    if c != " ":
        return t9[ord(c) - 97]
    else:
        return t9[-1]


n = int(input())

for j in range(n):
    s = str(input())
    a = []
    a.extend(get_t9(s[0]))

    i = 1
    while i < len(s):
        c = get_t9(s[i])
        if c[0] == a[-1]:
            a.append(" ")
        a.extend(c)
        i += 1

    print("Case #%d: " % (j + 1) + "".join(a))
