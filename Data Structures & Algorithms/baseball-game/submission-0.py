class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = []
        for op in operations:
            if op == "D":
                score.append(score[-1]*2)
            elif op == "C":
                score.pop()
            elif op == "+":
                score_add = (score[-1] + score[len(score) - 2])
                score.append(score_add)
            else:
                score_add = int(op)
                score.append(score_add)
        
        return sum(score)