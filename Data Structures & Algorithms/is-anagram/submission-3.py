class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictionary1 = {}
        dictionary2 = {}
        for letter in s:
            letter = letter.lower()
            if letter not in dictionary1:
                dictionary1[letter] = 1 
            else:
                dictionary1[letter] += 1 
        for letter in t:
            letter = letter.lower()
            if letter not in dictionary2:
                dictionary2[letter] = 1 
            else:
                dictionary2[letter] += 1 
        if dictionary1.items() == dictionary2.items():
            return True
        else:
            return False