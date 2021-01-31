class Solution:
    def isValid(self, s: str) -> bool:
        valid = []
        match = {'(': ')', '[': ']', '{': '}'}
        for c in s:
            if c in match:
                valid.append(c)
            else:
                if not valid or match[valid.pop()] != c:
                    return False
        return not valid
