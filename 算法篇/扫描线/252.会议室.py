class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        if len(intervals)==1:
            return True
        def get_begin(element):
            return element[0]
        intervals.sort(key=get_begin)
        for i in range(len(intervals)-1):
            if intervals[i][1]>intervals[i+1][0]:
                return False
        return True
        aaa=1
        
        
        
intervals = [[0,30],[5,10],[15,20]]
solution=Solution()
print(solution.canAttendMeetings(intervals))