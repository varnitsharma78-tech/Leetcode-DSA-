from typing import List


class Solution:

  def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    word_set = set(wordDict)
    n = len(s)

    # dp[i] is True if s[:i] can be segmented into dictionary words
    dp = [False] * (n + 1)
    dp[0] = True  # Base case: empty string

    for i in range(1, n + 1):
      for j in range(i):
        # Check if prefix s[:j] is valid and substring s[j:i] is in the dictionary
        if dp[j] and s[j:i] in word_set:
          dp[i] = True
          break

    return dp[n]
