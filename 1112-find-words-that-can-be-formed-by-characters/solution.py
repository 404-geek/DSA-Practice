class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:

        cnt_ch =Counter(chars)
        res = 0

        for i in words:

            cnt_i = Counter(i)

            k = 0

            for j in cnt_i:

                if cnt_i[j] > cnt_ch.get(j,0):
                    break
                
            else:
                res += len(i)

        
        return res
