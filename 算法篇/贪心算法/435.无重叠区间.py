# 给定一个区间的集合 intervals ，其中 intervals[i] = [starti, endi] 。返回 需要移除区间的最小数量，使剩余区间互不重叠 。

 

# 示例 1:

# 输入: intervals = [[1,2],[2,3],[3,4],[1,3]]
# 输出: 1
# 解释: 移除 [1,3] 后，剩下的区间没有重叠。
# 示例 2:

# 输入: intervals = [ [1,2], [1,2], [1,2] ]
# 输出: 2
# 解释: 你需要移除两个 [1,2] 来使剩下的区间没有重叠。
# 示例 3:

# 输入: intervals = [ [1,2], [2,3] ]
# 输出: 0
# 解释: 你不需要移除任何区间，因为它们已经是无重叠的了。
 

# 提示:

# 1 <= intervals.length <= 105
# intervals[i].length == 2
# -5 * 104 <= starti < endi <= 5 * 104

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals:
            return 0
        intervals.sort(key=lambda x:x[0])
        
        count=0
        for i in range(1,len(intervals)):
            #两个相邻不重叠
            if intervals[i][0]>=intervals[i-1][1]:
                continue
            else:
                count+=1
                intervals[i][1]=min(intervals[i-1][1],intervals[i][1])
        return count
        
solution=Solution()
intervals=[[1,2],[2,3],[3,4],[1,3]]
print(solution.eraseOverlapIntervals(intervals))