class Solution:
    def calPoints(self, operations: List[str]) -> int:

        res = []

        for op in operations:
            if op not in ['+','C','D']:
                res.append(int(op))
            elif op == "+":
                num_1 = res[-1]
                num_2 = res[-2]
                num_3 = num_1+num_2
                res.append(num_3)   
            elif op == "C":
                res.pop()
            elif op == "D":
                num_1 = res[-1]
                res.append(2 * num_1) 
        return sum(res)