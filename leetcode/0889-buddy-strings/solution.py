class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        
        if len(s) != len(goal):
            return False

        if s == goal:
            # Check for at least one duplicate letter
            return len(set(s)) < len(s)

        # Find the indices where characters differ
        diff = [(a, b) for a, b in zip(s, goal) if a != b]

        # Must have exactly two mismatches, and they must be swappable
        return len(diff) == 2 and diff[0] == diff[1][::-1]
