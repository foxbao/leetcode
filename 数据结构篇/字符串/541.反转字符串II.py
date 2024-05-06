# 给定一个字符串 s 和一个整数 k，从字符串开头算起，每计数至 2k 个字符，就反转这 2k 字符中的前 k 个字符。

# 如果剩余字符少于 k 个，则将剩余字符全部反转。
# 如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。
 

# 示例 1：

# 输入：s = "abcdefg", k = 2
# 输出："bacdfeg"
# 示例 2：

# 输入：s = "abcd", k = 2
# 输出："bacd"
 

# 提示：

# 1 <= s.length <= 104
# s 仅由小写英文组成
# 1 <= k <= 104

class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        
        res = list(s)

        for cur in range(0, len(s), 2 * k):
            res[cur: cur + k] = self.reverse_substring(res[cur: cur + k])
        
        return ''.join(res)
    
    def reverse_substring(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        if len(s)==1:
            return s
        left=0
        right=len(s)-1
        
        while left<=right:
            tmp=s[left]
            s[left]=s[right]
            s[right]=tmp
            left+=1
            right-=1
        return s
        
        
        
solution=Solution()
s = "abcdefg"
k=2
print(solution.reverseStr(s,k))