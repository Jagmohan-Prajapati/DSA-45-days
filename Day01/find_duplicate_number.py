<<<<<<< HEAD

# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.There is only one repeated number in nums, return this repeated number.You must solve the problem without modifying the array nums and uses only constant extra space.

 

# Example 1:Input: nums = [1,3,4,2,2]
# Output: 2

# Example 2:Input: nums = [3,1,3,4,2]
# Output: 3

# Example 3:Input: nums = [3,3,3,3,3]
# Output: 3

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        finder = nums[0]
        while finder != slow:
            finder = nums[finder]
            slow = nums[slow]
=======

# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.There is only one repeated number in nums, return this repeated number.You must solve the problem without modifying the array nums and uses only constant extra space.

 

# Example 1:Input: nums = [1,3,4,2,2]
# Output: 2

# Example 2:Input: nums = [3,1,3,4,2]
# Output: 3

# Example 3:Input: nums = [3,3,3,3,3]
# Output: 3

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        finder = nums[0]
        while finder != slow:
            finder = nums[finder]
            slow = nums[slow]
>>>>>>> f7ddbd845e91d3eb417133e3b8af15b449b064c9
        return finder