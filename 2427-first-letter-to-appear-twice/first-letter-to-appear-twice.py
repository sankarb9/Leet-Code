class Solution(object):
    def repeatedCharacter(self, s):
        count = {}

        for ch in s:
            count[ch] = count.get(ch, 0) + 1

            if count[ch] == 2:
                return ch

        return ""