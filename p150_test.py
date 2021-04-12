from p150 import Solution

test_cases = [
    (["2","1","+","3","*"], 9),
    (["4","13","5","/","+"], 6),
    (["10","6","9","3","+","-11","*","/","*","17","+","5","+"], 22),
    (["4","13","5","/","+"], 6),
]

def test_evalRPN():
    for case in test_cases:
        s = Solution()
        assert s.evalRPN(case[0]) == case[1], case
