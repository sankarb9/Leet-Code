class Solution(object):
    def checkString(self, s):
        for i in range(len(s)):
            if s[i] == 'b':
                if 'a' in s[i+1:]:
                    return False
        return True