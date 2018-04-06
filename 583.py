#-*- coding: utf-8 -*-
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

        n = len(word1)
        m = len(word2)
        dp = [[0] * (m+1) for i in range(n+1)]
        for i in range(n):
            for j in range(m):
                if word1[i] == word2[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        return n+m - 2*dp[n][m]
        # dp = [[0] * (n + 1) for i in range(m + 1)]
        # for i in range(m):
        #     for j in range(n):
        #         dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j], dp[i][j] + (w1[i] == w2[j]))
        # return m + n - 2 * dp[m][n]


if __name__ == '__main__':
    s = Solution()
    print(s.minDistance("","a"))
