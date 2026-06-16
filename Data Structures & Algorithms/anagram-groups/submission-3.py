class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        same = defaultdict(list)
        for word in strs:
            sort = ''.join(sorted(word))
            same[sort].append(word)
        return list(same.values())