#-*- coding: utf-8 -*-
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """

        total = 0
        start = 0
        cnt = len(nums) + 1

        for end, num in enumerate(nums):
            total += num
            while total >= s:
                cnt = min(cnt, end - start + 1)
                total -= nums[start]
                start += 1
        if cnt < len(nums)+1:
            return cnt
        else:
            return 0

if __name__ == '__main__':
    p = Solution()
    s = 14
    nums = [2,3,1,2,4]
    print(p.minSubArrayLen(s, nums))