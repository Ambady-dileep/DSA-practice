# # FIRST APPROACH - If the lengths differ, then duplicates existed.
# def containsDuplicate(nums):
#     return len(nums) != len(set(nums))

# nums = [1,2,4,2,3]
# print(containsDuplicate(nums))

# # SECOND APPROACH
# def containsDuplicate(nums):
#     seen = set()
#     for num in nums:
#         if num in seen:
#             return True
#         seen.add(num)
#     return False
# nums = [1,6,4,2,3]
# print(containsDuplicate(nums))
