class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        counter, res = 0,0
        for num in nums:
            if num ==1:
                counter +=1
            else:
                res = max(counter, res)
                counter = 0
        return max(counter, res)
            
            
        