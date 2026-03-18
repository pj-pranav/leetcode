class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int

        """
        nums.append(target)
        nums.sort()
        for i in range(len(nums)):
            if nums[i]==target:
                return i

            
    
        