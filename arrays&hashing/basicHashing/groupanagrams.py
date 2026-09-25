```python
# ============================================================
# DAY 1 — ARRAYS & HASHING
# PROBLEM 4 — GROUP ANAGRAMS
# ============================================================

# Pattern:
# Frequency Hashing / HashMap
#
# Problem:
# Given an array of strings, group the anagrams together.
#
# Example:
#
# strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
#
# Output can be:
#
# [
#     ["eat", "tea", "ate"],
#     ["tan", "nat"],
#     ["bat"]
# ]
#
# Order of the groups does not matter.
#
# Key observation:
#
# Anagrams have exactly the same character frequencies.
#
# "eat" → a:1, e:1, t:1
# "tea" → a:1, e:1, t:1
#
# Therefore, they should have the same key.


# ============================================================
# APPROACH 1 — SORT EACH STRING
# ============================================================

# Idea:
#
# Sort every string.
#
# "eat" → "aet"
# "tea" → "aet"
# "ate" → "aet"
#
# Strings with the same sorted form are anagrams.
#
# We use the sorted string as the HashMap key.
#
# Time Complexity:
# O(n * k log k)
#
# n = number of strings
# k = maximum length of a string
#
# Space Complexity:
# O(n * k)


class Solution:
    def groupAnagrams(self, strs):

        # Dictionary:
        # sorted string → list of anagrams
        groups = {}

        # Process every string
        for word in strs:

            # Sort the characters to create a common key
            #
            # Example:
            # "eat" → "aet"
            # "tea" → "aet"
            key = ''.join(sorted(word))

            # If this key doesn't exist yet,
            # create an empty group
            if key not in groups:
                groups[key] = []

            # Add the original word to its anagram group
            groups[key].append(word)

        # Return all groups
        return list(groups.values())


# ============================================================
# APPROACH 2 — CHARACTER FREQUENCY ⭐
# ============================================================

# Main idea:
#
# Instead of sorting every string, count the frequency
# of each character.
#
# For lowercase English letters, we can create a list
# of 26 counts.
#
# Example:
#
# "eat"
#
# a → 1
# e → 1
# t → 1
#
# The frequency list becomes the key.
#
# All anagrams produce exactly the same frequency key.
#
# Time Complexity:
# O(n * k)
#
# Space Complexity:
# O(n * k)
#
# This is better than sorting because we don't need
# O(k log k) sorting for every string.


class Solution:
    def groupAnagrams(self, strs):

        # Dictionary:
        # frequency pattern → list of anagrams
        groups = {}

        # Process every word
        for word in strs:

            # Create frequency array for 26 lowercase letters
            count = [0] * 26

            # Count each character
            for char in word:

                # Convert character to index:
                #
                # ord('a') - ord('a') = 0
                # ord('b') - ord('a') = 1
                # ...
                # ord('z') - ord('a') = 25
                index = ord(char) - ord('a')

                # Increase frequency of this character
                count[index] += 1

            # Lists cannot be dictionary keys because
            # they are mutable.
            #
            # Convert the frequency list into a tuple
            # so it can be used as a HashMap key.
            key = tuple(count)

            # Create a new group if this frequency pattern
            # has not appeared before
            if key not in groups:
                groups[key] = []

            # Add the original word to its anagram group
            groups[key].append(word)

        # Return all grouped anagrams
        return list(groups.values())


# ============================================================
# WHY DOES THE FREQUENCY KEY WORK?
# ============================================================

# Consider:
#
# "eat"
# "tea"
# "ate"
#
# All contain:
#
# a → 1
# e → 1
# t → 1
#
# Therefore:
#
# frequency("eat")
#      =
# frequency("tea")
#      =
# frequency("ate")
#
# They get the SAME HashMap key.
#
# Therefore, they automatically go into the same group.


# ============================================================
# WHY USE A TUPLE?
# ============================================================

# This will NOT work:
#
# groups[count] = []
#
# because 'count' is a list.
#
# Lists are mutable and cannot be used as dictionary keys.
#
# So we convert:
#
# [1, 0, 1, ...]
#
# into:
#
# (1, 0, 1, ...)
#
# A tuple is immutable and can be used as a HashMap key.


# ============================================================
# INTERVIEW EXPLANATION
# ============================================================

# "The key observation is that two strings are anagrams if
# they have exactly the same character frequencies.
#
# I use a HashMap where the key represents the frequency
# pattern of a string and the value is the list of strings
# having that pattern.
#
# For each word, I count the frequency of its 26 lowercase
# characters and convert that frequency list into a tuple.
# If the tuple already exists, I append the word to that group.
# Otherwise, I create a new group.
#
# This gives O(n*k) time where n is the number of strings and
# k is the maximum string length."


# ============================================================
# PATTERN TO REMEMBER
# ============================================================

# Question:
#
# "Group strings that have the same characters/frequencies."
#
# Think:
#
#             FREQUENCY PATTERN
#                    ↓
#                 HashMap
#                    ↓
#             group together
#
#
# Core idea:
#
# key = character frequency
#
# groups[key].append(word)
#
#
# Common signals:
#
# - Group anagrams
# - Same character composition
# - Same frequency pattern
# - Group elements with the same structure
#
# ============================================================
```

## 🔑 Pattern progression

You've now covered:

```text
1. Contains Duplicate
   → HashSet

2. Two Sum
   → HashMap + Complement

3. Valid Anagram
   → Frequency HashMap

4. Group Anagrams
   → Frequency Pattern + HashMap
```

### The key idea for Group Anagrams

> **If two strings have the same frequency pattern, they belong to the same group.**

For interviews, know **both approaches**, but prioritize the **frequency-array approach** because it gives **O(n × k)** instead of **O(n × k log k)** when the input is restricted to lowercase English letters.
    