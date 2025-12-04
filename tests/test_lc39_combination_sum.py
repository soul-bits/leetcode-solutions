from recursion.lc39_combination_sum import Solution


class TestCombinationSum:
    def test_example1(self):
        sol = Solution()
        candidates = [2, 3, 6, 7]
        target = 7
        result = sol.combinationSum(candidates, target)
        expected = [[2, 2, 3], [7]]
        assert len(result) == len(expected)
        for comb in expected:
            assert comb in result

    def test_example2(self):
        sol = Solution()
        candidates = [2, 3, 5]
        target = 8
        result = sol.combinationSum(candidates, target)
        expected = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
        assert len(result) == len(expected)
        for comb in expected:
            assert comb in result

    def test_example3(self):
        sol = Solution()
        candidates = [2]
        target = 1
        result = sol.combinationSum(candidates, target)
        assert result == []

    def test_empty_candidates(self):
        sol = Solution()
        candidates = []
        target = 7
        result = sol.combinationSum(candidates, target)
        assert result == []

    def test_no_combination(self):
        sol = Solution()
        candidates = [5, 10]
        target = 3
        result = sol.combinationSum(candidates, target)
        assert result == []

    def test_single_candidate_multiple_times(self):
        sol = Solution()
        candidates = [2]
        target = 4
        result = sol.combinationSum(candidates, target)
        assert result == [[2, 2]]

    def test_target_equals_single_candidate(self):
        sol = Solution()
        candidates = [3]
        target = 3
        result = sol.combinationSum(candidates, target)
        assert result == [[3]]

