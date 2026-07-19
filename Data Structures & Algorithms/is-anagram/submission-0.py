class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_dict = self.makeDict(s)
        t_dict = self.makeDict(t)

        return s_dict == t_dict

    def makeDict(self, string):
        res = {}
        for char in string:
            res[char] = res.get(char, 0) + 1
        return res