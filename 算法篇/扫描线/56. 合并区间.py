class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
        def get_start(element):
            return element[0]
        intervals.sort(key=get_start)
        res=[]
        cur=intervals[0]
        for interval in intervals:
            if cur[1]>=interval[0]:
                cur[1]=max(interval[1],cur[1])
            else:
                res.append(cur)
                cur=interval
        res.append(cur)
        return res
            
        
intervals = [[1,3],[2,6],[8,10],[15,18]]
solution=Solution()
print(solution.merge(intervals))