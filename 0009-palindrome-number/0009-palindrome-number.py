class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        '''rem=0
        rev=0
        org=x
        while x>0:
            rem=x%10
            rev=rev*10+rem
            x=x//10
        if org==rev:
            return True
        
        return False'''
        string=str(x)

        if string==string[::-1]:
            return True
        else:
            return False
        