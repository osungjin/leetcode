#-*- coding: utf-8 -*-

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        buf = set()
        res = set()
        for i in range(len(s) - 9):
            base_str = s[i:i+10]
            if base_str not in buf:
                buf.add(base_str)
            else:
                res.add(base_str)
        return list(res)
if __name__ == '__main__':
    s = Solution()
    print(s.findRepeatedDnaSequences("AAAAAAAAAAAA"))
