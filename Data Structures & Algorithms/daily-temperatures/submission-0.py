class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        ans = [0] * n

        for i in range(n):
            current_temp = temperatures[i]
            if len(stack) == 0:
                stack.append((current_temp, i))
                continue
            while stack and current_temp > stack[-1][0]:
                prev, ind = stack.pop()
                ans[ind] = i - ind
            stack.append((current_temp, i))
        return ans