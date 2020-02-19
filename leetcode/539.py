class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def to_int(t):
            # NOTE : make it integer!
            h, m = map(int, t.split(':'))
            return h*60 + m
        
        timePoints = [to_int(elem) for elem in timePoints]
        timePoints.sort()
        
        min_diff = float('inf')
        for idx, elem in enumerate(timePoints):
            # NOTE : exception for last elem
            if idx == len(timePoints) - 1: break
            min_diff = min(min_diff, timePoints[idx+1] - elem)
        
        min_diff = min(min_diff, timePoints[0] - timePoints[-1] + 1440)
        return min_diff
