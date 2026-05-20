class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1 
        if nums[left] < nums[right]:
            return nums[left]

        while left < right: 
            mid = left + (right - left)  // 2 
            if nums[mid] > nums[right]:
                mid += 1 
                left = mid 
            else:
                right = mid 

        return nums[left]
                
            