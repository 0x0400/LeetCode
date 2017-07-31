from p22 import Solution


def test_generateParenthesis():
    s = Solution()
    result = s.generateParenthesis(3)
    result.sort()
    assert_value = ["((()))", "(()())", "(())()", "()(())", "()()()"]
    assert_value.sort()
    assert result == assert_value

    result = s.generateParenthesis(4)
    result.sort()
    assert_value = ["(((())))", "((()()))", "((())())", "((()))()", "(()(()))",
                    "(()()())", "(()())()", "(())(())", "(())()()", "()((()))",
                    "()(()())", "()(())()", "()()(())", "()()()()"]
    assert_value.sort()
    assert result == assert_value
