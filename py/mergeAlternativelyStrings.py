class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = str()
        i = j = 0
        choice = 0
        while i < len(word1) and j < len(word2):
            if choice == 0:
                merged += word1[i]
                i += 1
                choice = 1
            elif choice == 1:
                choice = 0
                merged += word2[j]
                j += 1
        

        # print(i, j)
        while i < len(word1):
            merged += word1[i]
            i += 1
        # print(j < len(word2))
        while j < len(word2):
            print(word2[j])
            merged += word2[j]
            j += 1
        
        return merged

print(Solution().mergeAlternately(input(), input()))