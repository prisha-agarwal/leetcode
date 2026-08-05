class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0: 
            return 1
        binary = bin(n)[2:]
        flipped = ''.join('1' if b=='0' else '0' for b in binary)
        return int(flipped, 2)