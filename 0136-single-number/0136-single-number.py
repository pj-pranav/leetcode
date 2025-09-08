class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k=0
        for i in range(len(nums)):#cheching index value in array
                k=k^nums[i] #XOR(^) a^0=a, a^a=0
        return k
        
        
        