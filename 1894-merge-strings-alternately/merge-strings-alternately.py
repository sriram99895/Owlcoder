class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s1 = len(word1)
        s2 = len(word2)
        i = 0
        j = 0
        new_word = ""
        while(i<s1 and j<s2):
            new_word+=word1[i]
            new_word+=word2[j]
            i+=1
            j+=1
        while(i<s1):
            new_word+=word1[i]
            i+=1
        while(j<s2):
            new_word+=word2[j]
            j+=1
        return new_word    
            
        