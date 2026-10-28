class Solution(object):
    def uniqueMorseRepresentations(self, words):
        morse = [
            ".-", "-...", "-.-.", "-..", ".", "..-.", "--.",
            "....", "..", ".---", "-.-", ".-..", "--", "-.",
            "---", ".--.", "--.-", ".-.", "...", "-", "..-",
            "...-", ".--", "-..-", "-.--", "--.."
        ]

        result = set()

        for word in words:
            code = ""

            for letter in word:
                code += morse[ord(letter) - ord('a')]

            result.add(code)

        return len(result)