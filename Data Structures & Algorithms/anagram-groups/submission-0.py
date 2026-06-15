from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramList = defaultdict(list)
        for word in strs:
            sortWord = ''.join(sorted(word))
            anagramList[sortWord].append(word)
        return list(anagramList.values())