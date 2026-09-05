class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefixmax=[]
        currentmax=nums[0]
        for i in range(len(nums)):
            currentmax=max(currentmax,nums[i])
            prefixmax.append(currentmax)

        suffixmin=[0]*len(nums)
        currentmin=nums[-1]
        for i in range(len(nums)-1,-1,-1):
            currentmin=min(currentmin,nums[i])
            suffixmin[i]=currentmin

        for i in range(len(nums)):
            stableindex=prefixmax[i]-suffixmin[i]
            if stableindex<=k:
                return i
        return -1