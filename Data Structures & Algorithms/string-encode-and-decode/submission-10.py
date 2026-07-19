class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return ">\<"
        enc = ">/<".join(strs)
        print(enc)
        return enc


    def decode(self, s: str) -> List[str]:
        if s == ">\<":
            return []
        return s.split(">/<")

