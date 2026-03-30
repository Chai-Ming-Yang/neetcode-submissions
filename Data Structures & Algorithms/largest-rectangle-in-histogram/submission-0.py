class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """ CONCEPT:
            - if (i+1) == (i): 
                extend & continue
            - if (i+1)  < (i): 
                pop & calculate
        """
        stack = []
        maxArea = 0
        for i in range(len(heights)):
            if not stack:
                stack.append([i, heights[i]])
                continue
            if stack[-1][1] < heights[i]:
                stack.append([i, heights[i]])
                continue
            popped = False
            while stack and stack[-1][1] > heights[i]:
                j, h = stack.pop()
                popped = True
                maxArea = max(maxArea, (i-j)*h)
            if popped:
                stack.append([j, heights[i]])
        print(stack)
        while stack:
            j, h = stack.pop()
            print(len(heights), j, h)
            maxArea = max(maxArea, (len(heights)-j)*h)
        return maxArea