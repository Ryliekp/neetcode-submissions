class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {}
        for i in s:
            if i in letters:
                letters[i] += 1
            else:
                letters[i] = 1

        for j in t:
            if j in letters:
                letters[j] -= 1
                if letters[j] == 0:
                    letters.pop(j)
            else:
                return False
        return len(letters) == 0