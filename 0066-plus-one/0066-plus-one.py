class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        st="".join(str(i) for i in digits)
        num=int(st)+1
        li=str(num)
        res=[int(i) for i in li]
        return res