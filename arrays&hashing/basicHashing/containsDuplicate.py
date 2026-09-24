
# ============================================================
# DAY 1 — ARRAYS & HASHING
# PROBLEM 1 — CONTAINS DUPLICATE
# ============================================================

# Pattern:
# HashSet / Basic Hashing
#
# Problem:
# Given an integer array nums, return True if any value
# appears at least twice. Otherwise, return False.
#
# Example:
# nums = [1, 2, 3, 1]
# Output: True
#
# nums = [1, 2, 3, 4]
# Output: False


# ============================================================
# APPROACH 1 — BRUTE FORCE
# ============================================================

# Idea:
# Compare every element with every other element.
#
# If nums[i] == nums[j], we found a duplicate.
#
# Time Complexity: O(n²)
# Space Complexity: O(1)

class Solution:
    def containsDuplicate(self, nums):
        
        # Compare every pair of elements
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):

                # If two different positions contain
                # the same value, it is a duplicate
                if nums[i] == nums[j]:
                    return True

        # No duplicate was found
        return False


# ============================================================
# APPROACH 2 — HASHSET ⭐ OPTIMIZED
# ============================================================

# Pattern:
# "Have I seen this element before?"
#              ↓
#           HashSet
#
# A HashSet gives approximately O(1) average-time lookup.
#
# We scan the array once:
#
# If number is already in the set:
#     → duplicate found
#
# Otherwise:
#     → add it to the set
#
# Time Complexity: O(n)
# Space Complexity: O(n)


class Solution:
    def containsDuplicate(self, nums):

        # Store all numbers that we have already seen
        seen = set()

        # Traverse the array once
        for num in nums:

            # If num is already present,
            # we have encountered the same number before
            if num in seen:
                return True

            # Otherwise, remember this number
            # for future comparisons
            seen.add(num)

        # We checked the entire array
        # and found no duplicate
        return False


# ============================================================
# WHY HASHSET?
# ============================================================

# Without a HashSet:
# We would have to repeatedly compare elements → O(n²)
#
# With a HashSet:
# We can quickly check whether an element already exists.
#
# Therefore:
#
# Brute Force  → O(n²) time, O(1) space
# HashSet      → O(n) time, O(n) space
#
# We choose HashSet because the problem is essentially asking:
#
# "Have I seen this value before?"


# ============================================================
# INTERVIEW EXPLANATION
# ============================================================

# "I need to determine whether any element appears more than
# once. A brute-force solution would compare every pair and
# take O(n²) time.
#
# Instead, I use a HashSet to store elements I have already
# seen. While traversing the array, if the current element is
# already in the set, I immediately return True. Otherwise,
# I add it to the set.
#
# This reduces the time complexity to O(n) with O(n) extra
# space."


# ============================================================
# PATTERN TO REMEMBER
# ============================================================

# Question:
# "Have I seen this element before?"
#
# Think:
#
#              HashSet
#
# Common signals:
# - Duplicate detection
# - Already seen?
# - Unique elements
# - Fast membership checking
#
# Core template:
#
# seen = set()
#
# for x in nums:
#     if x in seen:
#         ...
#     seen.add(x)
#
# ============================================================
