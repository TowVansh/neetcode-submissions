class Solution:
    def encode(self, strs: List[str]) -> str:
        return ",".join(map(str, map(len, strs))) + "#" + "".join(strs)

    def decode(self, s: str) -> List[str]:
        head, body = s.split("#", 1)
        if not head:
            return []
        out, i = [], 0
        for n in map(int, head.split(",")):
            out.append(body[i:i + n])
            i += n
        return out