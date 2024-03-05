class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals:
            return 0
        if len(intervals)==1:
            return 1
        begin=[]
        end=[]
        for interval in intervals:
            begin.append(interval[0])
            end.append(interval[1])
        begin.sort()
        end.sort()
        i=0
        j=0
        count=0
        res=0
        while i <len(intervals) and j<len(intervals):
            if begin[i]<end[j]:
                count+=1
                i+=1
            else:
                count-=1
                j+=1
            res=max(res,count)
        return res
        
intervals = [[13,15],[1,13]]
solution=Solution()
print(solution.minMeetingRooms(intervals))