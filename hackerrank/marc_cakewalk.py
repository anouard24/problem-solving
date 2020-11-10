def marcsCakewalk(calorie):
    p = 1
    s = 0
    for i in sorted(calorie, reverse=True):
        s += i*p
        p <<= 1
    return s

if __name__ == '__main__':

    n = int(input())
    calorie = list(map(int, input().rstrip().split()))

    print(marcsCakewalk(calorie))
