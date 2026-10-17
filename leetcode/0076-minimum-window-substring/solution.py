class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        cnt_t = Counter(t)

        m = len(s)

        req = len(cnt_t)

        i = 0

        curr_dict = {}
        ongoing = 0
        
        min_len = float('inf')
        word = ""

        for j in range(m):

            ch = s[j]

            if ch in curr_dict:
                curr_dict[ch] += 1
            else:
                curr_dict[ch] = 1

            if ch in cnt_t and curr_dict[ch] == cnt_t[ch]:
                ongoing+=1

            while ongoing == req:

                if j - i + 1 < min_len:

                    min_len = j-i+1

                    word = s[i:j+1]
                
                curr_dict[s[i]]-=1

                if s[i] in cnt_t and curr_dict[s[i]] < cnt_t[s[i]]:
                    ongoing-=1

                i+=1

        return word

        

                 

                





            
