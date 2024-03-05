# 给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。

# 回文串 是正着读和反着读都一样的字符串。

 

# 示例 1：

# 输入：s = "aab"
# 输出：[["a","a","b"],["aa","b"]]
# 示例 2：

# 输入：s = "a"
# 输出：[["a"]]
 

# 提示：

# 1 <= s.length <= 16
# s 仅由小写英文字母组成

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.res=[]
        # if len(s)==1:
        #     self.res.append(s)
        #     return self.res
        self.backtracking(s,0,[])
        return self.res
        
    def backtracking(self,s,start_idx,path):
        
        if start_idx==len(s):
            self.res.append(path[:])
            return
        for i in range(start_idx,len(s)):
            if self.isPalindrome(s[start_idx:i+1]):
                path.append(s[start_idx:i+1])
                self.backtracking(s,i+1,path)
                path.pop()

    def isPalindrome(self,s):
        left=0
        right=len(s)-1
        while left<right:
            if not s[left]==s[right]:
                return False       
            left+=1
            right-=1
        return True
        
        
        
solution=Solution()
s='a'
print(solution.partition(s))


