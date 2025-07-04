from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        def justify(str_words, total_chars, is_last_line=False):
            if len(str_words) == 1 or is_last_line:
                # Left-justified
                line = " ".join(str_words)
                return line + " " * (maxWidth - len(line))

            spaces_to_fill = maxWidth - total_chars
            gaps = len(str_words) - 1
            base_space = spaces_to_fill // gaps
            extra_space = spaces_to_fill % gaps

            res = ""
            for i in range(len(str_words)):
                res += str_words[i]
                if i < gaps:
                    # Extra spaces go to the leftmost gaps
                    res += " " * (base_space + (1 if i < extra_space else 0))
            return res

        res = []
        i = 0
        curr_line = []
        curr_len = 0

        while i < len(words):
            word = words[i]
            if curr_len + len(curr_line) + len(word) > maxWidth:
                # len(curr_line) is number of gaps between words
                res.append(justify(curr_line, curr_len))
                curr_line = []
                curr_len = 0
            curr_line.append(word)
            curr_len += len(word)
            i += 1

        # Last line → left-justified
        res.append(justify(curr_line, curr_len, is_last_line=True))
        return res

