class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        
        map = defaultdict(int)
        left = 0
        result = 0
        candidate = 0

        for right in range(len(s)):

            char = s[right]

            map[char]+=1
            candidate += 1

            while map[char] > 2:


                map[s[left]] -= 1
                left+=1
                candidate -= 1
            
            result = max(result, candidate)
        
        return result
        




