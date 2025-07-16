from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        max_len = max(len(word) for word in wordDict)
        for i in range(1, len(s) + 1):
            for j in range(max(0, i - max_len), i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break

        return dp[len(s)]
    

    def rebuild_solution(self, dp: List[bool], s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        words = []
        i = n
        j = n - 1
        while i >= 0 and j >= 0:
            if dp[j] and s[j:i] in wordDict:
                words.append(s[j:i])
                i = j
            j -= 1
        return words[::-1]