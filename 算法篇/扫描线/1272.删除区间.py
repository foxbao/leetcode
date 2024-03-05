class Solution(object):
    def removeInterval(self, intervals, toBeRemoved):
        """
        :type intervals: List[List[int]]
        :type toBeRemoved: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        for interval in intervals:
            if interval[1]<=toBeRemoved[0] or interval[0]>=toBeRemoved[1]:
                res.append(interval)
            else:
                if interval[0]<toBeRemoved[0]:
                    res.append([interval[0],toBeRemoved[0]])
                if interval[1]>toBeRemoved[1]:
                    res.append([toBeRemoved[1],interval[1]])        
        return res
intervals = [[0,2],[3,4],[5,7]]
toBeRemoved = [1,6]
solution=Solution()
print(solution.removeInterval(intervals,toBeRemoved))