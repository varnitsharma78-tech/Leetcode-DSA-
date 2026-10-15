
class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        result = []
        i = 0

        while i < len(words):
            line_words = []
            letters = 0

            # Find words that fit in the current line
            while i < len(words) and letters + len(words[i]) + len(line_words) <= maxWidth:
                line_words.append(words[i])
                letters += len(words[i])
                i += 1

            # Last line or only one word: left-justify
            if i == len(words) or len(line_words) == 1:
                line = " ".join(line_words)
                line += " " * (maxWidth - len(line))
            else:
                spaces = maxWidth - letters
                gaps = len(line_words) - 1
                space_each = spaces // gaps
                extra = spaces % gaps

                line = ""
                for j, word in enumerate(line_words[:-1]):
                    line += word
                    line += " " * (space_each + (1 if j < extra else 0))

                line += line_words[-1]

            result.append(line)

        return result
