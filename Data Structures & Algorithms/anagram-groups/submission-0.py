class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strsd={}
        output=[]
        for s in strs:
            strsd["".join(sorted(s))]=[]
        for s in strs:
            strsd["".join(sorted(s))].append(s)
        for key in strsd:
            output.append(strsd[key])
        return output