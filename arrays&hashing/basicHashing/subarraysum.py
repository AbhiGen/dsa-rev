
# ============================================================
# DAY 2 — ARRAYS & HASHING
# PROBLEM 6 — SUBARRAY SUM EQUALS K
# ============================================================

# Pattern:
# Prefix Sum + HashMap
#
# Problem:
# Given an integer array nums and an integer k,
# return the total number of subarrays whose sum equals k.
#
# A subarray must be CONTIGUOUS.
#
# Example:
#
# nums = [1, 1, 1]
# k = 2
#
# Subarrays with sum 2:
#
# [1, 1]  → indices 0,1
# [1, 1]  → indices 1,2
#
# Answer = 2


# ============================================================
# APPROACH 1 — BRUTE FORCE
# ============================================================

# Idea:
# Try every possible starting point and calculate
# the sum of every subarray.
#
# Time Complexity: O(n²)
# Space Complexity: O(1)


class Solution:
    def subarraySum(self, nums, k):

        count = 0

        # Choose the starting position
        for i in range(len(nums)):

            current_sum = 0

            # Extend the subarray from i
            for j in range(i, len(nums)):

                # Add the current element
                current_sum += nums[j]

                # If the current subarray has sum k,
                # we found one valid subarray
                if current_sum == k:
                    count += 1

        return count


# ============================================================
# APPROACH 2 — PREFIX SUM + HASHMAP ⭐ OPTIMIZED
# ============================================================

# Main idea:
#
# Let:
#
# prefix_sum = sum of elements from the beginning
#              up to the current position
#
# Suppose:
#
# current_prefix - previous_prefix = k
#
# Then:
#
# previous_prefix = current_prefix - k
#
# Therefore, while traversing the array, we check whether
# current_prefix - k has appeared before.
#
# If it has appeared x times, then there are x subarrays
# ending at the current position whose sum is k.
#
# Time Complexity: O(n)
# Space Complexity: O(n)


class Solution:
    def subarraySum(self, nums, k):

        # Store:
        # prefix_sum → number of times it has appeared
        #
        # Prefix sum 0 appears once before we process
        # any elements.
        prefix_count = {0: 1}

        # Current prefix sum
        prefix_sum = 0

        # Number of valid subarrays
        count = 0

        # Traverse the array once
        for num in nums:

            # Add current number to the running prefix sum
            prefix_sum += num

            # We need an earlier prefix sum such that:
            #
            # current_prefix - previous_prefix = k
            #
            # Therefore:
            #
            # previous_prefix = current_prefix - k
            required = prefix_sum - k

            # If this prefix sum appeared before,
            # every occurrence gives us one valid subarray
            if required in prefix_count:
                count += prefix_count[required]

            # Store the current prefix sum for future subarrays
            prefix_count[prefix_sum] = (
                prefix_count.get(prefix_sum, 0) + 1
            )

        return count


# ============================================================
# WHY DOES prefix_sum - k WORK?
# ============================================================

# Suppose:
#
# nums = [1, 2, 3]
# k = 5
#
# At 3:
#
# prefix_sum = 6
#
# We need:
#
# previous_prefix = 6 - 5
#                 = 1
#
# We previously had prefix sum 1:
#
# [1]
#
# Current prefix:
#
# [1, 2, 3] = 6
#
# Therefore:
#
# 6 - 1 = 5
#
# The subarray:
#
# [2, 3]
#
# has sum 5.
#
# This is the core idea of the problem.


# ============================================================
# WHY prefix_count = {0: 1}?
# ============================================================

# This is VERY important.
#
# Suppose:
#
# nums = [5]
# k = 5
#
# After processing 5:
#
# prefix_sum = 5
#
# required = 5 - 5
#          = 0
#
# We need prefix sum 0 to already exist.
#
# That represents the empty prefix before the array starts.
#
# Therefore:
#
# prefix_count = {0: 1}
#
# This allows us to correctly count subarrays
# that start from index 0.


# ============================================================
# WHY DO WE ADD prefix_count[required]?
# ============================================================

# We don't simply do:
#
# count += 1
#
# because the same prefix sum can occur multiple times.
#
# Example:
#
# prefix_sum = 5
#
# If prefix_sum - k appeared 3 times before,
# then there are 3 different subarrays ending here
# whose sum is k.
#
# Therefore:
#
# count += prefix_count[required]


# ============================================================
# INTERVIEW EXPLANATION
# ============================================================

# "A brute-force solution would check every possible
# subarray and take O(n²) time.
#
# I can optimize this using prefix sums and a HashMap.
#
# If the current prefix sum is P, then I need an earlier
# prefix sum of P-k so that:
#
# P - (P-k) = k
#
# I store each prefix sum and the number of times it has
# occurred in a HashMap.
#
# Whenever prefix_sum-k exists in the map, I add its
# frequency to the answer.
#
# I initialize the map with {0: 1} to handle subarrays
# starting from index 0.
#
# This gives O(n) time and O(n) space."


# ============================================================
# PATTERN TO REMEMBER
# ============================================================

# Question:
#
# "Count contiguous subarrays with a target sum."
#
# Think:
#
#          PREFIX SUM
#               +
#            HASHMAP
#
#
# Core formula:
#
# required = prefix_sum - k
#
#
# Core template:
#
# prefix_count = {0: 1}
# prefix_sum = 0
# count = 0
#
# for num in nums:
#
#     prefix_sum += num
#
#     required = prefix_sum - k
#
#     if required in prefix_count:
#         count += prefix_count[required]
#
#     prefix_count[prefix_sum] = \
#         prefix_count.get(prefix_sum, 0) + 1
#
#
# Common signals:
#
# - Subarray
# - Contiguous
# - Target sum
# - Count number of subarrays
# - Negative numbers may be present
#
# ============================================================
```

### 🔑 The one thing to memorize

```text
Current Prefix Sum - Previous Prefix Sum = K

Therefore:

Previous Prefix Sum = Current Prefix Sum - K
```

So whenever you see:

> **"Number of contiguous subarrays with sum K"**

think immediately:

**Prefix Sum + HashMap → `prefix_sum - k`**

**Complexity:** `O(n)` time, `O(n)` space.

After this, your next problem is **Continuous Subarray Sum**, which uses the same prefix-sum idea but introduces the **remainder/modulo** pattern.
