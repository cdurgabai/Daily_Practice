class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for element in s:
            if element in "([{":
                stack.append(element)
            else:
                if len(stack)==0:
                    return False
                x=stack.pop()
                if x=="(" and element==")" or x=="[" and element=="]" or x=="{" and element=="}":
                    continue
                else:
                    return False
        return len(stack)==0

#s="{{[(}}" # False
s="{[({{{}}})]}"
sol=Solution()
print(sol.isValid(s)) # True
