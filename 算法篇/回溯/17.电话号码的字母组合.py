# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。

# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。



 

# 示例 1：

# 输入：digits = "23"
# 输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
# 示例 2：

# 输入：digits = ""
# 输出：[]
# 示例 3：

# 输入：digits = "2"
# 输出：["a","b","c"]
 

# 提示：

# 0 <= digits.length <= 4
# digits[i] 是范围 ['2', '9'] 的一个数字。

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        self.letterMap = [
            "",     # 0
            "",     # 1
            "abc",  # 2
            "def",  # 3
            "ghi",  # 4
            "jkl",  # 5
            "mno",  # 6
            "pqrs", # 7
            "tuv",  # 8
            "wxyz"  # 9
        ]
        self.result=[]
        if len(digits) == 0:
            return self.result
        s=""
        self.backtracking(digits, 0,s)
        return self.result
    
    def backtracking(self,digits,index,s):
        if index==len(digits):
            self.result.append(s)
            return
        digit =int(digits[index])
        letters=self.letterMap[digit]
        for i in range(len(letters)):
            s+=letters[i]
            self.backtracking(digits,index+1,s)
            s=s[:-1]
    
        
        
solution=Solution()
digits="23"
print(solution.letterCombinations(digits))