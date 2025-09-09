class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num==0:
            return 0
        else:
            return 1+(num-1)%9 #formula to get result number between 1 to 9(one digit)
      