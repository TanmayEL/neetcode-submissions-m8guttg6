class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        ans = [0] * n

        for i in range(n):
            current_temp = temperatures[i]
            if len(stack) == 0:
                stack.append(i)
                continue
            while stack and current_temp > temperatures[stack[-1]]:
                ind = stack.pop()
                ans[ind] = i - ind
            stack.append(i)
        return ans