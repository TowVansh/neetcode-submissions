class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs)==0:
                return "10101010"
        return "0592045969".join(strs)
    def decode(self, s: str) -> List[str]:
        if s=="10101010":
            return []
        return s.split("0592045969")