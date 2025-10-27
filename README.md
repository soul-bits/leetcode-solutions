# LeetCode Solutions

![CI](https://github.com/soul-bits/leetcode-solutions/workflows/CI/badge.svg)

A collection of LeetCode problem solutions, focusing on recursion and algorithmic problem-solving.

## Problems

| # | Problem | Category | LeetCode | Solution | YouTube |
|---|---------|----------|----------|----------|---------|
| 46 | Permutations | Recursion | [View](https://leetcode.com/problems/permutations/) | [lc46_permutations.py](recursion/lc46_permutations.py) | 🔗 |
| 78 | Subsets | Recursion | [View](https://leetcode.com/problems/subsets/) | [lc78_subsequences_of_string.py](recursion/lc78_subsequences_of_string.py) | [Watch](https://youtu.be/_pOyA0v93rI) |

## Running Solutions

Each file can be run independently:

```bash
python recursion/lc46_permutations.py
python recursion/lc78_subsequences_of_string.py
```

## Running Tests

Install dependencies:

```bash
pip install -r requirements.txt
```

Run all tests:

```bash
pytest
```

Run tests for a specific file:

```bash
pytest recursion/test_lc46_permutations.py
pytest recursion/test_lc78_subsequences_of_string.py
```

