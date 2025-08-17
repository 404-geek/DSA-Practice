class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        i = 0
        j = 0
        max_cnt_vowels = 0
        vowels = 0

        vowel = {"a","e","i","o","u"}

        while j < len(s):

            if s[j] in vowel:

                vowels+=1

            if j - i + 1 > k:
                if s[i] in vowel:
                    vowels-=1
                i+=1

            if j - i + 1 == k:

                max_cnt_vowels = max(max_cnt_vowels, vowels)

            j+=1

        return max_cnt_vowels




