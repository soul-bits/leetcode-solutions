from recursion.lc77_combinations import Solution


class TestCombinations:
    def test_combine_basic(self):
        sol = Solution()
        result = sol.combine(4, 2)
        expected = [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
        assert len(result) == len(expected)
        for comb in expected:
            assert comb in result

    def test_combine_single_element(self):
        sol = Solution()
        result = sol.combine(1, 1)
        assert result == [[1]]

    def test_combine_all_elements(self):
        sol = Solution()
        result = sol.combine(3, 3)
        assert result == [[1, 2, 3]]

    def test_combine_k_equals_one(self):
        sol = Solution()
        result = sol.combine(4, 1)
        expected = [[1], [2], [3], [4]]
        assert len(result) == len(expected)
        for comb in expected:
            assert comb in result

    def test_combine_larger_case(self):
        sol = Solution()
        result = sol.combine(5, 3)
        # C(5,3) = 10 combinations
        assert len(result) == 10
        expected = [
            [1, 2, 3], [1, 2, 4], [1, 2, 5],
            [1, 3, 4], [1, 3, 5], [1, 4, 5],
            [2, 3, 4], [2, 3, 5], [2, 4, 5],
            [3, 4, 5]
        ]
        for comb in expected:
            assert comb in result

