class Solution:

    def encode(self, strs: List[str]) -> str:
        return " ".join(strs)
    def decode(self, s: str) -> List[str]:
        print(s)
        return s.split(" ")