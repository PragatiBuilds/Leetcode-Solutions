class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [0] * (2*n)
        for i in range(2*n):
            if i < n:
                ans[i] = nums[i]
            else:
                ans[i] = nums[n-i-1]
        
        return ans
