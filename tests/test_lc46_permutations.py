from recursion.lc46_permutations import Solution


class TestPermutations:
    def test_permute_basic(self):
        sol = Solution()
        result = sol.permute([1, 2, 3])
        expected = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        assert len(result) == len(expected)
        for perm in expected:
            assert perm in result

    def test_permute_single_element(self):
        sol = Solution()
        result = sol.permute([1])
        assert result == [[1]]

    def test_permute_two_elements(self):
        sol = Solution()
        result = sol.permute([1, 2])
        expected = [[1, 2], [2, 1]]
        assert len(result) == len(expected)
        for perm in expected:
            assert perm in result

    def test_permute_empty(self):
        sol = Solution()
        result = sol.permute([])
        assert result == [[]]

    def test_permute_duplicates_allowed(self):
        sol = Solution()
        result = sol.permute([0, 1])
        expected = [[0, 1], [1, 0]]
        assert len(result) == len(expected)
        for perm in expected:
            assert perm in result

