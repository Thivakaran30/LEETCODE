class Solution(object):
    def removeElement(self, nums, val):
        i=0
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        for x in nums:
            
            if x != val:
                nums[i]= x
                i+=1
        return i
