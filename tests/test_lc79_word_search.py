from recursion.lc79_word_search import Solution


class TestWordSearch:
    def test_exist_basic(self):
        sol = Solution()
        board = [
            ["A","B","C","E"],
            ["S","F","C","S"],
            ["A","D","E","E"]
        ]
        assert sol.exist(board, "ABCCED") == True
        assert sol.exist(board, "SEE") == True
        assert sol.exist(board, "ABCB") == False

    def test_exist_single_char(self):
        sol = Solution()
        board = [["A"]]
        assert sol.exist(board, "A") == True
        assert sol.exist(board, "B") == False

    def test_exist_single_row(self):
        sol = Solution()
        board = [["A","B","C"]]
        assert sol.exist(board, "ABC") == True
        assert sol.exist(board, "CBA") == False
        assert sol.exist(board, "AB") == True

    def test_exist_single_column(self):
        sol = Solution()
        board = [["A"], ["B"], ["C"]]
        assert sol.exist(board, "ABC") == True
        assert sol.exist(board, "CBA") == False
        assert sol.exist(board, "AB") == True

    def test_exist_no_path(self):
        sol = Solution()
        board = [
            ["A","B"],
            ["C","D"]
        ]
        assert sol.exist(board, "ACDB") == True
        assert sol.exist(board, "ABCD") == False

    def test_exist_reuse_cell(self):
        sol = Solution()
        board = [
            ["A","B","C"],
            ["D","E","F"],
            ["G","H","I"]
        ]
        # Should not reuse same cell
        assert sol.exist(board, "ABE") == True
        assert sol.exist(board, "ABA") == False

    def test_exist_long_word(self):
        sol = Solution()
        board = [
            ["A","B","C","D"],
            ["E","F","G","H"],
            ["I","J","K","L"],
            ["M","N","O","P"]
        ]
        assert sol.exist(board, "ABCDHLPONMIEFG") == True
        assert sol.exist(board, "ABCDHLPONMIEFGX") == False

    def test_exist_duplicate_letters(self):
        sol = Solution()
        board = [
            ["A","A","A"],
            ["A","A","A"],
            ["A","A","A"]
        ]
        assert sol.exist(board, "AAAAA") == True
        assert sol.exist(board, "AAAAAA") == True
        assert sol.exist(board, "AAAAAAAAA") == True

    def test_exist_small_board(self):
        sol = Solution()
        board = [
            ["A","B"],
            ["C","D"]
        ]
        assert sol.exist(board, "AB") == True
        assert sol.exist(board, "AC") == True
        assert sol.exist(board, "BD") == True
        assert sol.exist(board, "CD") == True

