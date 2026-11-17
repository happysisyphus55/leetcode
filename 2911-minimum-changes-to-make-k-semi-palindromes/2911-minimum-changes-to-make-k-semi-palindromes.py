class Solution:
  def minimumChanges(self, s: str, k: int) -> int:
    n = len(s)
    
    # divisors[length] stores all proper divisors of length
    divisors = [[] for _ in range(n + 1)]
    for length in range(1, n + 1):
      for d in range(1, length):
        if length % d == 0:
          divisors[length].append(d)

    # g[i][j] = minimum changes to make s[i..j] a semi-palindrome
    g = [[0] * n for _ in range(n)]
    for i in range(n):
      for j in range(i, n):
        length = j - i + 1
        min_changes = float('inf')
        for d in divisors[length]:
          changes = 0
          for start in range(d):
            # check characters in the group formed by interval d
            group = [s[k_idx] for k_idx in range(i + start, j + 1, d)]
            left, right = 0, len(group) - 1
            while left < right:
              if group[left] != group[right]:
                changes += 1
              left += 1
              right -= 1
          min_changes = min(min_changes, changes)
        g[i][j] = min_changes

    # dp[i][c] = min changes to partition s[0..i] into c parts
    INF = float('inf')
    dp = [[INF] * (k + 1) for _ in range(n)]
    
    for i in range(n):
      dp[i][1] = g[0][i]

    for c in range(2, k + 1):
      for i in range(c - 1, n):
        for h in range(c - 2, i):
          dp[i][c] = min(dp[i][c], dp[h][c - 1] + g[h + 1][i])

    return dp[n - 1][k]
