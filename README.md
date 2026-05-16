# LeetCode Solutions

A curated collection of my LeetCode solutions, organized by topic and difficulty.

## Overview

This repository contains:
- Accepted LeetCode solutions
- Multiple problem-solving patterns
- Optimized approaches with clean implementations
- Notes for important concepts and tricks

## Languages Used

- Python
- C++
- Java

## Repository Structure

```text
problems/
├── Arrays/
├── Binary Search/
├── Dynamic Programming/
├── Graphs/
├── Greedy/
├── Hashing/
├── Linked List/
├── Math/
├── Sliding Window/
├── Stack/
├── Trees/
└── Two Pointers/
```

---

## Problem Statistics

| Difficulty | Count |
|---|---|
| Easy | 0 |
| Medium | 0 |
| Hard | 0 |

> Statistics update automatically as new solutions are synchronized.

---

## Goals

- Strengthen Data Structures & Algorithms fundamentals
- Prepare for coding interviews
- Improve problem-solving speed and pattern recognition
- Maintain consistency through daily practice

---

## Topics Covered

- Arrays & Strings
- Hash Maps & Sets
- Sliding Window
- Two Pointers
- Binary Search
- Recursion & Backtracking
- Stack & Queue
- Linked Lists
- Trees & BST
- Heaps / Priority Queues
- Graph Algorithms
- Dynamic Programming
- Greedy Algorithms
- Bit Manipulation

---

## Sample Solution Format

```python
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def maxProfit(self, prices):
        min_price = float('inf')
        profit = 0

        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)

        return profit
```

---

## Sync Automation

This repository is automatically synchronized with LeetCode submissions using GitHub Actions.

---

## Profiles

- LeetCode: [your-leetcode-username](https://leetcode.com/)
- GitHub: [your-github-username](https://github.com/)

---

## Progress Tracker

```text
Consistency > Intensity
```

Daily problem solving and revision focused.

---

## Notes

Some solutions may contain:
- Optimized approaches
- Alternative methods
- Pattern explanations
- Edge-case handling

---

## License

This repository is maintained for educational and interview preparation purposes.
