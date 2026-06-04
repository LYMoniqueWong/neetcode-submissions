class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s): 
            # find length
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            # extract string
            start = j + 1
            end = start + length
            res.append(s[start:end])
            i = end
        return res