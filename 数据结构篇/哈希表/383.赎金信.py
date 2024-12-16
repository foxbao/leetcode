# 给你两个字符串：ransomNote 和 magazine ，判断 ransomNote 能不能由 magazine 里面的字符构成。

# 如果可以，返回 true ；否则返回 false 。

# magazine 中的每个字符只能在 ransomNote 中使用一次。

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        counts={}
        for c in magazine:
            counts[c]=counts.get(c,0)+1
        for c in ransomNote:
            if c not in counts or counts[c]==0:
                return False
            counts[c]-=1
            
        return True
        
        # ransom_count=[0]*26
        # magazine_count=[0]*26
        
        # for c in ransomNote:
        #     ransom_count[ord(c)-ord('a')]+=1
        # for c in magazine:
        #     magazine_count[ord(c)-ord('a')]+=1
            
        # return all(ransom_count[i] <= magazine_count[i] for i in range(26))
        
solution=Solution()
ransomNote = "aa"
magazine="aab"
print(solution.canConstruct(ransomNote,magazine))