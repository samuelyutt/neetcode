class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += f'{str(len(s)).zfill(3)}{s}'
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            length = int(s[i: i + 3])
            if (length):
                out = s[i + 3: i + 3 + length]
            else:
                out = ''
            res.append(out)
            i += (3 + length)

        return res
