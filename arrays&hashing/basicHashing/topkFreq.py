```python
# ============================================================
# DAY 1 — ARRAYS & HASHING
# PROBLEM 5 — TOP K FREQUENT ELEMENTS
# ============================================================

# Pattern:
# Frequency HashMap + Heap
#
# Problem:
# Given an integer array nums and an integer k,
# return the k most frequent elements.
#
# Example:
#
# nums = [1, 1, 1, 2, 2, 3]
# k = 2
#
# Output:
# [1, 2]
#
# Because:
#
# 1 → appears 3 times
# 2 → appears 2 times
# 3 → appears 1 time
#
# The 2 most frequent elements are 1 and 2.


# ============================================================
# APPROACH 1 — FREQUENCY MAP + SORTING
# ============================================================

# Idea:
#
# Step 1:
# Count how many times each number appears.
#
# Step 2:
# Sort the numbers according to their frequency.
#
# Step 3:
# Return the first k elements.
#
# Time Complexity:
# O(n log n)
#
# Space Complexity:
# O(n)


class Solution:
    def topKFrequent(self, nums, k):

        # Store:
        # number → frequency
        freq = {}

        # Count frequency of every number
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # Sort numbers based on their frequency
        # from highest to lowest
        sorted_nums = sorted(
            freq,
            key=freq.get,
            reverse=True
        )

        # Return the k most frequent numbers
        return sorted_nums[:k]


# ============================================================
# APPROACH 2 — FREQUENCY MAP + MIN HEAP ⭐
# ============================================================

# Main idea:
#
# We need only the TOP K elements.
#
# Instead of sorting ALL elements, we can maintain
# a Min Heap containing only k elements.
#
# Steps:
#
# 1. Count frequencies using HashMap.
# 2. Add each (frequency, number) to a Min Heap.
# 3. If heap size becomes greater than k,
#    remove the least frequent element.
# 4. At the end, the heap contains the k most frequent elements.
#
# Time Complexity:
# O(n log k)
#
# Space Complexity:
# O(n + k)
#
# This is especially useful when k is much smaller than n.


import heapq


class Solution:
    def topKFrequent(self, nums, k):

        # Store:
        # number → frequency
        freq = {}

        # Count frequency of every number
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # Min Heap:
        # Stores (frequency, number)
        heap = []

        # Process every unique number
        for num, count in freq.items():

            # Add the current element and its frequency
            heapq.heappush(heap, (count, num))

            # Keep only k elements in the heap
            #
            # The smallest frequency is removed first.
            if len(heap) > k:
                heapq.heappop(heap)

        # Extract the numbers from the heap
        result = []

        for count, num in heap:
            result.append(num)

        return result


# ============================================================
# WHY MIN HEAP?
# ============================================================

# We only care about the TOP K elements.
#
# Suppose:
#
# k = 2
#
# Instead of keeping every element sorted, we maintain
# a heap containing only the best 2 elements.
#
# Whenever the heap contains 3 elements:
#
#     Remove the smallest frequency
#
# Therefore, the heap always keeps the current top k elements.
#
# This changes:
#
# Sorting:
# O(n log n)
#
# Heap:
# O(n log k)
#
# When k is small compared to n, this is more efficient.


# ============================================================
# WHY MIN HEAP INSTEAD OF MAX HEAP?
# ============================================================

# This may seem confusing:
#
# "We want the MOST frequent elements.
#  Why use a MIN Heap?"
#
# Because we want the LEAST frequent element among our
# current k elements to be easy to remove.
#
# Example:
#
# k = 3
#
# Heap contains:
#
# frequency 2
# frequency 5
# frequency 7
#
# If a new element has frequency 10:
#
# Add 10
#
# Now we have:
# 2, 5, 7, 10
#
# Remove the smallest → 2
#
# Remaining:
# 5, 7, 10
#
# These are our current top 3.


# ============================================================
# INTERVIEW EXPLANATION
# ============================================================

# "First, I count the frequency of every element using a
# HashMap.
#
# Since I only need the k most frequent elements, I maintain
# a Min Heap of size k.
#
# For every unique element, I insert its frequency and value
# into the heap. If the heap size becomes greater than k,
# I remove the element with the smallest frequency.
#
# Therefore, after processing all elements, the heap contains
# the k most frequent elements.
#
# The time complexity is O(n log k), and the space complexity
# is O(n + k)."


# ============================================================
# PATTERN TO REMEMBER
# ============================================================

# Question:
#
# "Find the TOP K / KTH largest / KTH smallest..."
#
# Think:
#
#              HEAP
#
# For TOP K:
#
#       Frequency Map
#              ↓
#           Min Heap
#              ↓
#          Keep K
#
#
# Common signals:
#
# - Top K frequent
# - Kth largest
# - Kth smallest
# - K closest
# - Keep only K best elements
#
# ============================================================
```

## 🔑 What you should remember

The pattern is:

```text
Frequency problem
        ↓
   HashMap
        ↓
     Top K
        ↓
    Min Heap
```

And the important complexity improvement is:

```text
Sorting → O(n log n)

Min Heap → O(n log k)
```

### 🎯 Day 1 is now complete

You've covered:

```text
✅ 1. Contains Duplicate
   → HashSet

✅ 2. Two Sum
   → HashMap + Complement

✅ 3. Valid Anagram
   → Frequency HashMap

✅ 4. Group Anagrams
   → Frequency Pattern + HashMap

✅ 5. Top K Frequent Elements
   → Frequency HashMap + Min Heap
```

**Don't start the next topic yet.** First try to solve these 5 again without looking at your files. Then commit today's work to GitHub.

