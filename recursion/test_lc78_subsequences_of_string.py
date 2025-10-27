import pytest
from lc78_subsequences_of_string import generate_subsequences


class TestSubsequences:
    def test_generate_subsequences_basic(self):
        result = generate_subsequences("abc")
        expected = ["", "a", "b", "c", "ab", "ac", "bc", "abc"]
        assert len(result) == len(expected)
        for subseq in expected:
            assert subseq in result

    def test_generate_subsequences_single_char(self):
        result = generate_subsequences("a")
        expected = ["", "a"]
        assert len(result) == len(expected)
        for subseq in expected:
            assert subseq in result

    def test_generate_subsequences_empty_string(self):
        result = generate_subsequences("")
        assert result == [""]

    def test_generate_subsequences_two_chars(self):
        result = generate_subsequences("ab")
        expected = ["", "a", "b", "ab"]
        assert len(result) == len(expected)
        for subseq in expected:
            assert subseq in result

    def test_generate_subsequences_numeric(self):
        result = generate_subsequences("12")
        expected = ["", "1", "2", "12"]
        assert len(result) == len(expected)
        for subseq in expected:
            assert subseq in result

