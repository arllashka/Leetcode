class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            match i:
                case "]":
                    if not stack or stack.pop() != "[" : return False 
                case "}":
                    if not stack or stack.pop() != "{" : return False 
                case ")":
                    if not stack or stack.pop() != "(" : return False 
                case _:
                    stack.append(i)
            
        
        return not stack