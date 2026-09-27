class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        # Convert knowledge list into a dictionary
        mp = {}

        for key, value in knowledge:
            mp[key] = value

        result = []
        i = 0

        while i < len(s):
            if s[i] == '(':
                # Find closing bracket
                j = i + 1

                while s[j] != ')':
                    j += 1

                # Extract key
                key = s[i + 1:j]

                # Add value or ?
                result.append(mp.get(key, '?'))

                i = j + 1
            else:
                result.append(s[i])
                i += 1

        return ''.join(result)