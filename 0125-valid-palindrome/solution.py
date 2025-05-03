class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0

        j = len(s) -1

        while i < j:

            if s[i].isalnum() and s[j].isalnum() and s[i].lower() == s[j].lower():
                i+=1
                j-=1
            elif not s[i].isalnum():
                i+=1
            elif not s[j].isalnum():
                j-=1
            
            elif s[i].lower() != s[j].lower():
                return False
        
        return True

