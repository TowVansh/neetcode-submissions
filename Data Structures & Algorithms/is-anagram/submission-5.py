class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict={}
        t_dict={}
        if len(s)!=len(t):
            return False
        for char in s:
            s_dict[char] = s.count(char)
        for char in t:
            t_dict[char] = t.count(char)
        for char in s:
            try:
                if s_dict[char]!=t_dict[char]:
                    return False
            except Exception as e:
                return False
        for char in t:
            try:
                if s_dict[char]!=t_dict[char]:
                    return False
            except Exception as e:
                return False
        return True