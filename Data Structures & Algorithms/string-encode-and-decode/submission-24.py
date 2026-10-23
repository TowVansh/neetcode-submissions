class Solution:
    def encode(self, strs: List[str]) -> str:
        return "\u0100".join(strs) if strs else "\u0101"

    def decode(self, s: str) -> List[str]:
        return [] if s == "\u0101" else s.split("\u0100")