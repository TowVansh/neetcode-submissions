class Solution:
    def encode(self, strs: List[str]) -> str:
        return "~%@!".join(strs) if strs else "~%@!~%@!"

    def decode(self, s: str) -> List[str]:
        return [] if s == "~%@!~%@!" else s.split("~%@!")