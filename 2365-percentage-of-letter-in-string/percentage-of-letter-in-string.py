class Solution(object):
    def percentageLetter(self, s, letter):
        n=len(s)
        from collections import Counter
        co=Counter(s)
        le=co[letter]
        return (le*100)//n