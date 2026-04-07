class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_val = 0
        counter = 0
        for p in nums:
            if p == 1:
                counter += 1
            else:
                max_val = max(max_val, counter)
                counter = 0
        return max(max_val, counter)