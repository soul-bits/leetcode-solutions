from recursion.lc22_generate_parentheses import Solution


class TestGenerateParentheses:
    def test_n1(self):
        sol = Solution()
        result = sol.generateParenthesis(1)
        assert set(result) == {"()"}

    def test_n2(self):
        sol = Solution()
        result = sol.generateParenthesis(2)
        expected = {"()()", "(())"}
        assert set(result) == expected

    def test_n3(self):
        sol = Solution()
        result = sol.generateParenthesis(3)
        expected = {"((()))", "(()())", "(())()", "()(())", "()()()"}
        assert set(result) == expected


