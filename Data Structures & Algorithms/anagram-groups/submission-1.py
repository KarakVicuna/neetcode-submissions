class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramList = defaultdict(list)
        for word in strs:
            letters = [0] * 26
            for i in word:
                letters[ord(i) - ord('a')] += 1
            tup = tuple(letters)
            anagramList[tup].append(word)

        return list(anagramList.values())