from recursion.lc90_subsets_ii import Solution


class TestSubsetsII:
    def test_subsets_with_dup_basic(self):
        sol = Solution()
        result = sol.subsetsWithDup([1, 2, 2])
        expected = [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
        assert len(result) == len(expected)
        for subset in expected:
            assert subset in result

    def test_subsets_with_dup_no_duplicates(self):
        sol = Solution()
        result = sol.subsetsWithDup([1, 2, 3])
        expected = [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
        assert len(result) == len(expected)
        for subset in expected:
            assert subset in result

    def test_subsets_with_dup_single_element(self):
        sol = Solution()
        result = sol.subsetsWithDup([1])
        expected = [[], [1]]
        assert len(result) == len(expected)
        for subset in expected:
            assert subset in result

    def test_subsets_with_dup_empty(self):
        sol = Solution()
        result = sol.subsetsWithDup([])
        assert result == [[]]

    def test_subsets_with_dup_multiple_duplicates(self):
        sol = Solution()
        result = sol.subsetsWithDup([1, 1, 2, 2])
        # Should have unique subsets only
        assert len(result) == 9
        expected = [
            [], [1], [1, 1], [1, 1, 2], [1, 1, 2, 2],
            [1, 2], [1, 2, 2], [2], [2, 2]
        ]
        for subset in expected:
            assert subset in result

    def test_subsets_with_dup_all_same(self):
        sol = Solution()
        result = sol.subsetsWithDup([2, 2, 2])
        expected = [[], [2], [2, 2], [2, 2, 2]]
        assert len(result) == len(expected)
        for subset in expected:
            assert subset in result

    def test_subsets_with_dup_three_duplicates(self):
        sol = Solution()
        result = sol.subsetsWithDup([4, 4, 4, 1, 4])
        # After sorting: [1, 4, 4, 4, 4]
        assert len(result) == 10
        # Verify some key subsets
        assert [] in result
        assert [1] in result
        assert [1, 4] in result
        assert [1, 4, 4, 4, 4] in result
        assert [4, 4, 4, 4] in result

