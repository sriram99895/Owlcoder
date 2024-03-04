class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        score = 0
        i = 0
        j = len(tokens)-1
        mas = 0
        while i<=j:
            if tokens[i]<=power:
                score +=1
                power = power - tokens[i]
                i+=1
            elif tokens[i]>power and score>=1:
                score = score -1
                power+=tokens[j]
                j-=1
            else:
                return mas
            mas = max(mas,score)    
        # if i == j:
        #     if tokens[i]<=power:
        #         mas = mas+1

        return mas           
            


        