class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        i,j = None, None

        for n in nums:
            if i == None or i >= n:
                i = n
            elif j == None or j >= n:
                j = n
            else:
                return True
        return False

if __name__ == '__main__':
	s = Solution()
	print(s.increasingTriplet([2,1,5,0,4,6]))
