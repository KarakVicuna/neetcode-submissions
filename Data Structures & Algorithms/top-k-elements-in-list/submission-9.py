class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countK = {}

        for i in nums:
            countK[i] = 1 + countK.get(i, 0)

        arr = []
        for i, count in countK.items():
            arr.append([count, i])
        arr.sort()

        finalList = []
        while len(finalList) < k:
            finalList.append(arr.pop()[1])
        return finalList
            