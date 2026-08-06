class Solution:
    def isPalindrome(self, s: str) -> bool:
        st=""
        for x in s:
            if x.isalnum():
                st+=x
        return st.lower()==st[::-1].lower()      