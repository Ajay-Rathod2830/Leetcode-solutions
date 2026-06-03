# Two Sum

## Problem Statement

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to the target.

You may assume that each input has exactly one solution, and you may not use the same element twice.

### Example

Input:

```python
nums = [2, 7, 11, 15]
target = 9
```

Output:

```python
[0, 1]
```

Explanation:

```python
nums[0] + nums[1] = 2 + 7 = 9
```

## Approach

A hash map is used to store previously visited numbers and their indices.

For each element:

1. Calculate the required complement:

   ```python
   complement = target - nums[i]
   ```
2. Check if the complement already exists in the hash map.
3. If found, return the indices.
4. Otherwise, store the current number and its index.

## Solution (Python)

```python
class Solution:
    def twoSum(self, nums, target):
        hash_map = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in hash_map:
                return [hash_map[complement], i]

            hash_map[nums[i]] = i
```

## Complexity Analysis

* Time Complexity: O(n)
* Space Complexity: O(n)

## Key Concept

The optimal solution uses a hash map to achieve constant-time lookups, reducing the time complexity from O(n²) to O(n).
