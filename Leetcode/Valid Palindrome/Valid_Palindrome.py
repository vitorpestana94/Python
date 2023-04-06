class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[\s\W_]', "", s).lower()
        return True if s == s[::-1] else False
