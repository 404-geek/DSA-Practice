from collections import defaultdict

class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        n = len(word)
        vowel = {"a", "e", "i", "o", "u"}

        def atleast(k):

            left, right = 0, 0
            consonants = 0
            vowels = defaultdict(int)
            cnt = 0
            n = len(word)

            while right < n:
                if word[right] in vowel:
                    vowels[word[right]] += 1
                else:
                    consonants += 1

                while consonants >= k and len(vowels) == 5:
                    cnt += (n - right)

                    if word[left] in vowel:
                        vowels[word[left]] -= 1
                        if vowels[word[left]] == 0:
                            del vowels[word[left]]
                    else:
                        consonants -= 1

                    left += 1

                right += 1

            return cnt

        return atleast(k) - atleast(k + 1)

