class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        line_letters = 0
        line_words =[]
        res = []

        def justify_text(words, letter, end_line=False):
            
            if end_line or len(words) == 1:
                line = " ".join(words)
                return line + " " * (maxWidth - len(line))

            left_spaces = maxWidth - letter

            spaces_present = len(words) - 1

            rem = left_spaces // spaces_present
            extra = left_spaces % spaces_present

            line = ""
            for i in range(spaces_present):
                line+= words[i]
                line+= " " * (rem + (1 if i < extra else 0))
            
            line+=words[-1]
            return line

        
        for word in words:

            if line_letters + len(word) + len(line_words) <= maxWidth:
                line_letters+= len(word)
                line_words.append(word)
            else:
                res.append(justify_text(line_words, line_letters))
                line_words = [word]
                line_letters = len(word)
        
        res.append(justify_text(line_words, line_letters, True))
        return res



        
                





        
