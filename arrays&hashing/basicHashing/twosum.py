
# ============================================================
# DAY 1 — ARRAYS & HASHING
# PROBLEM 2 — TWO SUM
# ============================================================

# Pattern:
# HashMap / Complement
#
# Problem:
# Given an array of integers nums and an integer target,
# return the indices of the two numbers whose sum equals target.
#
# Each input has exactly one solution.
#
# Example:
# nums = [2, 7, 11, 15]
# target = 9
#
# Output:
# [0, 1]
#
# Because:
# nums[0] + nums[1] = 2 + 7 = 9


# ============================================================
# APPROACH 1 — BRUTE FORCE
# ============================================================

# Idea:
# Check every possible pair of numbers.
#
# For every nums[i], compare it with every number after it.
#
# If:
#
# nums[i] + nums[j] == target
#
# we found the answer.
#
# Time Complexity: O(n²)
# Space Complexity: O(1)


class Solution:
    def twoSum(self, nums, target):

        # Try every possible pair
        for i in range(len(nums)):

            for j in range(i + 1, len(nums)):

                # Check whether the current pair
                # adds up to the target
                if nums[i] + nums[j] == target:
                    return [i, j]

        # No valid pair found
        return []


# ============================================================
# APPROACH 2 — HASHMAP ⭐ OPTIMIZED
# ============================================================

# Main idea:
#
# Instead of searching for the second number repeatedly,
# store numbers that we have already seen.
#
# For the current number:
#
# required = target - current
#
# If required is already in the HashMap,
# we have found the answer.
#
# Example:
#
# nums = [2, 7, 11, 15]
# target = 9
#
# Start:
# current = 2
# required = 9 - 2 = 7
#
# 7 is not seen yet → store 2
#
# Next:
# current = 7
# required = 9 - 7 = 2
#
# 2 is already in the HashMap → answer found!


class Solution:
    def twoSum(self, nums, target):

        # Store:
        # number → index
        #
        # This allows us to quickly find
        # whether the required number exists.
        seen = {}

        # Traverse the array only once
        for i in range(len(nums)):

            # Find the number required to reach target
            complement = target - nums[i]

            # If complement was already seen,
            # we have found the required pair
            if complement in seen:
                return [seen[complement], i]

            # Store the current number and its index
            #
            # We store it AFTER checking the complement
            # so we don't use the same element twice.
            seen[nums[i]] = i

        # No solution found
        return []


# ============================================================
# WHY HASHMAP?
# ============================================================

# Brute force:
#
# For every number, we search through the rest of the array.
# This takes O(n²) time.
#
# HashMap:
#
# We store previously seen numbers.
# Looking up a number in a HashMap takes O(1) average time.
#
# Therefore, we only need one pass through the array.
#
# Brute Force → O(n²) time, O(1) space
#
# HashMap → O(n) time, O(n) space


# ============================================================
# THE MOST IMPORTANT IDEA — COMPLEMENT
# ============================================================

# When the problem says:
#
# "Find two numbers that add up to target"
#
# Don't immediately think:
#
# "Which two numbers?"
#
# Think:
#
# "What number do I NEED?"
#
# For every nums[i]:
#
# complement = target - nums[i]
#
# Then ask:
#
# "Have I already seen this complement?"
#
# If YES → answer found
# If NO  → store current number


# ============================================================
# INTERVIEW EXPLANATION
# ============================================================

# "A brute-force solution would check every pair of elements,
# which takes O(n²) time.
#
# To optimize it, I use a HashMap to store the numbers I have
# already seen along with their indices.
#
# For each current number, I calculate its complement as
# target - current number.
#
# If that complement is already present in the HashMap,
# I return the stored index and the current index.
# Otherwise, I store the current number and continue.
#
# This allows me to solve the problem in O(n) time using
# O(n) extra space."


# ============================================================
# PATTERN TO REMEMBER
# ============================================================

# Question:
#
# "Find two values that satisfy a target condition."
#
# Think:
#
#             COMPLEMENT
#                 ↓
#          target - current
#                 ↓
#              HashMap
#
#
# Core template:
#
# seen = {}
#
# for i in range(len(nums)):
#
#     complement = target - nums[i]
#
#     if complement in seen:
#         return [seen[complement], i]
#
#     seen[nums[i]] = i
#
#
# Common signals:
#
# - Two numbers
# - Target sum
# - Find a pair
# - Need indices
# - Fast lookup
#
# ============================================================


### 🔑 What you should remember
"""
**Two Sum → Complement → HashMap**

The key line is:

```python
complement = target - nums[i]
```

Then:

```python
if complement in seen:
```

That's the **actual pattern** you want to recognize in a new OA problem—not just memorize the Two Sum code.

**Next Day 1 problem → Valid Anagram: Frequency Hashing.**
"""