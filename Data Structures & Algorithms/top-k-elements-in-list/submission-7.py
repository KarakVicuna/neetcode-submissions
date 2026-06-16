class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countK = {}

        for i in nums:
            print(i)
            countK[i] = 1 + countK.get(i, 0)

        arr = []
        for i, count in countK.items():
            arr.append([count, i])
        arr.sort()
        print(arr)

        finalList = []
        while len(finalList) < k:
            finalList.append(arr.pop()[1])
            print(arr)
            print(finalList)
        return finalList
            