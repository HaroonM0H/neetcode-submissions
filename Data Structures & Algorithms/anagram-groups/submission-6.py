class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultDict(list)

        for  s in strs:
            count = [0] * 26 # a to z

            for c in s:
                count[ord(c) - ord ("a")] += 1
            return res[tuple(count)].append(s)
        return list(res.values) 