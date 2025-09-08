class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        string=s.strip().split() #strip removes the whitespace and split makes list of words  
        
        return len(string[-1])
        