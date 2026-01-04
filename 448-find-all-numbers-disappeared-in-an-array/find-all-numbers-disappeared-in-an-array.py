class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n= set(nums)
        m = len(nums)
        x = []
        for p in range (1, m+1):
            if  p not in n:
                x.append(p)
        return x