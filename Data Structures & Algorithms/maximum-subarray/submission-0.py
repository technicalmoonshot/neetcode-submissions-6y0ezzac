class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        maxSum = nums[0]
        CurrSum = 0

        for n in nums:
            CurrSum = max(CurrSum,0)
            CurrSum +=n
            maxSum = max(maxSum,CurrSum)
        return maxSum
        