class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hasDuplicate = set(nums)
        if len(hasDuplicate) == len(nums):
            return False
        else:
            return True

        