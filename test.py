# class Solution:
#     def differenceOfSums(self, n: int, m: int) -> int:
#         num1 = sum([i for i in range(1, n + 1) if i % m])
#         num2 = sum([i for i in range(1, n + 1) if not i % m])
#         return num1 - num2


# # Two Sum
# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         seen = {}
#         for i, num in enumerate(nums):
#             complement = target - num
#             if complement in seen:
#                 return [seen[complement], i]
#             seen[num] = i


# # Add Two Numbers
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# class Solution:
#     def addTwoNumbers(
#         self, l1: Optional[ListNode], l2: Optional[ListNode]
#     ) -> Optional[ListNode]:
#         dummy = ListNode()
#         current = dummy
#         carry = 0

#         while l1 or l2 or carry:
#             val1 = l1.val if l1 else 0
#             val2 = l2.val if l2 else 0

#             total = val1 + val2 + carry
#             carry = total // 10
#             digit = total % 10

#             current.next = ListNode(digit)
#             current = current.next

#             if l1:
#                 l1 = l1.next
#             if l2:
#                 l2 = l2.next

#         return dummy.next


# l1 = [9, 9, 9, 9, 9, 9, 9]
# l2 = [9, 9, 9, 9]
# object = Solution()
# object.addTwoNumbers(l1, l2)


def lengthOfLongestSubstring(s: str) -> int:
    substrings = set()
    current = ""
    for i in s:
        if i not in current:
            current += i
        else:
            substrings.add(current)
            current = ""
            current += i
    return len(max(substrings, key=len))


print(lengthOfLongestSubstring("bbbbb"))
