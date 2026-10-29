class Solution:
    def candy(self, ratings: list[int]) -> int:
        n = len(ratings) 
        count= n * [1] 

        for i in range(1,n):
            if ratings[i]>ratings[i-1]:
                count[i] = count[i-1] + 1

        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                count[i] = max(count[i+1] + 1, count[i])
        return sum(count) 
            
  
            


