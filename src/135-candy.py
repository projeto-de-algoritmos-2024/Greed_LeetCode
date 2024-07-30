class Solution(object):
    def candy(self, ratings):
        l = len(ratings)
        candies = [1] * l
        
        # laço do segundo ao último 
        for i in range(1, l):
            # se tiver mais rating que o da esquerda, incrementa.
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1

        # laço do penúltimo ao primeiro
        for i in range(l - 2, -1, -1):
            # se tiver mais rating que o da direita e
            # menor doces que o da direita + 1, incrementa 
            if ratings[i] > ratings[i+1] and candies[i+1] + 1 > candies[i]:
                candies[i] = candies[i+1] + 1
        
        return sum(candies)
        