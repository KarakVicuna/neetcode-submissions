class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniqueNumbers = set(nums)
        if len(uniqueNumbers) == len(nums):
            return False
        else: 
            return True

        
        