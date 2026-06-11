class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ouput = []
        from collections import deque
        q = deque()

        l,r =0,0

        for i in range(len(nums)):
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
            
            if q[0] < i - k + 1:
                q.popleft()
            
            if i >= k - 1:
                output.append(nums[q[0]])
        
        return output