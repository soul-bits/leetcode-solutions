from recursion.lc89_gray_code import Solution


class TestGrayCode:
    def test_n1(self):
        sol = Solution()
        result = sol.grayCode(1)
        assert result == [0, 1] or result == [1, 0]

    def test_n2(self):
        sol = Solution()
        result = sol.grayCode(2)
        # Valid gray code sequences for n=2: [0,1,3,2], [0,2,3,1], [1,0,2,3], etc.
        assert len(result) == 4
        assert set(result) == {0, 1, 2, 3}
        # Check that consecutive numbers differ by exactly one bit
        for i in range(len(result) - 1):
            diff = result[i] ^ result[i + 1]
            assert bin(diff).count('1') == 1

    def test_n3(self):
        sol = Solution()
        result = sol.grayCode(3)
        assert len(result) == 8
        assert set(result) == {0, 1, 2, 3, 4, 5, 6, 7}
        # Check that consecutive numbers differ by exactly one bit
        for i in range(len(result) - 1):
            diff = result[i] ^ result[i + 1]
            assert bin(diff).count('1') == 1

    def test_n0(self):
        sol = Solution()
        result = sol.grayCode(0)
        assert result == [0]

