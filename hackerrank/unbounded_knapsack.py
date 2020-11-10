from collections import defaultdict

def unboundedKnapsack(k, arr):
    d = defaultdict(int)
    for i in arr:
        d[i] = 1
    a = sorted(d)
    n = len(a)+1
    dp = [0] * n
    for i in range(n):
        dp[i] = [0]* (k+1)
    for i in range(1, n):
        for j in range(1, k+1):
            v = j % a[i-1]
            if v == 0:
                dp[i][j] = j
            elif j > a[i-1]:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j], a[i-1]+dp[i][j-a[i-1]])
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        if dp[i][k] == k:
            return k
    return dp[-1][-1]

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().rstrip().split())
        arr = list(map(int, input().rstrip().split()))
        result = unboundedKnapsack(k, arr)
        print(result)
