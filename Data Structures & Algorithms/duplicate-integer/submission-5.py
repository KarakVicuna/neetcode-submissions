class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        inList = set()
        for num in nums:
            if num in inList:
                return True
            inList.add(num)
        return False
        