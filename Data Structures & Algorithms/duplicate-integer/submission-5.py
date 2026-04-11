class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # seen = set()

        # for num in nums:
        #     if num in seen:
        #         return True
        #     else:
        #         seen.add(num)
        # return False

        nums.sort()

        for i in range(0,len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
    
        return False
        
    


         