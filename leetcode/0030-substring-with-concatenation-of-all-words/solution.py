class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        l = len(words[0])
        word_freq = Counter(words)
        w = len(words)
        n = len(s)

        res = []


        for offset in range(l):

            left = offset

            curr = defaultdict(int)
            count = 0

            for j in range(offset, n - l + 1, l):

                word = s[j : j+l]

                if word in word_freq:

                    curr[word]+=1
                    count+=1

                    while curr[word] > word_freq[word]:
                        left_word = s[left:left + l]
                        curr[left_word] -=1
                        count-=1
                        left +=  l

                    if count == w:

                        res.append(left)
                        left_word = s[left:left + l]
                        curr[left_word] -=1
                        count-=1
                        left +=  l

                else:
                    curr.clear()
                    count=0
                    left = j + l

        return res
        
