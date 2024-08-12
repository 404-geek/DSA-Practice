class Solution(object):
    def finalString(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        reversed_flag = False
        
        for char in s:
            if char == 'i':
                reversed_flag = not reversed_flag
            else:
                if reversed_flag:
                    result.insert(0, char)
                else:
                    result.append(char)
        
        if reversed_flag:
            result.reverse()
        
        return ''.join(result)

