#-*- coding: utf-8 -*-
# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """

        intervals = sorted(intervals, key= lambda interval: interval.start)
        interval_length = len(intervals)
        prev, count = 0, 0
        for i in range(1, interval_length):
            if intervals[prev].end > intervals[i].start:
                if intervals[prev].end > intervals[i].end:
                    prev = i
                count += 1
            else:
                prev = i
        return count

if __name__ == '__main__':
    s = Solution()
    input_list = []
    input_list.append(Interval(1, 2))
    input_list.append(Interval(1, 2))
    input_list.append(Interval(1, 2))
    print(s.eraseOverlapIntervals(input_list))
