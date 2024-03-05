class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        
        res=[]
        for interval in intervals:
            if not(newInterval) or newInterval[0]>interval[1]:
                res.append(interval)
            elif newInterval[1]<interval[0]:
                res.append(newInterval)
                res.append(interval)
                newInterval=[]
            else:
                newInterval[0]=min(newInterval[0],interval[0])
                newInterval[1]=max(newInterval[1],interval[1])
        if newInterval:
            res.append(newInterval)
        return res
            
        
intervals = [[1,3],[6,9]]
newInterval = [2,5]
solution=Solution()
print(solution.insert(intervals,newInterval))