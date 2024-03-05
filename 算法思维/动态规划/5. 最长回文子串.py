class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res=""
        n=len(s)
        for i in range(n):
            for j in range(i,n):
                if(j-i+1>=len(res) and self.isPalindrome(s,i,j)):
                    res=s[i:j+1]

        return res

    def isPalindrome(self,s,start,end):
        n=len(s)
        l=start
        r=end
        while(l<=r):
            if(s[l]!=s[r]):
                return False
            l+=1
            r-=1
        return True
