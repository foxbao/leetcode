class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        M=len(matrix)
        N=len(matrix[0])
        dp=[[0]*N for _ in range(M)]
        
        res=0
        for i in range(M):
            dp[i][0]=int(matrix[i][0])
            res=max(res,dp[i][0])
            
        for j in range(N):
            dp[0][j]=int(matrix[0][j])
            res=max(res,dp[0][j])
        
        for i in range(1,M):
            for j in range(1,N):
                if int(matrix[i][j])==1:
                    dp[i][j]=min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1
                    if dp[i][j]>res:
                        res=dp[i][j]
        return res*res
        
solution=Solution()
print(solution.maximalSquare(matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))