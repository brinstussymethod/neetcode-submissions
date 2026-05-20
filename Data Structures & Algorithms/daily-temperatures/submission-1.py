class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0] * len(temperatures)

        stack = [] # {temp , index}

        for i , t in enumerate(temperatures):
            while stack and t > stack[-1][0]: #top of stack is -1, first value in pair is 0 
                stackT, stackInd = stack.pop() # gets the number and index 
                res[stackInd] = (i - stackInd) # calculates the days it took subtracting stakc temp index and stack index

            stack.append([t, i])
        return res 

        

                


