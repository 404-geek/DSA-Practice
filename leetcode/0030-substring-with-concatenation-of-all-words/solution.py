class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        words_cnt = Counter(words)
        stats = defaultdict(int)
        
        k = len(words[0]) 
        total = k * len(words)

        res = []

        for start in range(k):

            left = right = start
            word_counter = Counter()

            while right + k <= len(s):

                word = s[right:right + k]
                right+=k

                if word not in words_cnt:
                    word_counter.clear()
                    left = right
                    continue
                
                word_counter[word]+=1

                while word_counter[word] > words_cnt[word]:
                    removed_word = s[left:left+k]

                    left+=k
                    word_counter[removed_word]-=1

                if right - left == total:
                    res.append(left)

        return res

            





