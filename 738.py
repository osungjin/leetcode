#-*- coding: utf-8 -*-

class Solution(object):
    def calculate(self, N):
        for i in range(1, len(N)):
            if N[i] >= N[i-1]:
                pass
            else:
                return False, i
        return True, 0

    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        
        N = str(N)
        input_n = N
        for i in range(len(N)):
            r1, r2 = self.calculate(input_n)
            if r1 == False:
                tmp = int(input_n[:r2]) - 1
                tmp_2 = [str(9)] * len(input_n[r2:])
                res = str(tmp) + ''.join(tmp_2)
                return int(res)
                #tmp = (int(N) / pow(10,r2+1) - 1) * pow(10, r2+1)
            else:
                return int(input_n)

if __name__ == '__main__':
    s = Solution()
    N = str(input())
    print(s.monotoneIncreasingDigits(N))


