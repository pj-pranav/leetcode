class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
    	temp=[0]*n
    	j=0
    	for i in range(n):
    	   if nums[i]!=0:
    	       temp[j]=nums[i]
    	       j+=1
    	for i in range(n):
    	    nums[i]=temp[i]
    	return nums