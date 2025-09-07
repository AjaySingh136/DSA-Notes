# leetcode 303. Range sum query
# question2
"""
# Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.

# Input
# ["NumArray", "sumRange", "sumRange", "sumRange"]
# [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
# Output
# [null, 1, -1, -3]

# Explanation
# NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
# numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
# numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
# numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3

from typing import List
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums.copy()

    def sumRange(self, left: int, right: int) -> int:

        temp_nums = self.nums.copy()
        if right <= len(temp_nums) and left<right:
            left+=1
            for left in range(left,right+1):
                temp_nums[left]+= temp_nums[left-1]
                
            return(temp_nums[left: right+1])
        if left == right or (left-1) == right:
            return temp_nums[right]

        
# Your NumArray object will be instantiated and called as such:
nums = [-2, 0, 3, -5, 2, -1]
# obj = NumArray(nums)
# param_1 = obj.sumRange(0,2)
# param_2 = obj.sumRange(2, 5)
# param_3 = obj.sumRange(0,5)
# param_4 = obj.sumRange(5,6)
# param_5 =  NumArray([-1]).sumRange(0,0)

param_6 =  NumArray([-4,-5]).sumRange(0,1)
# [[[-1]],[0,0]]
# print(param_1, param_2, param_3, param_4)
print(param_6)

"""


# leetcode 525. contiguous array
 