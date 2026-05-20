class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #only add open paranthesis if open < n 
        #only add a closing paranthesis if close < open 
        #it's valid IIF open == close == n 

        #using a recurssive stack 

        stack = [] 
        res = [] 
        # n = 3 
        def backtrack(openN , closedN):
             if openN == closedN == n:
                res.append("".join(stack)) #take every character in a stack, and join them together. And add them to res. 
                return
             if openN < n:
                stack.append("(")
                backtrack(openN + 1 , closedN)
                stack.pop() 
             if closedN < openN:
                stack.append(")")
                backtrack(openN , closedN + 1)
                stack.pop() 

        backtrack(0 , 0)
        return res 
        #how does the algoritm know not to dulpitcate a path that has already been appended to res 
        #The answer probably lies in DFS      

