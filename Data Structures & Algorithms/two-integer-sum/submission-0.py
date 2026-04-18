class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = 0
        arr = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                temp = nums[i] + nums[j]
                if temp == target:
                    arr.append(i)
                    arr.append(j)
                    return arr