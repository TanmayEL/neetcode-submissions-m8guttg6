class Solution:
    def countSeniors(self, details: List[str]) -> int:
        cnt = 0

        for passenger in details:
            if int(passenger[11:13]) > 60:
                cnt += 1
        
        return cnt