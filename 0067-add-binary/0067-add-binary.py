class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        c=int(a,base=2)
        d=int(b,base=2)
        add=c+d

        return format(add,'b')