class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for index, n in enumerate(nums):
            hashmap[n] = index
        
        for k, v in hashmap.items():
            print(k, v)

        for index, n in enumerate(nums):
            difference = target - n
            if difference in hashmap and hashmap[difference] != index:
                return [index, hashmap[difference]]

        return []