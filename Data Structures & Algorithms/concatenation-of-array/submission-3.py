class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums)
        ans = [0] * (2 * length)
        for i, nums in enumerate(nums):
            ans[i] = nums
            ans[i + length] = nums
        return ans