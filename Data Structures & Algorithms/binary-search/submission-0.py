class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l , r = 0 , len(nums) - 1 
        
        for number in nums:

            middle = l + ((r - l) // 2) 

            if(target == nums[middle]):
                return middle 
            if(target < nums[middle]):
                middle -= 1 
                r = middle 
            if(target > nums[middle]):
                middle += 1 
                l = middle 
            
        return -1 
            
            