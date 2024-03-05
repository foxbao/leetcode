# 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。

 

# 示例 1：

# 输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
# 输出：[[1,6],[8,10],[15,18]]
# 解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
# 示例 2：

# 输入：intervals = [[1,4],[4,5]]
# 输出：[[1,5]]
# 解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。
 

# 提示：

# 1 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 104

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        result=[]
        if len(intervals)==0:
            return result
        
        intervals.sort(key=lambda x:x[0])
        result.append(intervals[0])
        
        for i in range(1,len(intervals)):
            if result[-1][1]>=intervals[i][0]: 
                result[-1][1]=max(result[-1][1],intervals[i],1)
            else:
                result.append(intervals[i])
        return result
solution=Solution()
intervals=[[1,3],[2,6],[8,10],[15,18]]
print(solution.merge(intervals))