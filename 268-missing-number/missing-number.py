class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum =0
        sum= (n*(n+1)//2)
        x = 0
        for nm in nums:
            x+=nm
        final = sum - x
        return final