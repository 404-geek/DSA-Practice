class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:

        n = len(word)
        vowels = {"a", "e", "i", "o", "u"}
        tot_subs = 0

        for i in range(n):  # start of substring
            seen_v = set()
            cons = 0

            for j in range(i, n):  # end of substring

                if word[j] in vowels:
                    seen_v.add(word[j])
                else:
                    cons += 1

                # only count when all vowels and exactly k consonants
                if len(seen_v) == 5 and cons == k:
                    tot_subs += 1

                # pruning: if too many consonants, break
                if cons > k:
                    break

        return tot_subs
            

