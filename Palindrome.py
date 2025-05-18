class Solution:
    def isPalindrome(self, x: int) -> bool:
        c_str=str(x)
        rev=""

        for i in c_str:
            rev=i+rev
        
        if c_str==rev:
            return True
        else:
            return False
