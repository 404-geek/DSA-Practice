class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:

        cnt = 0
        map = defaultdict(list)

        for i in range(len(s)):
            map[s[i]].append(i)

        def find_index(arr, ele):

            l = 0
            r = len(arr) - 1

            while l <= r:

                mid = (l + r) // 2

                if arr[mid] > ele:
                    r = mid - 1
                else:
                    l = mid + 1

            return l
                 
        def is_subs(word):
            curr = -1

            for ch in word:
                if ch not in map:
                    return False

                ind = find_index(map[ch], curr)
                
                if ind == len(map[ch]):
                    return False

                curr = map[ch][ind]

            return True

        freq = Counter(words)

        for w, f in freq.items():

            if is_subs(w):
                cnt+=f
        
        return cnt
                
        
