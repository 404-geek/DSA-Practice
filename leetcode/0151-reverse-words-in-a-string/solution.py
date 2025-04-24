class Solution:
    def reverseWords(self, s: str) -> str:

        res_arr = []
        for word in s.split(" ")[::-1]:
            if word:
                res_arr.append(word)

        print(res_arr)

        return " ".join(res_arr)

        
