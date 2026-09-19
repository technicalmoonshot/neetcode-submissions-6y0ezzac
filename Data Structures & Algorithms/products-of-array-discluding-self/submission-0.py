class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_prod = [1]* n
        post_fix_prod = [1] * n
        res = [1] * n

        total_prefix, total_postfix = 1,1

        for i in range(0,n):
            total_prefix = total_prefix * nums[i]
            prefix_prod[i] = total_prefix

        for j in range(n-1,-1,-1):
            total_postfix = total_postfix * nums[j]
            post_fix_prod[j] = total_postfix

        for k in range(0,n):
            left = prefix_prod[k-1] if k >0 else 1
            right = post_fix_prod[k+1] if k < n-1 else 1
            res[k] = left * right
        
        return res
        

        




        