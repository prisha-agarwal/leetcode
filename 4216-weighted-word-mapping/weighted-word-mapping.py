class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        result = str()
        dic = {chr(97+i): weights[i] for i in range(26)}
        rev = {i: chr(122-i) for i in range(26)}
        for s in words: 
            result1 = 0
            for c in s: 
                result1 += dic[c] 
            result2 = result1 % 26
            lastletter = rev[result2]
            result+=lastletter
        return result 

        