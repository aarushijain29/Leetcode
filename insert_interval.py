class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]

            # newInterval is to the left on current interval and doesn't overlap
            if newInterval[1] < start:
                res.append(newInterval)
                return res + intervals[i::]
            # newInterval is to the right on current interval and doesn't overlap
            elif newInterval[0] > end:
                res.append(intervals[i])
                # no return because we still need to check if newInterval overlaps with
                # other intervals
            # above conditions not satisfied - newInterval overlaps with current interval
            else:
                newInterval[0] = min(start, newInterval[0])
                newInterval[1] = max(end, newInterval[1])

        res.append(newInterval)
        return res
    
