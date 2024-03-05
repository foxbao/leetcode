class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        
boxTypes = [[1,3],[2,2],[3,1]]
truckSize = 4
solution=Solution()
print(solution.maximumUnits(boxTypes,truckSize))