
# ============================================================
# DAY 1 — ARRAYS & HASHING
# PROBLEM 3 — VALID ANAGRAM
# ============================================================

# Pattern:
# Frequency Hashing / HashMap
#
# Problem:
# Given two strings s and t, return True if t is an anagram
# of s. Otherwise, return False.
#
# An anagram contains exactly the same characters with the
# same frequencies, but the order can be different.
#
# Example:
#
# s = "anagram"
# t = "nagaram"
#
# Output: True
#
# Example:
#
# s = "rat"
# t = "car"
#
# Output: False


# ============================================================
# APPROACH 1 — SORTING
# ============================================================

# Idea:
# Two strings are anagrams if their sorted versions are equal.
#
# Example:
#
# "anagram" → "aaagmnr"
# "nagaram" → "aaagmnr"
#
# Therefore, they are anagrams.
#
# Time Complexity: O(n log n)
# Space Complexity: O(n)
#
# The space depends on the sorting implementation / converted
# character arrays.


class Solution:
    def isAnagram(self, s, t):

        # Anagrams must have the same number of characters
        if len(s) != len(t):
            return False

        # Sort both strings.
        # If they contain the same characters with the same
        # frequencies, their sorted versions will be identical.
        return sorted(s) == sorted(t)


# ============================================================
# APPROACH 2 — FREQUENCY HASHMAP ⭐ OPTIMIZED
# ============================================================

# Main idea:
#
# Instead of sorting, count how many times each character
# appears in both strings.
#
# Example:
#
# s = "aabbc"
#
# Frequency:
# a → 2
# b → 2
# c → 1
#
# If t has exactly the same frequency map,
# then t is an anagram of s.
#
# Time Complexity: O(n)
# Space Complexity: O(n)


class Solution:
    def isAnagram(self, s, t):

        # Different lengths mean they cannot contain
        # the same characters with the same frequencies
        if len(s) != len(t):
            return False

        # Store character frequencies
        count = {}

        # Count characters from s
        for char in s:

            # Increase the frequency of this character
            count[char] = count.get(char, 0) + 1

        # Process characters from t
        for char in t:

            # If the character does not exist in s,
            # t cannot be an anagram
            if char not in count:
                return False

            # Use one occurrence of this character
            count[char] -= 1

            # If frequency becomes negative,
            # t contains this character too many times
            if count[char] < 0:
                return False

        # All character frequencies matched
        return True


# ============================================================
# ALTERNATIVE — TWO FREQUENCY MAPS
# ============================================================

# Another easy way to understand the same idea:
#
# Create one frequency map for s
# Create another frequency map for t
#
# Then compare both maps.
#
# Time Complexity: O(n)
# Space Complexity: O(n)


class Solution:
    def isAnagram(self, s, t):

        # Different lengths → impossible
        if len(s) != len(t):
            return False

        count_s = {}
        count_t = {}

        # Count characters in s
        for char in s:
            count_s[char] = count_s.get(char, 0) + 1

        # Count characters in t
        for char in t:
            count_t[char] = count_t.get(char, 0) + 1

        # Both strings must have exactly the same
        # character frequencies
        return count_s == count_t


# ============================================================
# WHY FREQUENCY HASHING?
# ============================================================

# The important question is:
#
# "Do both strings contain the same characters
#  with the same frequencies?"
#
# So instead of comparing every character with every other
# character, we count how often each character occurs.
#
# HashMap gives approximately O(1) average-time access.
#
# Therefore:
#
# Sorting approach  → O(n log n)
# HashMap approach  → O(n)


# ============================================================
# INTERVIEW EXPLANATION
# ============================================================

# "First, I check whether the two strings have the same length.
# If they don't, they cannot be anagrams.
#
# Then I use a HashMap to count the frequency of every
# character in the first string.
#
# While processing the second string, I decrease the frequency
# of each character. If a character doesn't exist or its
# frequency becomes negative, the strings are not anagrams.
#
# If all characters match, the strings are anagrams.
#
# This takes O(n) time and O(n) space."


# ============================================================
# PATTERN TO REMEMBER
# ============================================================

# Question:
#
# "Do two strings/arrays contain the same elements
#  with the same frequencies?"
#
# Think:
#
#              FREQUENCY MAP
#                    ↓
#             element → count
#
#
# Core template:
#
# freq = {}
#
# for x in arr:
#     freq[x] = freq.get(x, 0) + 1
#
#
# Common signals:
#
# - Anagram
# - Same characters
# - Same elements
# - Frequency
# - Count occurrences
# - Compare frequencies
#
# ============================================================
```

## 🔑 Pattern to remember

**Anagram → Frequency Map**

The key idea is:

```text
character → frequency
```

And your progression so far is:

```text
1. Contains Duplicate → HashSet
2. Two Sum            → HashMap / Complement
3. Valid Anagram      → Frequency HashMap
```

**Next → Group Anagrams**, where you'll use the **same frequency idea**, but instead of checking two strings, you'll group many strings based on their character pattern.
