from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# TEMPLATES:

# BACKTRACKING:
# https://algo.monster/problems/backtracking

# DP:
# https://patterns.eecs.berkeley.edu/?page_id=416

class Solution:
    def test(self):
        n: List = []
        n1: Optional = []

    # def quicksort(self, array: List[int], low: int, high: int):
    #     if low < high:
    #         pi = self._quicksort_partition(array, low, high)
    #         self.quicksort(array, low, pi - 1)
    #         self.quicksort(array, pi, high)
    #
    #
    # def _quicksort_partition(self, array: List[int], low: int, high: int):
    #     # pivot is right last element
    #     pivot = array[high]
    #     i = low - 1
    #
    #     for j in range(low, high):
    #         if array[j] <= pivot:
    #             i = i + 1
    #             array[i], array[j] = array[j], array[i]
    #
    #     array[i + 1], array[high] = array[high], array[i + 1]
    #     return i + 1
    #
    #
    # def recursive_fibo(self, n):
    #     if n <= 1:
    #         return n
    #     return self.recursive_fibo(n - 1) + self.recursive_fibo(n - 2)
    #
    #
    # def normal_fibo(self, n):
    #     a = 0
    #     b = 1
    #     for i in range(2, n + 1):
    #         c = a + b
    #         a = b
    #         b = c
    #
    #     return b
    #
    #
    # def mergesort(self, arr):
    #     # PARTITION STEP
    #     # divide array in half and divide all halves until only one element remains in each left and right array
    #     if len(arr) > 1:
    #         # split the array in 2 parts
    #         middle = len(arr) // 2
    #         left_arr = arr[:middle]
    #         right_arr = arr[middle:]
    #
    #         # call mergesort recursively, split array in multiple one size arrays
    #         self.mergesort(left_arr)
    #         self.mergesort(right_arr)
    #
    #         # MERGE STEP
    #         i = 0  # left arr indx
    #         j = 0  # right arr indx
    #         k = 0  # merged array indx
    #         while i < len(left_arr) and j < len(right_arr):
    #             if left_arr[i] < right_arr[j]:
    #                 arr[k] = left_arr[i]
    #                 i += 1
    #             else:
    #                 arr[k] = right_arr[j]
    #                 j += 1
    #             k += 1
    #
    #         # if left array still has items
    #         while i < len(left_arr):
    #             arr[k] = left_arr[i]
    #             i += 1
    #             k += 1
    #
    #         while j < len(right_arr):
    #             arr[k] = right_arr[j]
    #             j += 1
    #             k += 1
    #
    #
    # def binary_search_iterative(self, arr, target):
    #     left = 0
    #     right = len(arr) - 1
    #     while left <= right:
    #         mid = (left + right) // 2
    #         if arr[mid] == target:
    #             return mid
    #
    #         if target < arr[mid]:
    #             right = mid - 1
    #         else:
    #             left = mid + 1
    #     return -1

    # 83 - Remove duplicates from Sorted List
    # loop over the list and check if current node has the same values with the one in current.next
    # if they have the same values then current.next should point to the next node for checking
    # if they have different values then move to the next node
    # def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     current = head
    #     while current and current.next:
    #         next_node = current.next
    #         if current.val == next_node.val:
    #             current.next = next_node.next
    #             next_node.next = None
    #         else:
    #             current = current.next
    #
    #     return head

    # 88. Merge Sorted Array
    # We can start with two pointers i and j, initialized to m-1 and n-1, respectively. We will also have another pointer k initialized to m+n-1, which will be used to keep track of the position in nums1 where we will be placing the larger
    # element. Then we can start iterating from the end of the arrays i and j, and compare the elements at these positions. We will place the larger element in nums1 at position k, and decrement the corresponding pointer i or j accordingly. We
    # will continue doing this until we have iterated through all the elements in nums2. If there are still elements left in nums1, we don't need to do anything because THEY ARE ALREADY IN THEIR CORRECT ORDER.
    # def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    #     i = m - 1
    #     j = n - 1
    #     k = m + n - 1
    #
    #     while j >= 0:
    #         if i >= 0 and nums1[i] > nums2[j]:
    #             nums1[k] = nums1[i]
    #             i -= 1
    #         else:
    #             nums1[k] = nums2[j]
    #             j -= 1
    #         k -= 1

    # 100. Same Tree | Diff: Easy | Tags: Tree, Binary Tree, DFS | Date: 04/09/2023
    # The intuition behind the solution is to recursively check if two binary trees are identical. If both trees are empty (null), they are considered identical. If only one tree is empty or the values of the current nodes are different,
    # the trees are not identical. Otherwise, we recursively check if the left and right subtrees of both trees are identical.
    # def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    #     if p is None and q is None:
    #         return True
    #
    #     if p is None or q is None:
    #         return False
    #
    #     if p.val == q.val:
    #         return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    #
    #     return False

    # 101. Symmetric Tree
    # To check if a binary tree is symmetric, we need to compare its left subtree and right subtree. To do this, we can traverse the tree recursively and compare the left and right subtrees at each level. If they are symmetric,
    # we continue the traversal. Otherwise, we can immediately return false.
    # https://leetcode.com/problems/symmetric-tree/solutions/3290112/easy-solutions-in-java-python-and-c-look-at-once/
    # def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    #     if root is None:
    #         return True
    #     return self.isMirror(root.left, root.right)
    #
    #
    # def isMirror(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    #     # both are empty -> mirror
    #     if root1 is None and root2 is None:
    #         return True
    #
    #     # if only one of them is None and one has a values -> not mirror
    #     if root1 is None or root2 is None:
    #         return False
    #
    #     # if they have the same value -> mirror
    #     # recursively call isMirror for the subtrees return True if they have the same value and false if they don't
    #     return root1.val == root2.val and self.isMirror(root1.left, root2.right) and self.isMirror(root1.right, root2.left)

    # 767. Reorganize String | Diff: Medium | Tags: String, Hash Table, Heap
    # one method of solving this is to put the most frequent character in the result string
    # for doing this a maxheap that contains the characters with their frequency can be used
    # https://www.youtube.com/watch?v=2g_b1aYTHeg
    # def reorganizeString(self, s: str) -> str:
    #     # make a hashmap that contains every character in the string along with the frequency
    #     char_frequency = {}
    #     for c in s:
    #         char_frequency[c] = char_frequency.get(c, 0) + 1
    #
    #     # python only has minheap, so to make it a maxheap I inserted -count in the heap
    #     max_heap = [[-count, char] for char, count in char_frequency.items()]
    #     heapq.heapify(max_heap)
    #
    #     prev = None
    #     result = ""
    #     while max_heap:
    #         count, char = heapq.heappop(max_heap)
    #         result += char
    #         # because I use a minheap I have to use +1 instead of -1
    #         count += 1
    #
    #         if prev:
    #             heapq.heappush(max_heap, prev)
    #             prev = None
    #
    #         if count != 0:
    #             prev = [count, char]
    #
    #     if prev and not max_heap:
    #         return ""
    #
    #     return result

    # 136. Single Number
    # one method is to use a hashmap to find the frequency of the items in the array and return the one with freq=1
    # another method is to use XOR: because there are at most 2 duplicates when using xor so a^a = 0 -> in the end only the non-duplicate item will remain
    # def singleNumber1(self, nums: List[int]) -> int:
    #     num_frequency = {}
    #     for num in nums:
    #         num_frequency[num] = num_frequency.get(num, 0) + 1
    #
    #     for item in num_frequency.items():
    #         if item[1] == 1:
    #             return item[0]
    #
    # def singleNumber2(self, nums: List[int]) -> int:
    #     rez = 0
    #     for item in nums:
    #         rez ^= item
    #     return rez

    # 168. Excel Sheet Column Title
    # def convertToTitle(self, columnNumber: int) -> str:
    #     base = 26
    #     digits = []
    #     output = ""
    #
    #     while columnNumber:
    #         # divmod used because using % and // results in bugs
    #         columnNumber, current_digit = divmod(columnNumber - 1, base)
    #         digits.append(current_digit)
    #
    #     for digit in digits:
    #         string_val = chr(65 + digit)
    #         output += string_val
    #
    #     return output[::-1]

    # 169. Majority Element
    # count frequency of elements and return the one with max frequency
    # or sort the array and return the middle element
    # def majorityElement(self, nums: List[int]) -> int:
    #     num_frequency = {}
    #     for num in nums:
    #         num_frequency[num] = num_frequency.get(num, 0) + 1
    #     for item in num_frequency.items():
    #         if item[1] > len(nums) // 2:
    #             return item[0]
    #
    # def majorityElement2(self, nums: List[int]) -> int:
    #     nums.sort()
    #     return nums[len(nums) // 2]

    # 190. Reverse Bits
    # def reverseBits(self, n: int) -> int:
    #     mod = 0
    #     for i in range(32):
    #         mod = mod << 1
    #         mod |= n & 1
    #         n = n >> 1
    #     return mod

    # 191. Number of 1 Bits
    # def hammingWeight(self, n: int) -> int:
    #     count = 0
    #     while n:
    #         if n & 1 == 1:
    #             count += 1
    #         n = n >> 1
    #     return count

    # 68. Text Justification
    # def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
    #     i = 0
    #     char_sum = 0
    #     line = []
    #     final_result = []
    #
    #     while i < len(words):
    #         if len(words[i]) + char_sum <= maxWidth:
    #             line.append(words[i])
    #             char_sum += len(words[i]) + 1
    #             i += 1
    #         else:
    #             spaces_to_add = maxWidth - char_sum + len(line)
    #             added = 0
    #             j = 0
    #             temp_result = ""
    #
    #             # add spaces iteratively, add from left to right until the end then come back at the start
    #             # if spaces to add doesn't divide well with the number of spaces
    #             while added != spaces_to_add:
    #                 if j >= len(line) - 1:
    #                     j = 0
    #
    #                 line[j] += " "
    #                 added += 1
    #                 j += 1
    #
    #             for word in line:
    #                 temp_result += word
    #             final_result.append("".join(temp_result))
    #
    #             char_sum = 0
    #             line = []
    #
    #     for word in range(len(line) - 1):
    #         line[word] += " "
    #
    #     line[-1] += " " * (maxWidth - char_sum + 1)
    #     final_result.append("".join(line))
    #
    #     return final_result

    # 231. Power of Two
    # def isPowerOfTwo(self, n: int) -> bool:
    #     if n == 0:
    #         return False
    #
    #     count = 0
    #     while n:
    #         count += n & 1
    #         if count > 1:
    #             return False
    #         n = n >> 1
    #     return True

    # 1000 & 111 = 0
    # if I use & between a number n, and n-1 then the result n & (n-1) should be 0 if n is a power of 2
    # def isPowerOfTwo(self, n: int) -> bool:
    #     return n and not (n & n - 1)

    # 234. Palindrome Linked List
    # def isPalindrome(self, head: Optional[ListNode]) -> bool:
    #     aux = head
    #     stack = []
    #     while aux:
    #         stack.append(aux.val)
    #         aux = aux.next
    #
    #     aux = head
    #     while aux:
    #         if aux.val != stack.pop():
    #             return False
    #         aux = aux.next
    #     return True

    # 226. Invert Binary Tree
    # In this question we have to Invert the binary tree.
    # So we use Post Order Traversal in which first we go in Left subtree and then in Right subtree then we return back to Parent node.
    # When we come back to the parent node we swap it's Left subtree and Right subtree.
    # def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    #     if not root:
    #         return None
    #
    #     self.invertTree(root.left)  # Call the left subtree
    #     self.invertTree(root.right)  # Call the right subtree
    #     # Swap the nodes
    #     root.left, root.right = root.right, root.left
    #     return root  # Return the root

    # 242. Valid Anagram
    # check if frequency of chars in first string is the same as the frequency in the second string
    # def isAnagram(self, s: str, t: str) -> bool:
    #     if len(s) != len(t):
    #         return False
    #
    #     s_freq = Counter(s)
    #     t_freq = Counter(t)
    #
    #     for item in s_freq.items():
    #         if item[1] != t_freq[item[0]]:
    #             return False
    #
    #     return True

    # 257. Binary Tree Paths
    # To find all the root-to-leaf paths, we can use a depth-first search (DFS) algorithm. We'll implement a recursive helper function solve() that takes two parameters: the current node and the current path string. The
    # solve() function will traverse the tree in a depth-first manner and append the root-to-leaf paths to the ans list.
    # def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
    #     answer = []
    #
    #     def dfs(root: TreeNode, string):
    #         string += str(root.val)
    #         if not root.left and not root.right:
    #             answer.append(string)
    #             return
    #
    #         if root.left:
    #             dfs(root.left, string + "->")
    #         if root.right:
    #             dfs(root.right, string + "->")
    #
    #     dfs(root, "")
    #     return answer

    # 338. Counting Bits
    # def countBits(self, n: int) -> List[int]:
    #     return [bin(i).count('1') for i in range(n+1)]

    # 326. Power of Three
    # def isPowerOfThree(self, n: int) -> bool:
    #     if n == 0:
    #         return False
    #     while n % 3 == 0:
    #         n //= 3
    #     return n == 1

    # 342. Power of Four
    # In this implementation, we first check if the number is greater than zero and is a power of two. If it is, then we check if the number is of the form 4^x by using a bitwise 'and' operation with a mask of 0x55555555, which is a 32-bit number
    # that has every other bit set to 1. This check ensures that the only bits that are set in the number are in positions that are multiples of 2, which is the condition for the number to be of the form 4^x. If the number passes both checks,
    # then it is a power of four.
    # OR check bit 1 and 2, if they are 1 then it's not a power of 2, shift by 2 ( / 4) and if the final number is 1 then it's a power of 2
    # def isPowerOfFour(self, n: int) -> bool:
    #     while n:
    #         if n == 1:
    #             return True
    #         if (n & 1 or n & 2):
    #             return False
    #         n = n >> 2

    # 345. Reverse Vowels of a String
    # def reverseVowels(self, s: str) -> str:
    #     vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    #     i = 0
    #     j = len(s) - 1
    #     s = list(s)
    #     while i < j:
    #         if s[i] not in vowels:
    #             i += 1
    #         if s[j] not in vowels:
    #             j -= 1
    #         if s[i] in vowels and s[j] in vowels:
    #             s[i], s[j] = s[j], s[i]
    #             i += 1
    #             j -= 1
    #     s = "".join(s)
    #     return s

    # 349. Intersection of Two Arrays
    # def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    #     x = set(nums1)
    #     y = set(nums2)
    #     return list(x.intersection(y))

    # 350. Intersection of Two Arrays II
    # def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    #     x = Counter(nums1)
    #     y = Counter(nums2)
    #
    #     arr = []
    #     for num1 in x:
    #         if num1 in y:
    #             count = min(x[num1], y[num1])
    #             arr.extend([num1] * count)
    #
    #     return arr

    # 367. Valid Perfect Square
    # similar to 69
    # def isPerfectSquare(self, num: int) -> bool:
    #     if num == 0 or num == 1:
    #         return True
    #
    #     left = 0
    #     right = num
    #
    #     while left <= right:
    #         middle = left + (right - left) // 2
    #         if middle * middle == num:
    #             return True
    #         elif middle > num // middle:
    #             right = middle - 1
    #         else:
    #             left = middle + 1
    #
    #     return False

    # 383. Ransom Note
    # def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    #     ran_freq = Counter(ransomNote)
    #     mag_freq = Counter(magazine)
    #
    #     for item in ran_freq.items():
    #         if item[0] in mag_freq:
    #             if item[1] > mag_freq[item[0]]:
    #                 return False
    #         else:
    #             return False
    #
    #     return True

    # 387. First Unique Character in a String
    # def firstUniqChar(self, s: str) -> int:
    #     chars = Counter(s)
    #
    #     for char in s:
    #         if chars[char] == 1:
    #             return s.index(char)
    #
    #     return -1

    # 389. Find the Difference
    # def findTheDifference(self, s: str, t: str) -> str:
    #     return list(Counter(t) - Counter(s))[0]

    # 392. Is Subsequence
    # def isSubsequence(self, s: str, t: str) -> bool:
    #     for char in s:
    #         index = t.find(char)
    #         if index == -1:
    #             return False
    #         # continue search from the next char in t string
    #         else:
    #             t = t[index + 1:]
    #
    #     return True

    # def isSubsequence(self, s: str, t: str) -> bool:
    #     i = 0
    #     j = 0
    #
    #     while i < len(s) and j < len(t):
    #         if s[i] == t[j]:
    #             i += 1
    #         j += 1
    #
    #     return i == len(s)

    # 404. Sum of Left Leaves
    # def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
    #     def helper(node, is_left):
    #         if not node:
    #             return 0
    #
    #         if not node.left and not node.right and is_left:
    #             return node.val
    #
    #         left_sum = helper(node.left, True)
    #         right_sum = helper(node.right, False)
    #
    #         return left_sum + right_sum
    #
    #     return helper(root, False)

    # 409. Longest Palindrome
    # def longestPalindrome(self, s: str) -> int:
    #     char_freq = Counter(s)
    #     length = 0
    #     contains_odd = False
    #     for item in char_freq.items():
    #         length += item[1] // 2 * 2
    #         if item[1] % 2 and not contains_odd:
    #             length += 1
    #             contains_odd = not contains_odd
    # 
    #     return length

    # 448. Find All Numbers Disappeared in an Array
    # def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
    #     num_set = set(nums)
    #     result = []
    #     for i in range(1, len(nums) + 1):
    #         if i not in num_set:
    #             result.append(i)
    #
    #     return result

    # 412. Fizz Buzz
    # def fizzBuzz(self, n: int) -> List[str]:
    #
    #     result = []
    #     for i in range(1, n + 1):
    #         if i % 3 == 0 and i % 5 == 0:
    #             result.append("FizzBuzz")
    #         elif i % 3 == 0:
    #             result.append("Fizz")
    #         elif i % 5 == 0:
    #             result.append("Buzz")
    #         else:
    #             result.append(str(i))
    #
    #     return result

    # 414. Third Maximum Number
    # def thirdMax(self, nums: List[int]) -> int:
    #     nums = list(set(nums))
    #     nums.sort(reverse=True)
    #
    #     if len(nums) == 1:
    #         return nums[0]
    #     if len(nums) == 2:
    #         return nums[0]
    #     if len(nums) >= 3:
    #         return nums[2]

    # 283. Move Zeroes
    # def moveZeroes(self, nums: List[int]) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     idx = 0
    #     for num in nums:
    #         if num != 0:
    #             nums[idx] = num
    #             idx += 1
    #
    #     while idx < len(nums):
    #         nums[idx] = 0
    #         idx += 1

    # 441. Arranging Coins
    # Math solution
    # def arrangeCoins(self, n: int) -> int:
    #     i = 1
    #     total_sum = 1
    #     while total_sum <= n:
    #         i += 1
    #         total_sum = (i * (i + 1)) // 2
    #     return i - 1

    #     left = 0
    #     right = len(arr) - 1
    #     while left <= right:
    #         mid = (left + right) // 2
    #         if arr[mid] == target:
    #             return mid
    #
    #         if target < arr[mid]:
    #             right = mid - 1
    #         else:
    #             left = mid + 1
    #     return -1

    # !!! binary search
    # https://www.youtube.com/watch?v=5rHz_6s2Buw
    # def arrangeCoins(self, n: int) -> int:
    #     left = 1
    #     right = n
    #     result = 0
    #
    #     while left <= right:
    #         mid = (left + right) // 2
    #         coins = (mid * (mid + 1)) // 2
    #
    #         if coins > n:
    #             right = mid - 1
    #         else:
    #             left = mid + 1
    #             result = mid
    #
    #     return result

    # 461. Hamming Distance
    # def hammingDistance(self, x: int, y: int) -> int:
    #     diff = x ^ y
    #     sum = 0
    #     for i in range(32):
    #         sum += (diff >> i) & 1
    #     return sum

    # def hammingDistance(self, x: int, y: int) -> int:
    #     return str(bin(x ^ y)).count("1")

    # 482. License Key Formatting
    # def licenseKeyFormatting(self, s: str, k: int) -> str:
    #     s = s.replace("-", "").upper()
    #     first_group = len(s) % k
    #     result = s[:first_group]
    #
    #     for i in range(first_group, len(s), k):
    #         if result:
    #             result += "-"
    #         result += s[i:i + k]
    #
    #     return result

    # 485. Max Consecutive Ones
    # def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    #     max_count = -1
    #     current = 0
    #     for i in range(len(nums)):
    #         if nums[i] == 1:
    #             current += 1
    #         else:
    #             max_count = max(current, max_count)
    #             current = 0
    #     return max(current, max_count)

    # 495. Teemo Attacking
    # def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
    #     if not timeSeries or duration == 0:
    #         return 0
    #
    #     poisoned_time = 0
    #     for i in range(0, len(timeSeries) - 1):
    #         # if teemo attacks before the last poison ends then the duration of the poison is the diff between the 2 attacks
    #         if timeSeries[i + 1] - timeSeries[i] < duration:
    #             poisoned_time += timeSeries[i + 1] - timeSeries[i]
    #         else:
    #             poisoned_time += duration
    #
    #     return poisoned_time + duration

    # 501. Find Mode in Binary Search Tree
    # def findMode(self, root: Optional[TreeNode]) -> List[int]:
    #     freq = {}
    #
    #     def helper(root):
    #         if not root:
    #             return
    #
    #         if root.val in freq:
    #             freq[root.val] += 1
    #         else:
    #             freq[root.val] = 1
    #
    #         helper(root.left)
    #         helper(root.right)
    #         return
    #
    #     helper(root)
    #
    #     max_val = max(freq.values())
    #     result = []
    #     for key, val in freq.items():
    #         if val == max_val:
    #             result.append(key)
    #
    #     return result

    # 500. Keyboard Row
    # def findWords(self, words: List[str]) -> List[str]:
    #     first = "qwertyuiop"
    #     second = "asdfghjkl"
    #     third = "zxcvbnm"
    #     result = []
    #
    #     for word in words:
    #         aux = word.lower()
    #         if len(set(first + aux)) == len(first) or len(set(second + aux)) == len(second) or len(set(third + aux)) == len(third):
    #             result.append(word)
    #
    #     return result

    # 205. Isomorphic Strings
    # def isIsomorphic(self, s: str, t: str) -> bool:
    #     first = []
    #     second = []
    #
    #     for val in s:
    #         first.append(s.index(val))
    #
    #     for val in t:
    #         second.append(t.index(val))
    #
    #     if first == second:
    #         return True
    #     return False

    # def isIsomorphic(self, s: str, t: str) -> bool:
    #     zipped_set = set(zip(s, t))
    #     return len(zipped_set) == len(set(s)) == len(set(t))

    # def wordPattern(self, pattern: str, s: str) -> bool:
    #     s = s.split(" ")
    #     pattern = list(pattern)
    #
    #     if len(pattern) != len(s):
    #         return False
    #
    #     pattern_word = {}
    #     word_pattern = {}
    #     for i in range(len(pattern)):
    #         pat = pattern[i]
    #         wor = s[i]
    #
    #         if pat in pattern_word and pattern_word[pat] != wor:
    #             return False
    #
    #         if wor in word_pattern and word_pattern[wor] != pat:
    #             return False
    #
    #         pattern_word[pat] = wor
    #         word_pattern[wor] = pat
    #
    #     return True

    # better version, faster because of dict
    # def wordPattern(self, pattern: str, s: str) -> bool:
    #     words = s.split(" ")
    #     pattern = list(pattern)
    #
    #     if len(pattern) != len(words):
    #         return False
    #
    #     dictionary = {}
    #
    #     for i in range(len(pattern)):
    #         if pattern[i] not in dictionary:
    #             # if pattern isn't in dict and the word is then it means that the word appears for a different pattern -> False
    #             if words[i] not in dictionary.values():
    #                 dictionary[pattern[i]] = words[i]
    #             else:
    #                 return False
    #         else:
    #             if dictionary[pattern[i]] != words[i]:
    #                 return False
    #
    #     return True

    # 509. Fibonacci Number
    # def fib(self, n: int) -> int:
    #     if n == 0:
    #         return 0
    #     if n <= 2:
    #         return 1
    #
    #     fib_values = [0] * (n + 1)
    #     fib_values[0] = 0
    #     fib_values[1] = 1
    #     fib_values[2] = 1
    #
    #     for i in range(3, n + 1):
    #         fib_values[i] = fib_values[i - 1] + fib_values[i - 2]
    #
    #     return fib_values[n]

    # 203. Remove Linked List Elements
    # def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
    #     if not head:
    #         return None
    #     head.next = self.removeElements(head.next, val)
    #     if head.val == val:
    #         return head.next
    #     else:
    #         return head

    # def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
    #     prev, curr = None, head
    #     while curr:
    #         if curr.val == val:  # cases 1-3
    #             if prev:  # cases 1-2
    #                 prev.next = curr.next
    #             else:  # case 3
    #                 head = curr.next
    #             curr = curr.next  # for all cases
    #         else:  # case 4
    #             prev, curr = curr, curr.next
    #     return head

    # 171. Excel Sheet Column Number
    # just a base conversion from the leftmost letter, digit = ASCII(letter)-64, add the digit to result and multiply it by 26 each iteration
    # def titleToNumber(self, columnTitle: str) -> int:
    #     result = 0
    #     for letter in columnTitle:
    #         result = result * 26 + (ord(letter) - 64)
    #
    #     return result
    #
    # def titleToNumber(self, columnTitle: str) -> int:
    #     result = 0
    #     power = 0
    #     for letter in reversed(columnTitle):
    #         result += (ord(letter) - 64) * (26 ** power)
    #         power += 1
    #
    #     return result

    # 434. Number of Segments in a String
    # def countSegments(self, s: str) -> int:
    #     count = 0
    #     for i in range(len(s)):
    #         if s[i] != ' ' and (i == 0 or s[i-1] == ' '):
    #             count += 1
    #     return count

    # 455. Assign Cookies
    # To assign cookies to children optimally we should give for each child the closest higher cookie. By using this greedy approach overall sum of wasted cookies will be minimum among all. To use this greedy solution in
    # effective way we can sort both arrays and use two pointers. We should move pointer of children only if there is enough cookies to make that child content. In each step we will try to make content child at position pointerG by searching the
    # closes higher cookie value.
    # def findContentChildren(self, g: List[int], s: List[int]) -> int:
    #     g.sort()
    #     s.sort()
    #
    #     i, j = 0, 0
    #
    #     while i < len(g) and j < len(s):
    #         if g[i] <= s[j]:
    #             i += 1
    #         j += 1
    #     return i

    # 504. Base 7
    # def convertToBase7(self, num: int) -> str:
    #     if num == 0:
    #         return '0'
    #
    #     ans = ""
    #     aux = abs(num)
    #
    #     while aux:
    #         aux, remainder = divmod(aux, 7)
    #         ans += str(remainder)
    #
    #     if num < 0:
    #         ans = ans + "-"
    #
    #     return ans[::-1]

    # 520. Detect Capital
    # counter number of uppercase letters, if count == 0 OR count == len(word) OR count == 1 and first letter is uppercase then it's good
    # def detectCapitalUse(self, word: str) -> bool:
    #     count = 0
    #     for s in word:
    #         if s.isupper():
    #             count += 1
    #
    #     if count == 0 or count == len(word) or (count == 1 and word[0].isupper()):
    #         return True
    #     return False

    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    # 530. Minimum Absolute Difference in BST
    # inorder search to find all the values and put them in an array, sort the array and find the minimum difference
    # def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
    #     vals = []
    #
    #     def inorder(root):
    #         if not root:
    #             return
    #         vals.append(root.val)
    #         inorder(root.left)
    #         inorder(root.right)
    #
    #         return
    #
    #     inorder(root)
    #
    #     vals.sort()  # Step 1: Sort the array
    #     min_diff = float('inf')  # Initialize minimum difference as positive infinity
    #
    #     for i in range(1, len(vals)):
    #         diff = abs(vals[i] - vals[i - 1])  # Step 2: Calculate absolute difference
    #         min_diff = min(min_diff, diff)  # Step 3: Update minimum difference
    #
    #     return min_diff

    # 543. Diameter of Binary Tree
    # def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    #     diameter = 0
    #
    #     def height(node) -> int:
    #         nonlocal diameter
    #         if not node:
    #             return 0
    #
    #         left = height(node.left)
    #         right = height(node.right)
    #         diameter = max(diameter, left + right)
    #         return 1 + max(left, right)
    #
    #     height(root)
    #     return diameter

    # DOESN'T WORK BECAUSE ONE SIDE Of THE TREE MIGHT HAVE A BIGGER DIAMETER THAN THE SUM OF BOTH
    #     def maxHeightOfBinaryTree(self, root: TreeNode) -> int:
    #         if not root:
    #             return 0
    #
    #         left = self.maxHeightOfBinaryTree(root.left)
    #         right = self.maxHeightOfBinaryTree(root.right)
    #         return 1 + max(left, right)
    #
    #     def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    #         left_height = self.maxHeightOfBinaryTree(root.left)
    #         right_height = self.maxHeightOfBinaryTree(root.right)
    #         return left_height + right_height

    # 551. Student Attendance Record I
    # def checkRecord(self, s: str) -> bool:
    #     for i in range(len(s) - 2):
    #         if s[i] == "L" and s[i + 1] == "L" and s[i + 2] == "L":
    #             return False
    #
    #     freq = Counter(s)
    #     if freq["A"] < 2:
    #         return True

    # 557. Reverse Words in a String III
    # 2 pointers, left points to the first letter of the word, right points to the first space found after the word
    # use splicing to add reversed string to the answer. At the end add the remaking word to the answer
    # def reverseWords(self, s: str) -> str:
    #     left = 0
    #     right = 0
    #     result = ""
    #
    #     while right < len(s):
    #         if s[right] != " ":
    #             right += 1
    #         else:
    #             result += s[left:right][::-1] + " "
    #             right += 1
    #             left = right
    #
    #     result += s[left:right][::-1]
    #     return result
    #
    # def reverseWords(self, s: str) -> str:
    #     split_list = s.split(" ")
    #     split_list = [i[::-1] for i in split_list]
    #     return " ".join(split_list)

    # 563. Binary Tree Tilt
    # tilt is absolute difference between values of left tree and right tree
    # use a postorder traversal func to find vals
    # def findTilt(self, root: Optional[TreeNode]) -> int:
    #     self.ans = 0
    #
    #     def helper(node):
    #         if not node:
    #             return 0
    #
    #         left = helper(node.left)
    #         right = helper(node.right)
    #         self.ans += abs(right - left)
    #
    #         return left + right + node.val
    #
    #     helper(root)
    #     return self.ans

    # 124. Binary Tree Maximum Path Sum | Diff: Hard | Tags: Tree, Binary Tree, DFS, Dynamic Programming | Date: 27/08/2023
    # recursive dfs, calculate the max between the current max and (leftValue + rightValue + nodeValue) for left subtree and right subtree
    # similar to 543, maxSum is the maximum between a value and the sum of (leftSubtree, rightSubtree, and node value)
    # def maxPathSum(self, root: Optional[TreeNode]) -> int:
    #     def maxPath(root):
    #         nonlocal maxSum
    #         if not root:
    #             return 0
    #
    #         left = maxPath(root.left)
    #         right = maxPath(root.right)
    #         maxSum = max(maxSum, left + right + root.val)
    #         return max(left + root.val, right + root.val, 0)
    #
    #     maxSum = -math.inf
    #     maxPath(root)
    #     return maxSum

    # 1. Two Sum | Diff: Easy | Tags: Array, Hash Table / Alternative: Two Pointers | Date: 01/08/2023
    # use a hashmap to store the index and the values in the array
    # loop over all keys in the hashmap and calculate the difference diff = target - key and use the diff as a key to search the hashmap for the other element
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     hash_map = {}
    #     # diff, index
    #     for i, val in enumerate(nums):
    #         diff = target - val
    #         if diff in hash_map:
    #             return [i, hash_map[diff]]
    #         else:
    #             hash_map[val] = i

    # 2. Add Two Numbers
    # Use % and /. Add the 2 values of the current nodes and add the carry, sum = val1 + val2 + carry. The value of the node will be sum%10 and the carry value will be sum / 10. 
    # At the end, if carry is > 0 then add another node that contains the carry value
    # def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    #     carry = 0
    #     root = result = ListNode(-1)
    #
    #     while l1 or l2 or carry:
    #         val1 = 0
    #         val2 = 0
    #
    #         if l1:
    #             val1 = l1.val
    #             l1 = l1.next
    #
    #         if l2:
    #             val2 = l2.val
    #             l2 = l2.next
    #
    #         current = val1+val2+carry
    #         result.next = ListNode(current%10)
    #         result = result.next
    #
    #         carry = current//10
    #
    #     if carry:
    #         result.next = ListNode(carry)
    #
    #     return root.next

    # 3. Longest Substring Without Repeating Characters
    # We take two pointers, l and r, both starting at 0. At every iteration, we update the longest string with non-repeating characters found = r-l+1 and just keep a note of which character we see at which index
    # Now, lets face it - our string does have repeating characters. We look at index 3, we're realizing we've seen a before. So we now, we can't just calculate the value of longest like we were doing before. We need to make sure our left pointer,
    # or l, is at least past the index where we last saw a thus - we move l to seen[right]+1. We also update our map with last seen of a to 3
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     char_map = {}
    #     left = 0
    #     max_length = 0
    #
    #     for right in range(len(s)):
    #
    #         # if char wasn't seen before, then store it in map with its index, update max length
    #         # or if the index of the character is less than the left pointer
    #         if s[right] not in char_map or char_map[s[right]] < left:
    #             char_map[s[right]] = right
    #             max_length = max(max_length, right - left + 1)
    #
    #         # if char was seen before, then update left pointer to be the next position AFTER the character that was a duplicate
    #         # and update the new position of the left pointer
    #         else:
    #             left = char_map[s[right]] + 1
    #             char_map[s[right]] = right
    #
    #     return max_length

    # 6. Zigzag Conversion
    # create a list of string lists; use a pointer to show where to put the current character; use a boolean variable to know when to increase or decrease the index of the list
    # def convert(self, s: str, numRows: int) -> str:
    #     if numRows == 1:
    #         return s
    #
    #     i = 1
    #     increase_index = True
    #     result_arrays = [""] * numRows
    #
    #     for character in s:
    #         result_arrays[i - 1] += character
    #
    #         if i == numRows:
    #             increase_index = False
    #         elif i == 1:
    #             increase_index = True
    #
    #         if increase_index:
    #             i += 1
    #         else:
    #             i -= 1
    #
    #     return "".join(result_arrays)

    # 7. Reverse Integer
    # def reverse(self, x: int) -> int:
    #     result = 0
    #     aux = abs(x)
    #     while aux:
    #         aux, remainder = divmod(aux, 10)
    #         result = result * 10 + remainder
    #         if result > 2147483647:
    #             return 0
    #
    #     return result if x > 0 else -result

    # 11. Container With Most Water
    # use 2 pointers left and right, left starts at 0, right starts at the last elements to ensure the width is the greatest possible
    # each iteration change the pointer of the line with the lower height (increment left or decrement right)
    # next check if the new area is bigger, if yes then replace max area with new one
    # def maxArea(self, height: List[int]) -> int:
    #     left = 0
    #     right = len(height) - 1
    #
    #     max_area = -1
    #
    #     while left < right:
    #         left_height = height[left]
    #         right_height = height[right]
    #
    #         area = (right - left) * min(left_height, right_height)
    #         if area > max_area:
    #             area, max_area = max_area, area
    #
    #         if left_height < right_height:
    #             left += 1
    #         else:
    #             right -= 1
    #
    #     return max_area

    # 12. Integer to Roman
    # take each roman numeral in descending order, divide num with current value, if count > 0 then we can use the symbol
    # update result as res+= (symbol*count) and update num as num%value to only check for the remainder in the future
    # def intToRoman(self, num: int) -> str:
    #     romans = {
    #         "I": 1,
    #         "IV": 4,
    #         "V": 5,
    #         "IX": 9,
    #         "X": 10,
    #         "XL": 40,
    #         "L": 50,
    #         "XC": 90,
    #         "C": 100,
    #         "CD": 400,
    #         "D": 500,
    #         "CM": 900,
    #         "M": 1000
    #     }
    #
    #     result = ""
    #     for key, value in reversed(romans.items()):
    #         count = num // value
    #         if count > 0:
    #             result += (key * count)
    #             num = num % value
    #     return result

    # 13. Roman to Integer
    # if a  numeral is in front of another one, and it is smaller IV -> then the smaller one is subtracted from the result IV = -1 + 5
    # if it is bigger then it is added XV = 10 + 5
    # def romanToInt(self, s: str) -> int:
    #     romans = {
    #         "I": 1,
    #         "V": 5,
    #         "X": 10,
    #         "L": 50,
    #         "C": 100,
    #         "D": 500,
    #         "M": 1000
    #     }
    #
    #     sum = 0
    #     for i in range(len(s)):
    #         if i < len(s) - 1 and romans[s[i]] < romans[s[i + 1]]:
    #             sum -= romans[s[i]]
    #         else:
    #             sum += romans[s[i]]
    #
    #     return sum

    # 14. Longest Common Prefix ???

    # 15. 3Sum
    # sort the array so that negative numbers are on the left side and positive on the right
    # loop the array and choose a fixed element
    # use 2 pointers to find the complements so that the sum is 0
    # left points to the next element after fixed one and right points to the last element of the array
    # calculate sum and move left and right like binary search
    # if sum > 0 then positive number is too big, right = right - 1
    # if sum < 0 then negative number is too big, left = left + 1
    # if sum == 0 then the triplet is found, append it to the result list
    # use 2 while loops
    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     nums.sort()
    #     results = []
    #
    #     for i in range(len(nums)):
    #         # as long as i is not on the last element of the duplicate group continue; this helps with left pointing
    #         if i > 0 and nums[i - 1] == nums[i]:
    #             continue
    #
    #         left = i + 1
    #         right = len(nums) - 1
    #
    #         while left < right:
    #             s = nums[i] + nums[left] + nums[right]
    #             if s == 0:
    #                 results.append([nums[i], nums[left], nums[right]])
    #                 left += 1
    #                 right -= 1
    #
    #                 # Skip all duplicates on left side
    #                 while left < right and nums[left - 1] == nums[left]:
    #                     left += 1
    #
    #                 # Skip all duplicates on right side
    #                 while left < right and nums[right + 1] == nums[right]:
    #                     right -= 1
    #
    #             if s < 0:
    #                 left += 1
    #
    #             if s > 0:
    #                 right -= 1
    #
    #     return results

    # 17. Letter Combinations of a Phone Number
    # use backtracking to create the resulting string
    # backtracking function takes index and current string as parameters
    # def letterCombinations(self, digits: str) -> List[str]:
    #     if not digits:
    #         return []
    #
    #     phone = {"2": "abc",
    #              "3": "def",
    #              "4": "ghi",
    #              "5": "jkl",
    #              "6": "mno",
    #              "7": "pqrs",
    #              "8": "tuv",
    #              "9": "wxyz"}
    #
    #     result = []
    #
    #     # function takes digit index and current string as parameters
    #     def backtrack(idx, currentString):
    #         # if the length of the current string is the same as the length of the digits given, then its valid and can be added to results
    #         if len(currentString) == len(digits):
    #             result.append(currentString)
    #             return
    #         # loop all characters in the current digit using the given index
    #         for char in phone[digits[idx]]:
    #             # call backtrack with the next index and add current char to the current string
    #             backtrack(idx + 1, currentString + char)
    #
    #     backtrack(0, "")
    #     return result

    # 19. Remove Nth Node From End of List
    # https://www.youtube.com/watch?v=XtYEEvrhemI
    # 2 pointers with a distance of n between them, when right reaches the end then left is on the node to be removed
    # first move right until it reaches the n-th node FROM THE START, now left and right are at distance of n between them
    # then move right and left until right is at None at the end of the list -> now left is on the previous node to the one to be deleted
    # def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    #     left = head
    #     right = head
    #
    #     for i in range(n):
    #         right = right.next
    #
    #     if not right:
    #         return head.next
    #
    #     while right.next:
    #         right = right.next
    #         left = left.next
    #
    #     left.next = left.next.next
    #
    #     return head

    # 22. Generate Parentheses
    # https://www.youtube.com/watch?v=s9fokUqJ76A -> just the cases
    # with n pairs there will be 3 open ( and 3 closed ) parenthesis
    # an open parenthesis can be added to the string only if open < n
    # a closing parenthesis can be added to the string only if the number of open ones is greater than the one of closed parenthesis
    # def generateParenthesis(self, n: int) -> List[str]:
    #     result = []
    #
    #     def backtrack(current_string, open, closed):
    #         if open == n and closed == n:
    #             result.append(current_string)
    #             return
    #
    #         if open < n:
    #             backtrack(current_string + "(", open + 1, closed)
    #
    #         if closed < open:
    #             backtrack(current_string + ")", open, closed + 1)
    #
    #     backtrack("", 0, 0)
    #     return result

    # 24. Swap Nodes in Pairs
    # def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     dummy = ListNode(0, head)
    #     current = dummy
    #
    #     while current.next and current.next.next:
    #         first = current.next
    #         second = current.next.next
    #         after = second.next
    #
    #         current.next = second
    #         second.next = first
    #         first.next = after
    #
    #         current = current.next.next
    #
    #     return dummy.next

    # 31. Next Permutation
    # https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order
    # def nextPermutation(self, nums: List[int]) -> None:
    #     k = -1
    #     i = len(nums) - 2
    #     while i >= 0:
    #         if nums[i] < nums[i + 1]:
    #             k = i
    #             break
    #         i -= 1
    #
    #     if k < 0:
    #         nums.reverse()
    #     else:
    #         l = 0
    #         i = len(nums) - 1
    #         while i >= 0 and i > k:
    #             if nums[i] > nums[k]:
    #                 l = i
    #                 break
    #             i -= 1
    #
    #         nums[k], nums[l] = nums[l], nums[k]
    #         nums[::] = nums[:k + 1] + nums[k + 1:][::-1]
    #
    #     print(nums)

    # 33. Search in Rotated Sorted Array
    # use binary search and keep in mind the rotated part, it looks like an x = y graph where a portion is swapped
    # if nums[left] <= nums[mid] -> LEFT SIDE IS SORTED;
    # target > nums[mid] continue RIGHT; target < nums[left]: then search in RIGHT because it contains rotated elements, maybe target
    # if nums[left] > nums[mid]: RIGHT SIDE IS SORTED
    # target < nums[mid] CONTINUE LEFT; target > nums[right]: then search in LEFT because it contains rotated elements, maybe target
    # https://www.youtube.com/watch?v=U8XENwh8Oy8
    # def search(self, nums: List[int], target: int) -> int:
    #     left = 0
    #     right = len(nums) - 1
    #
    #     while left <= right:
    #         mid = (left + right) // 2
    #         print(f"{nums[left]} {nums[mid]} {nums[right]}")
    #
    #         if nums[mid] == target:
    #             return mid
    #
    #         # it means that the left part is less than the left part has values [ nums[left], nums[mid] ] in increasing order so ITS SORTED
    #         if nums[left] < nums[mid]:
    #             # if target > nums[mid] then target it's also greater than any value in left subarray because nums[mid] is the greatest value in left subarray
    #             # if target < nums[left] then target it's also lower than any value in left subarray because nums[left] is lowest value in left subarray
    #             if target > nums[mid] or target < nums[left]:
    #                 left = mid + 1
    #             # if target < nums [mid] -> search in left subarray because values are in range [ nums[left], nums[mid] ]
    #             else:
    #                 right = mid - 1
    #
    #         # it means that the right part has values in interval [ nums[mid], nums[right] ] in increasing order so ITS SORTED
    #         else:
    #             # if target < nums[mid] then search in
    #             if target < nums[mid] or target > nums[right]:
    #                 right = mid - 1
    #             else:
    #                 left = mid + 1

    # 34. Find First and Last Position of Element in Sorted Array
    # https://www.youtube.com/watch?v=4sQL7R5ySUU -> bottom else is bad, change with target == num[mid] first
    # needs the start and end index of the target element positions
    # modify binary search: when target is found remember mid in an index
    # if searching for start index then continue binary search with right = mid - 1 until while loop is existed
    # if searching for end index then continue binary search with left = mid + 1 until while loop is existed
    # def searchRange(self, nums: List[int], target: int) -> List[int]:
    #     def bin_search_mod(searchLeft):
    #         left = 0
    #         right = len(nums) - 1
    #         idx = -1
    #
    #         while left <= right:
    #             mid = (left + right) // 2
    #
    #             if target == nums[mid]:
    #                 idx = mid
    #                 if searchLeft:
    #                     right = mid - 1
    #                 else:
    #                     left = mid + 1
    #
    #             if target < nums[mid]:
    #                 right = mid - 1
    #
    #             if target > nums[mid]:
    #                 left = mid + 1
    #         return idx
    #
    #     left = bin_search_mod(True)
    #     right = bin_search_mod(False)
    #
    #     return [left, right]

    # 36. Valid Sudoku
    # check if number is unique in line, unique in column and unique in its square
    # def isValidSudoku(self, board: List[List[str]]) -> bool:
    #     results = []
    #
    #     for i in range(9):
    #         for j in range(9):
    #             element = board[i][j]
    #             if board[i][j] != ".":
    #                 # The first tuple contains the row index (i) and the element itself.
    #                 # The second tuple contains the element and the column index
    #                 # The third tuple contains the floor division of the row index by 3 (i // 3), the floor division of the column index by 3 (j // 3), and the element itself.
    #                 # This tuple represents the 3x3 sub-grid that the current cell belongs to.
    #                 # order matters, ELEMENT,J has to be like this otherwise it fails
    #                 results += [(i, element), (element, j), (i // 3, j // 3, element)]
    #
    #     # 4)After processing all the cells, the method checks if the length of "res" is equal to the length of the set of "res".
    #     return len(results) == len(set(results))

    # 37. Sudoku Solver
    # https://www.youtube.com/watch?v=_Z9Mz2V-Mig -> better returns
    # def solveSudoku(self, board: List[List[str]]) -> None:
    #     """
    #     Do not return anything, modify board in-place instead.
    #     """
    #     return self.solve(board)
    #
    # def isValidPlacement(self, row, col, k, board):  # function to check whether it is safe to insert a no. in board or not
    #     for i in range(9):
    #         if board[row][i] == k:  # for checking element in same row
    #             return False
    #         if board[i][col] == k:  # for checking element in same column
    #             return False
    #         if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == k:  # for checking element in same box
    #             return False
    #     return True
    #
    # def solve(self, board):
    #     for i in range(len(board)):
    #         for j in range(len(board)):
    #             if board[i][j] == ".":
    #                 for num in range(1, 10):
    #                     char = str(num)
    #                     if self.isValidPlacement(i, j, char, board):
    #                         board[i][j] = char
    #
    #                         if self.solve(board):
    #                             return True
    #                         else:
    #                             board[i][j] = "."
    #                 return False
    #     return True

    # 39. Combination Sum
    # BETTER
    # def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    #     result = []
    #
    #     def backtrack(start, target, path):
    #         if target == 0:
    #             result.append(path[:])
    #             return
    #
    #         # loop over all candidates from the start index
    #         for i in range(start, len(candidates)):
    #             # if candidate is greater than target then skip
    #             if target >= candidates[i]:
    #                 # add the candidate to path,
    #                 # call backtrack with the same index ( same value can be used multiple times ), target becomes target - candidate value, and with updated path
    #                 path.append(candidates[i])
    #                 backtrack(i, target - candidates[i], path)
    #
    #                 # After the recursive call, we remove the last element from the path to backtrack and explore other possibilities.
    #                 path.pop()
    #
    #     backtrack(0, target, [])
    #     return result

    # def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    #     result = []
    #
    #     def backtracking(current_index: int, current_path: [], total: int):
    #         if total == target:
    #             # need to use copy, otherwise the values are modified
    #             result.append(current_path.copy())
    #             return
    #
    #         if total > target or current_index >= len(candidates):
    #             return
    #
    #         current_path.append(candidates[current_index])
    #         backtracking(current_index, current_path, total + candidates[current_index])
    #
    #         current_path.pop()
    #         backtracking(current_index + 1, current_path, total)
    #
    #         return
    #
    #     backtracking(0, [], 0)
    #     return result

    # 40. Combination Sum II
    # The isValid function is designed to consolidate the conditions that determine whether a candidate can be considered for inclusion in the combination. This function encapsulates two checks:
    # - Duplicate Candidate Check: This check ensures that a candidate is not considered a duplicate if it's the same as the previous candidate. It compares the value of the current candidate with the value of the previous candidate. If they are
    # equal (candidates[index] == candidates[index - 1]), it means we have a duplicate. However, if the current index is the starting index (index == start), we don't need to check for duplicates, as it's the first candidate.
    #
    # - Target Validity Check: This check verifies that using the current candidate won't make the remaining target negative. It compares the current candidate's value with the remaining target. If the candidate's value is greater than the remaining
    # target (target >= candidates[index]), it means that adding this candidate would result in overshooting the target, and therefore, it's not a valid choice.
    #
    # By combining these two checks within the isValid function, we create a single condition that encapsulates the necessary checks for candidate validity. The isValid function returns True if the candidate is valid for inclusion and returns
    # False otherwise.
    #
    # The advantage of using the isValid function is that it abstracts away the complexity of these checks from the main backtrack function, making the code more readable and easier to understand. It also promotes modularity by separating the
    # validity check logic into its own function.
    # def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    #     result = []
    #
    #     # def isValid(index, start, target):
    #     #     return index == start or candidates[index] != candidates[index - 1] and target >= candidates[index]
    #
    #     def backtrack(start, target, path):
    #         if target == 0:
    #             result.append(path[:])
    #             return
    #
    #         # loop over all candidates from the start index
    #         for i in range(start, len(candidates)):
    #             # if candidate is greater than target then skip
    #             if i == start or candidates[i] != candidates[i - 1] and target >= candidates[i]:
    #                 # add the candidate to path,
    #                 # call backtrack with the same index ( same value can be used multiple times ), target becomes target - candidate value, and with updated path
    #                 path.append(candidates[i])
    #                 backtrack(i + 1, target - candidates[i], path)
    #
    #                 # After the recursive call, we remove the last element from the path to backtrack and explore other possibilities.
    #                 path.pop()
    #
    #     backtrack(0, target, [])
    #     return result

    # USES CONTINUE INSTEAD OF ISVALID
    # def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    #
    #     # def isValid(index, start, target):
    #     #     return index == start or candidates[index] != candidates[index - 1] and target >= candidates[index]
    #
    #     def backtrack(start, target, path):
    #         if target == 0:
    #             result.append(path[:])
    #             return
    #
    #         # loop over all candidates from the start index
    #         for i in range(start, len(candidates)):
    #             # if candidate is greater than target then skip
    #             if i > start and candidates[i] == candidates[i - 1]:
    #                 continue
    #             if target < candidates[i]:
    #                 continue
    #
    #             # add the candidate to path,
    #             # call backtrack with the same index ( same value can be used multiple times ), target becomes target - candidate value, and with updated path
    #             path.append(candidates[i])
    #             backtrack(i + 1, target - candidates[i], path)
    #
    #             # After the recursive call, we remove the last element from the path to backtrack and explore other possibilities.
    #             path.pop()
    #
    #     result = []
    #     candidates.sort()
    #     backtrack(0, target, [])
    #     return result

    # 46. Permutations
    # def permute(self, nums: List[int]) -> List[List[int]]:
    #     def backtrack(current, used):
    #         if len(current) == len(nums):
    #             result.append(current[:])
    #             return
    #
    #         for i in range(len(nums)):
    #             if not used[i]:
    #                 used[i] = True
    #                 backtrack(current + [nums[i]], used)
    #                 used[i] = False
    #
    #     result = []
    #     backtrack([], [False] * len(nums))
    #     return result

    # 47. Permutations II
    # def permute(self, nums: List[int]) -> List[List[int]]:
    #     def backtrack(current, counter):
    #         if len(current) == len(nums):
    #             result.append(current[:])
    #             return
    #
    #         for val in counter:
    #             if counter[val] > 0:
    #                 counter[val] -= 1
    #                 backtrack(current + [val], counter)
    #                 counter[val] += 1
    #
    #     result = []
    #     backtrack([], Counter(nums))
    #     return result

    # 48. Rotate Image
    #  * clockwise rotate
    #  * first reverse up to down, then swap the symmetry
    #  * 1 2 3     7 8 9     7 4 1
    #  * 4 5 6  => 4 5 6  => 8 5 2
    #  * 7 8 9     1 2 3     9 6 3
    #
    #  * anticlockwise rotate
    #  * first reverse left to right, then swap the symmetry
    #  * 1 2 3     3 2 1     3 6 9
    #  * 4 5 6  => 6 5 4  => 2 5 8
    #  * 7 8 9     9 8 7     1 4 7
    # */
    # def rotate(self, matrix: List[List[int]]) -> None:
    #     """
    #     Do not return anything, modify matrix in-place instead.
    #     """
    #
    #     matrix.reverse()
    #
    #     for i in range(len(matrix)):
    #         for j in range(i + 1, len(matrix[i])):
    #             matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # 49. Group Anagrams
    # - Anagrams are words that have the same characters but in a different order
    # loop over each word in list and sort them lexicographically,
    # use a dict using the sorted word as key and add the original word to the dict
    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #     anagram_table = {}
    #
    #     for word in strs:
    #         sorted_word = "".join(sorted(word))
    #
    #         if sorted_word not in anagram_table:
    #             anagram_table[sorted_word] = []
    #
    #         anagram_table[sorted_word].append(word)
    #
    #     return list(anagram_table.values())

    # 51. N-Queens
    # simple verify is slow, for more speed use sets
    # def solveNQueens(self, n: int) -> List[List[str]]:
    #     def isValid(board, row, column):
    #         for i in range(n):
    #             # don't have to check row, only 1 queen per row can be placed
    #             # if board[row][i] == "Q":
    #             #     return False
    #             if board[i][column] == "Q":
    #                 return False
    #
    #         # Check upper left diagonal
    #         for i, j in zip(range(row - 1, -1, -1), range(column - 1, -1, -1)):
    #             if board[i][j] == 'Q':
    #                 return False
    #
    #         # Check upper right diagonal
    #         for i, j in zip(range(row - 1, -1, -1), range(column + 1, n)):
    #             if board[i][j] == 'Q':
    #                 return False
    #
    #         return True
    #
    #     def backtrack(board, row):
    #         # GOAL
    #         if row == n:
    #             result.append(["".join(row) for row in board])
    #             return
    #
    #         # CONDITIONS
    #         for column in range(n):
    #             # VALID
    #             if isValid(board, row, column):
    #                 board[row][column] = "Q"
    #                 backtrack(board, row + 1)
    #                 board[row][column] = "."
    #
    #     board = [["."] * n for i in range(n)]
    #     # [['.' for _ in range(n)] for _ in range(n)]
    #     result = []
    #     backtrack(board, 0)
    #
    #     return result

    # for easier column checking, use sets for columns
    # negative  has (row - column) constant for elements in the diagonal
    # positive diagonal increases column and decreases row
    # https://www.youtube.com/watch?v=Ph95IHmRp5M&t=1s
    # def solveNQueens(self, n: int) -> List[List[str]]:
    #     def isValid(row, column):
    #         if column in col or (row + column) in positiveDiagonal or (row - column) in negativeDiagonal:
    #             return False
    #         return True
    #
    #     def backtrack(board, row):
    #         # GOAL
    #         if row == n:
    #             result.append(["".join(row) for row in board])
    #             return
    #
    #         # CONDITIONS
    #         for column in range(n):
    #             # VALID
    #             if isValid(row, column):
    #                 board[row][column] = "Q"
    #                 col.add(column)
    #                 positiveDiagonal.add(row + column)
    #                 negativeDiagonal.add(row - column)
    #
    #                 backtrack(board, row + 1)
    #
    #                 col.remove(column)
    #                 positiveDiagonal.remove(row + column)
    #                 negativeDiagonal.remove(row - column)
    #
    #                 board[row][column] = "."
    #
    #     col = set()
    #     positiveDiagonal = set()
    #     negativeDiagonal = set()
    #     board = [["."] * n for i in range(n)]
    #     # [['.' for _ in range(n)] for _ in range(n)]
    #     result = []
    #     backtrack(board, 0)
    #
    #     return result

    # 69 - sqrt using binary search
    # def mySqrt(self, x: int) -> int:
    #     if x == 0 or x == 1:
    #         return x
    #
    #     left = 0
    #     right = x
    #
    #     while left <= right:
    #         middle = left + (right - left) // 2
    #         if middle == x // middle:
    #             return middle
    #         elif middle > x // middle:
    #             right = middle - 1
    #         else:
    #             left = middle + 1
    #
    #     return right

    # 121. Best Time to Buy and Sell Stock
    # https://www.youtube.com/watch?v=ioFPBdChabY
    # def maxProfit(self, prices: List[int]) -> int:
    #     profit = 0
    #     buy = prices[0]
    #     for sale in prices[1:]:
    #         if sale > buy:
    #             profit = max(profit, sale - buy)
    #         else:
    #             buy = sale
    #     return profit

    # def maxProfit(self, prices: List[int]) -> int:
    #     profit = 0
    #     buy_idx = 0
    #
    #     for sell_idx in range(1, len(prices)):
    #         if prices[sell_idx] > prices[buy_idx]:
    #             profit = max(profit, prices[sell_idx] - prices[buy_idx])
    #         else:
    #             buy_idx = sell_idx
    #
    #     return profit

    # 27. Remove Element - 01/09/2023
    # use 2 pointers i and j, i points to the first element that is not val and j points to the first element of val
    # def removeElement(self, nums: List[int], val: int) -> int:
    #     i = 0
    #     j = 0
    #     while i < len(nums):
    #         if nums[i] == val:
    #             i += 1
    #         else:
    #             nums[j] = nums[i]
    #             i += 1
    #             j += 1
    #
    #     return j

    # 26. Remove Duplicates from Sorted Array - 01/09/2023
    # like 25, use 2 pointers, i find first non-duplicate and j points to duplicate
    # def removeDuplicates(self, nums: List[int]) -> int:
    #     i = 0
    #     j = 0
    #     while i < len(nums):
    #         if nums[i] == nums[i - 1] and i > 0:
    #             i += 1
    #         else:
    #             nums[j] = nums[i]
    #             i += 1
    #             j += 1
    #
    #     return j

    # 1929. Concatenation of Array - 01/09/2023
    # 2 pointers: i points to the current element in result array, j points to the element in nums; when j == len(nums) reset j to 0
    # def getConcatenation(self, nums: List[int]) -> List[int]:
    #     result = [0] * len(nums) * 2
    #     j = 0
    #     for i in range(len(result)):
    #         result[i] = nums[j]
    #         j += 1
    #         if j == len(nums):
    #             j = 0
    #
    #     return result

    # 21. Merge Two Sorted Lists - 01/09/2023
    # create an empty node, loop over both lists and compare their current nodes, if list1Node.val < list2Node.val then newList.next = list1
    # def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> []:
    #     head = ListNode()
    #     current = head
    #
    #     while list1 and list2:
    #         if list1.val < list2.val:
    #             current.next = list1
    #             list1 = list1.next
    #         else:
    #             current.next = list2
    #             list2 = list2.next
    #
    #         current = current.next
    #
    #     current.next = list1 or list2
    #
    #     return head.next

    # 206. Reverse Linked List - 01/09/2023
    # use a stack; first loop all list element and add them to the stack; second loop replace current node val value popped from the stack
    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     stack = []
    #     dummy = head
    #     dummy2 = head
    #
    #     while dummy:
    #         stack.append(dummy.val)
    #         dummy = dummy.next
    #
    #     while dummy2:
    #         popped_val = stack.pop()
    #         dummy2.val = popped_val
    #         dummy2 = dummy2.next
    #
    #     return head

    # 682. Baseball Game - 01/09/2023
    # use a stack to record the values, C-> pop, D->push, int->push
    # def calPoints(self, operations: List[str]) -> int:
    #     op_stack = []
    #     for operation in operations:
    #         if operation == "C":
    #             op_stack.pop()
    #         elif operation == "D":
    #             op_stack.append(str(int(op_stack[-1]) * 2))
    #         elif operation == "+":
    #             op_stack.append(str(int(op_stack[-1]) + int(op_stack[-2])))
    #         else:
    #             op_stack.append(int(operation))
    #
    #     result = 0
    #     while op_stack:
    #         result += int(op_stack.pop())
    #
    #     return result

    # 155. Min Stack - 01/09/2023
    # https://www.youtube.com/watch?v=qkLl7nAwDPo
    # use 2 stacks, 1 stores the values normally, other stores the current min val; for each push call, push on the min stack the value if it is lower than the current min value in min stack;
    # duplicates in the min stack don't matter, when pop is called it removes from both stacks
    # class MinStack:
    #     def __init__(self):
    #         self.vals = []
    #         self.min_stack = []
    #
    #     def push(self, val: int) -> None:
    #         self.vals.append(val)
    #         val = min(val, self.min_stack[-1] if self.min_stack else val)
    #         self.min_stack.append(val)
    #
    #     def pop(self) -> None:
    #         self.vals.pop()
    #         self.min_stack.pop()
    #
    #     def top(self) -> int:
    #         return self.vals[-1]
    #
    #     def getMin(self) -> int:
    #         return self.min_stack[-1]

    # 509. Fibonacci Number - 01/09/2023
    # fibonacci normal recursion
    # def fib(self, n: int) -> int:
    #     if n == 0 or n == 1:
    #         return n
    #
    #     return self.fib(n - 1) + self.fib(n - 2)

    # fibonacci DP, top to bottom
    # def fib(self, n: int) -> int:
    #     fib_results = [0] * (n + 1)
    #
    #     fib_results[0] = 0
    #     fib_results[1] = 1
    #
    #     for i in range(2, n + 1):
    #         fib_results[i] = fib_results[i - 1] + fib_results[i - 2]
    #
    #     return fib_results[n]

    # fibonacci iterative
    # def fib(self, N: int) -> int:
    #     a, b = 0, 1
    #     for i in range(N):
    #         a, b = b, a + b
    #     return a

    # 74. Search a 2D Matrix - 01/09/2023
    # compare target with element on the final element of the row (row, final column) with target; if it is higher than target then call binary search for row values
    # def binary_search_iterative(self, arr, target):
    #     left = 0
    #     right = len(arr) - 1
    #     while left <= right:
    #         mid = (left + right) // 2
    #         if arr[mid] == target:
    #             return True
    #
    #         if target < arr[mid]:
    #             right = mid - 1
    #         else:
    #             left = mid + 1
    #     return False
    #
    # def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    #     max_col = len(matrix[0]) - 1
    #     for i in range(len(matrix)):
    #         if matrix[i][max_col] >= target:
    #             return self.binary_search_iterative(matrix[i], target)
    #
    #     return False

    # 240. Search a 2D Matrix II - 01/09/2023
    # https://leetcode.com/problems/search-a-2d-matrix-ii/solutions/2324351/python-explained/
    #
    # As the rows are sorted -> matrix[i][j] < matrix[i][j+1]
    # As the columns are sorted -> matrix[i][j] >matrix[i-1][j]
    #
    # Hence it can be said that :
    # any element right to matrix[i][j] will be greater than it.
    # any element to the top of matrix[i][j] will be less than it.
    # So we start searching from BOTTOM_LEFT:
    #
    # if element found -> return TRUE
    # if matrix[i][j] > target -> move UP.
    # if matrix[i][j] < target -> move RIGHT.
    # def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    #     N, M = len(matrix), len(matrix[0])
    #     r, c = N - 1, 0
    #
    #     while r >= 0 and c < M:
    #         value = matrix[r][c]
    #         if value == target:
    #             return True
    #         # go UP
    #         if value > target:
    #             r -= 1
    #         # go RIGHT
    #         if value < target:
    #             c += 1
    #
    #     return False

    # 700. Search in a Binary Search Tree - 01/09/2023
    # def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    #     if not root:
    #         return
    #
    #     if root.val == val:
    #         return root
    #
    #     if val < root.val:
    #         return self.searchBST(root.left, val)
    #     else:
    #         return self.searchBST(root.right, val)

    # 701. Insert into a Binary Search Tree - 01/09/2023
    # https://leetcode.com/problems/insert-into-a-binary-search-tree/solutions/1683942/well-detailed-explaination-java-c-python-easy-for-mind-to-accept-it/
    # If the root is empty, the new tree node can be returned as the root node.
    # Otherwise, compare root. val is related to the size of the target value:
    #
    # If root.val is greater than the target value, indicating that the target value should be inserted into the left subtree of the root, and the problem becomes root. Insert the target value in the left and recursively call the current function;
    # If root.val is less than the target value, indicating that the target value should be inserted into the right subtree of the root, and the problem becomes root. Insert the target value in right and recursively call the current function.
    # def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    #     if not root:
    #         return TreeNode(val)
    #
    #     if val < root.val:
    #         root.left = self.insertIntoBST(root.left, val)
    #     else:
    #         root.right = self.insertIntoBST(root.right, val)
    #
    #     return root

    # 450. Delete Node in a BST - 01/09/2023
    # https://www.youtube.com/watch?v=LFzAoJJt92M
    # def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
    #
    #     if not root:
    #         return root
    #
    #     if key < root.val:
    #         root.left = self.deleteNode(root.left, key)
    #     elif key > root.val:
    #         root.right = self.deleteNode(root.right, key)
    #     else:
    #         if not root.left:
    #             return root.right
    #         elif not root.right:
    #             return root.left
    #
    #         current = root.right
    #         while current.left:
    #             current = current.left
    #
    #         root.val = current.val
    #         root.right = self.deleteNode(root.right, root.val)
    #
    #     return root

    # 94. Binary Tree Inorder Traversal Left,Root,Right - 01/09/2023
    # def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #     result = []
    #
    #     def inorder(root):
    #         if not root:
    #             return None
    #
    #         inorder(root.left)
    #         result.append(root.val)
    #         inorder(root.right)
    #
    #     inorder(root)
    #     return result

    # 230. Kth Smallest Element in a BST - 01/09/2023
    # inorder search, get element k-1 from result list
    # def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    #     def inorder(root):
    #         if not root:
    #             return
    #
    #         inorder(root.left)
    #         result.append(root.val)
    #         inorder(root.right)
    #
    #     result = []
    #     inorder(root)
    #     return result[k - 1]

    # 78. Subsets - Backtracking - 01/09/2023
    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #
    #     def backtrack(index, path):
    #         result.append(path[:])
    #         if len(result) == 2 ** len(nums):
    #             return
    #
    #         for i in range(index, len(nums)):
    #             path = path + [nums[i]]
    #             backtrack(i + 1, path)
    #             path = path[:-1]
    #
    #     result = []
    #     backtrack(0, [])
    #     return result

    # 90. Subsets II - Backtracking - 01/09/2023
    # def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
    #
    #     def backtrack(index, path):
    #         result.append(path[:])
    #         if len(result) == 2 ** len(nums):
    #             return
    #
    #         for i in range(index, len(nums)):
    #             if i > index and nums[i] == nums[i - 1]:
    #                 continue
    #             path = path + [nums[i]]
    #             backtrack(i + 1, path)
    #             path = path[:-1]
    #
    #     result = []
    #     nums.sort()
    #     backtrack(0, [])
    #     return result

    # 77. Combinations - Backtracking
    # def combine(self, n: int, k: int) -> List[List[int]]:
    #     def backtrack(index, path: List):
    #         if len(path) == k:
    #             result.append(path[:])
    #             return
    #
    #         for i in range(index, n + 1):
    #             path.append(i)
    #             backtrack(i + 1, path)
    #             path.pop()
    #
    #     result = []
    #     backtrack(1, [])
    #     return result

    # 150. Evaluate Reverse Polish Notation - Stack - 01/09/2023
    # def evalRPN(self, tokens: List[str]) -> int:
    #     values = []
    #
    #     for token in tokens:
    #         if token == "+":
    #             a = values.pop()
    #             b = values.pop()
    #             values.append(a + b)
    #         elif token == "-":
    #             a = values.pop()
    #             b = values.pop()
    #             values.append(b - a)
    #         elif token == "*":
    #             a = values.pop()
    #             b = values.pop()
    #             values.append(a * b)
    #         elif token == "/":
    #             a = values.pop()
    #             b = values.pop()
    #             values.append(int(float(b) / a))  # evaluates to a 0 with the 6/-132 scenario (as required).
    #         else:
    #             number = int(token)
    #             values.append(number)
    #
    #     return values.pop()

    # 347. Top K Frequent Elements | Diff: Medium | Tags: Hashtable, Heap, Bucket Sort, Quickselect | Date: 02/09/2023
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     frequency = Counter(nums)
    #
    #     frequency = dict(sorted(frequency.items(), key=lambda x: x[1], reverse=True))
    #
    #     result = list(frequency.keys())[:k]
    #     return result

    # use a heap, counter to find all the frequencies, push key and value to heap (in python only minheap -> push -val);
    # while k, pop from heap
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     frequency = Counter(nums)
    #     heap = []
    #     for key, val in frequency.items():
    #         heappush(heap, (-val, key))
    #
    #     result = []
    #     while k:
    #         k -= 1
    #         result.append(heappop(heap)[1])
    #
    #     return result

    # 238. Product of Array Except Self | Diff: Medium | Tags: Array, Prefix Sum | Date: 02/09/2023
    # Compute 2 array prefix and postfix that contain the products of the array before the element and after the element
    # the result of product without current is product of elements before * product of elements after
    # https://www.youtube.com/watch?v=bNvIQI2wAjk
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     prefix = [1] * (len(nums))
    #     postfix = [1] * (len(nums))
    #
    #     prefix[0] = nums[0]
    #     for i in range(1, len(nums)):
    #         prefix[i] = prefix[i - 1] * nums[i]
    #
    #     postfix[len(nums) - 1] = nums[len(nums) - 1]
    #     for i in range(len(nums) - 2, -1, -1):
    #         postfix[i] = postfix[i + 1] * nums[i]
    #
    #     result = [0] * len(nums)
    #     for i in range(len(nums)):
    #         before = prefix[i - 1] if i - 1 >= 0 else 1
    #         after = postfix[i + 1] if i + 1 < len(nums) else 1
    #         result[i] = before * after if before != 0 or after != 0 else 0
    #
    #     return result

    # 128. Longest Consecutive Sequence | Diff: Medium | Tags: Array, Hash Table, Union Find | Date: 02/09/2023
    # https://www.youtube.com/watch?v=P6RZZMu_maU
    # use a set, if number is the start of sequence then it doesn't have a left neighbour, set[val-1] is not found
    # to find the longest sequence increment a value for how many numbers are linked to the initial value
    # def longestConsecutive(self, nums: List[int]) -> int:
    #     num_set = set(nums)
    #     longest = 0
    #
    #     for val in nums:
    #         # check if val is the start of a new sequence, it doesn't have a left neighbour
    #         if (val - 1) not in num_set:
    #             length = 0
    #             while val + length in num_set:
    #                 length += 1
    #             longest = max(longest, length)
    #
    #     return longest

    # 167. Two Sum II - Input Array Is Sorted | Diff: Medium | Tags: Array, Hash Map | Alternative: Two Pointers, Binary Search | Date: 02/09/2023
    # ??? same as two sum ??? but order is reversed
    # def twoSum(self, numbers: List[int], target: int) -> List[int]:
    #     dif_dict = {}
    #
    #     for i, val in enumerate(numbers):
    #         diff = target - val
    #         if diff in dif_dict:
    #             return [dif_dict[diff] + 1, i + 1]
    #         else:
    #             dif_dict[val] = i

    # Alternative with 2 Pointers - Similar with 3Sum move pointers like a binary search
    # def twoSum(self, numbers: List[int], target: int) -> List[int]:
    #     left = 0
    #     right = len(numbers) - 1
    #
    #     while left <= right:
    #         total = numbers[left] + numbers[right]
    #         if total == target:
    #             return [left + 1, right + 1]
    #
    #         if total < target:
    #             left += 1
    #
    #         if total > target:
    #             right -= 1
    #
    #     return -1

    # 42. Trapping Rain Water | Diff: Hard | Tags: Array, Two Pointers, Dynamic Programming | Date: 02/09/2023
    # https://www.youtube.com/watch?v=ZI2z5pq0TqA&t=4s
    # https://leetcode.com/problems/trapping-rain-water/solutions/1374608/c-java-python-maxleft-maxright-so-far-with-picture-o-1-space-clean-concise/
    # Same idea with solution 1, but now we don't need to build maxLeft and maxRight arrays, we will calculate maxLeft and maxRight as we go.
    # We start with maxLeft = height[0], maxRight = height[n-1], using 2 pointers left point to the next bar on the left side, right point to the next bar on the right side.
    # How to decide to move left or move right?
    # If maxLeft < maxRight, it means the water level is based on the left side (the left bar is smaller) then move left side:
    # If height[left] > maxLeft then there is no trap water, we update maxLeft by maxLeft = height[left].
    # Else if height[left] < maxLeft then it can trap an amount of water, which is maxLeft - height[left].
    # Move left by left += 1
    # Else if maxLeft > maxRight, it means the water level is based on the right side (the right bar is smaller) then move right side:
    # If height[right] > maxRight then there is no trap water, we update maxRight by maxRight = height[right].
    # Else if height[right] < maxRight then it can trap an amount of water, which is maxRight - height[right].
    # Move right by right -= 1.
    # def trap(self, height: List[int]) -> int:
    #     left = 0
    #     right = len(height) - 1
    #     leftMax = height[left]
    #     rightMax = height[right]
    #
    #     result = 0
    #     # TRICK -> similar with minimax; for 2 pointers, if maxLeft is 0 and maxRight currently is 1, then maxRight is not needed because I need to calculate min(0,1) so no matter what right value is, maxLeft is still smaller
    #
    #     while left < right:
    #         if leftMax < rightMax:
    #             left += 1
    #             leftMax = max(leftMax, height[left])
    #             result += leftMax - height[left]
    #         else:
    #             right += 1
    #             rightMax = max(rightMax, height[right])
    #             result += rightMax - height[right]
    #
    #     return result

    # https://leetcode.com/problems/trapping-rain-water/solutions/1374608/c-java-python-maxleft-maxright-so-far-with-picture-o-1-space-clean-concise/
    # calculates min and max values of heights before
    # A ith bar can trap the water if and only if there exists a higher bar to the left and a higher bar to the right of ith bar.
    # To calculate how much amount of water the ith bar can trap, we need to look at the maximum height of the left bar and the maximum height of the right bar, then
    # The water level can be formed at ith bar is: waterLevel = min(maxLeft[i], maxRight[i])
    # If waterLevel >= height[i] then ith bar can trap waterLevel - height[i] amount of water.
    # To achieve in O(1) when looking at the maximum height of the bar on the left side and on the right side of ith bar, we pre-compute it:
    # Let maxLeft[i] is the maximum height of the bar on the left side of ith bar.
    # Let maxRight[i] is the maximum height of the bar on the right side of ith bar.
    # def trap(self, height: List[int]) -> int:
    #     length = len(height)
    #     maxLeft = [0] * length
    #     maxRight = [0] * length
    #
    #     for i in range(1, length):
    #         maxLeft[i] = max(height[i - 1], maxLeft[i - 1])
    #
    #     for i in range(length - 2, -1, -1):
    #         maxRight[i] = max(height[i + 1], maxRight[i + 1])
    #
    #     print(maxLeft)
    #     print(maxRight)
    #
    #     result = 0
    #     for i in range(length):
    #         water = min(maxRight[i], maxLeft[i])
    #         if water > height[i]:
    #             result += water - height[i]
    #
    #     return result

    # 739. Daily Temperatures | Dif: Medium | Tags: Array, Stack, Monotonic Stack | Date: 02/09/2023
    # Link: https://leetcode.com/problems/daily-temperatures/description/
    # def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    #     result = [0] * len(temperatures)
    #     temp_stack = []  # index, temp
    #
    #     for index, temp in enumerate(temperatures):
    #         while temp_stack and temp > temp_stack[-1][1]:
    #             stack_index, stack_temp = temp_stack.pop()
    #             result[stack_index] = index - stack_index
    #         temp_stack.append([index, temp])
    #
    #     return result

    # def search(self, nums: List[int], target: int) -> int:
    #     left = 0
    #     right = len(nums) - 1
    #
    #     while left <= right:
    #         mid = (left + right) // 2
    #         print(f"{nums[left]} {nums[mid]} {nums[right]}")
    #
    #         if nums[mid] == target:
    #             return mid
    #
    #         # it means that the left part is less than the left part has values [ nums[left], nums[mid] ] in increasing order so ITS SORTED
    #         if nums[left] < nums[mid]:
    #             # if target > nums[mid] then target it's also greater than any value in left subarray because nums[mid] is the greatest value in left subarray
    #             # if target < nums[left] then target it's also lower than any value in left subarray because nums[left] is lowest value in left subarray
    #             if target > nums[mid] or target < nums[left]:
    #                 left = mid + 1
    #             # if target < nums [mid] -> search in left subarray because values are in range [ nums[left], nums[mid] ]
    #             else:
    #                 right = mid - 1
    #
    #         # it means that the right part has values in interval [ nums[mid], nums[right] ] in increasing order so ITS SORTED
    #         else:
    #             # if target < nums[mid] then search in
    #             if target < nums[mid] or target > nums[right]:
    #                 right = mid - 1
    #             else:
    #                 left = mid + 1

    # 153. Find Minimum in Rotated Sorted Array | Diff: Medium | Tags: Array, Binary Search | Date: 02/09/2023
    # def findMin(self, nums: List[int]) -> int:
    #     left = 0
    #     right = len(nums) - 1
    #
    #     while left < right:
    #         mid = (left + right) // 2
    #         print(f" {nums[left]} {nums[mid]} {nums[right]}")
    #
    #         if left == right:
    #             return nums[left]
    #
    #         # nums(mid) > nums(right) means that the minimal values has to be in right side, because everything left of right has to be lower
    #         if nums[mid] > nums[right]:
    #             left = mid + 1
    #         else:
    #             right = mid

    # def findMin(self, nums):
    #     # set left and right bounds
    #     left, right = 0, len(nums) - 1
    #
    #     # left and right both converge to the minimum index;
    #     # DO NOT use left <= right because that would loop forever
    #     while left < right:
    #         # find the middle value between the left and right bounds (their average);
    #         # can equivalently do: mid = left + (right - left) // 2,
    #         # if we are concerned left + right would cause overflow (which would occur
    #         # if we are searching a massive array using a language like Java or C that has
    #         # fixed size integer types)
    #         mid = (left + right) // 2
    #
    #         # the main idea for our checks is to converge the left and right bounds on the start
    #         # of the pivot, and never disqualify the index for a possible minimum value.
    #
    #         # in normal binary search, we have a target to match exactly,
    #         # and would have a specific branch for if nums[mid] == target.
    #         # we do not have a specific target here, so we just have simple if/else.
    #
    #         if nums[mid] > nums[right]:
    #             # we KNOW the pivot must be to the right of the middle:
    #             # if nums[mid] > nums[right], we KNOW that the pivot/minimum value must have occurred somewhere to the right of mid, which is why the values wrapped around and became smaller.
    #
    #             # example:  [3,4,5,6,7,8,9,1,2]
    #             # in the first iteration, when we start with mid index = 4, right index = 9.
    #             # if nums[mid] > nums[right], we know that at some point to the right of mid, the pivot must have occurred, which is why the values wrapped around  so that nums[right] is less then nums[mid]
    #
    #             # we know that the number at mid is greater than at least one number to the right, so we can use mid + 1 and never consider mid again; we know there is at least one value smaller than it on the right
    #             left = mid + 1
    #
    #         else:
    #             # here, nums[mid] <= nums[right]:
    #             # we KNOW the pivot must be at mid or to the left of mid: if nums[mid] <= nums[right], we KNOW that the pivot was not encountered to the right of middle, because that means the values would wrap around
    #             # and become smaller (which is caught in the above if statement). this leaves the possible pivot point to be at index <= mid.
    #
    #             # example: [8,9,1,2,3,4,5,6,7]
    #             # in the first iteration, when we start with mid index = 4, right index = 9.
    #             # if nums[mid] <= nums[right], we know the numbers continued increasing to the right of mid, so they never reached the pivot and wrapped around. therefore, we know the pivot must be at index <= mid.
    #
    #             # we know that nums[mid] <= nums[right].
    #             # therefore, we know it is possible for the mid index to store a smaller value than at least one other index in the list (at right), so we do not discard it by doing right = mid - 1. it still might have the minimum value.
    #             right = mid
    #
    #     # at this point, left and right converge to a single index (for minimum value) since
    #     # our if/else forces the bounds of left/right to shrink each iteration:
    #
    #     # when left bound increases, it does not disqualify a value
    #     # that could be smaller than something else (we know nums[mid] > nums[right],
    #     # so nums[right] wins and we ignore mid and everything to the left of mid).
    #
    #     # when right bound decreases, it also does not disqualify a
    #     # value that could be smaller than something else (we know nums[mid] <= nums[right],
    #     # so nums[mid] wins and we keep it for now).
    #
    #     # so we shrink the left/right bounds to one value,
    #     # without ever disqualifying a possible minimum
    #     return nums[left]

    # 104. Maximum Depth of Binary Tree | Diff: Easy | Tags: Tree, Binary Tree, DFS, BFS | Date: 04/09/2023
    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     # if previous node doesn't have a left child or a right child, return 0
    #     if not root:
    #         return 0
    #
    #     # next calculate max height between left subtree and right subtree
    #     return max(self.maxDepth(root.left) + 1, self.maxDepth(root.right) + 1)

    # 110. Balanced Binary Tree | Diff: Easy | Tags: Tree, Binary Tree, DFS | Date: 04/09/2023
    # Balanced = difference of heights between left subtree and right subtree is at most 1
    # To find if a tree is balanced use something like maxDepth and check if |leftDepth - rightDepth| > 1
    # def isBalanced(self, root: TreeNode) -> bool:
    #     if not root:
    #         return True
    #
    #     self.answer = True
    #
    #     def dfs(root):
    #         l, r = 0, 0
    #
    #         if root.left:
    #             l += dfs(root.left)
    #         if root.right:
    #             r += dfs(root.right)
    #         if abs(r - l) > 1:
    #             self.answer = False
    #
    #         # print(root.val, r, l)
    #         return max(r, l) + 1
    #
    #     dfs(root)
    #     return self.answer

    # 572. Subtree of Another Tree | Diff: Easy | Tags: Tree, Binary Tree, DFS | Date: 04/09/2023
    # To check if one tree is a subtree of another tree then you can do this by checking recursively if the child of the tree is the same tree with the subtree
    # use the function isSameTree to check if 2 trees are the same
    # use the function isSubtree to check if left subtree of root is the same tree with the subtree or if the right subtree of root is the same with the subtree
    # def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    #     if not subRoot:
    #         return True
    #     if not root:
    #         return False
    #
    #     if self.isSameTree(root, subRoot):
    #         return True
    #
    #     return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    #
    # def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    #     if p is None and q is None:
    #         return True
    #
    #     if p is None or q is None:
    #         return False
    #
    #     if p.val == q.val:
    #         return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    #
    #     return False

    # 141. Linked List Cycle | Diff: Easy | Tags: Linked List, Hash Table, Two Pointers | Date: 05/09/2023
    # put the value of the current node in a dictionary / list; for each node check if value was already seen
    # def hasCycle(self, head: Optional[ListNode]) -> bool:
    #     seen = {}
    #     while head:
    #         if head in seen:
    #             return True
    #         else:
    #             seen[head] = True
    #         head = head.next
    #     return False

    # 79. Word Search | Diff: Medium | Tags: Array, Matrix, Backtracking, DFS | Date: 05/09/2023
    # from current direction look up down left right for backtrack

    # works, but it's SLOW
    # def exist(self, board: List[List[str]], word: str) -> bool:
    #     def backtrack(found_word, row, col, word_index):
    #         if len(found_word) == len(word):
    #             return True
    #
    #         for i in range(row - 1, row + 2):
    #             if 0 <= i < len(board) and board[i][col] == word[word_index]:
    #                 found_word = found_word + board[i][col]
    #                 board[i][col] = "#"
    #
    #                 if backtrack(found_word, i, col, word_index + 1):
    #                     return True
    #
    #                 board[i][col] = found_word[-1]
    #                 found_word = found_word[:-1]
    #
    #         for j in range(col - 1, col + 2):
    #             if 0 <= j < len(board[0]) and board[row][j] == word[word_index]:
    #                 found_word = found_word + board[row][j]
    #                 board[row][j] = "#"
    #
    #                 if backtrack(found_word, row, j, word_index + 1):
    #                     return True
    #
    #                 board[row][j] = found_word[-1]
    #                 found_word = found_word[:-1]
    #
    #     for row in range(len(board)):
    #         for col in range(len(board[0])):
    #             if backtrack("", row, col, 0):
    #                 return True
    #     return False

    # TRY THIS
    # for i in range(row-1,row+2):
    #     for j in range(col-1,col-2):
    #         if 0 <= j < len(board[0]) and board[row][j] == word[word_index]:
    #             found_word = found_word + board[row][j]
    #               BACKTRACK

    # def exist(self, board: List[List[str]], word: str) -> bool:
    #     def backtrack(row, col, word_index):
    #         if word_index == len(word):
    #             return True
    #
    #         if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] != word[word_index]:
    #             return False
    #
    #         tmp = board[row][col]
    #         board[row][col] = "#"  # Mark as visited
    #
    #         if (backtrack(row + 1, col, word_index + 1) or
    #                 backtrack(row - 1, col, word_index + 1) or
    #                 backtrack(row, col + 1, word_index + 1) or
    #                 backtrack(row, col - 1, word_index + 1)):
    #             return True
    #
    #         board[row][col] = tmp  # Restore the original cell
    #         return False
    #
    #     for row in range(len(board)):
    #         for col in range(len(board[0])):
    #             if backtrack(row, col, 0):
    #                 return True
    #
    #     return False

    # 235. Lowest Common Ancestor of a Binary Search Tree | Diff: Medium | Tags: Tree, Binary Tree, DFS | Date: 05/09/2023
    # lowest common ancestor is the node before the split of p and q, the node where the search for p and q diverges
    # def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    #     while True:
    #         if root.val > p.val and root.val > q.val:
    #             root = root.left
    #         elif root.val < p.val and root.val < q.val:
    #             root = root.right
    #         else:
    #             return root

    # 102. Binary Tree Level Order Traversal | Diff: Medium | Tags: Tree, Binary Tree, BFS | Date: 05/09/2023
    # use bfs to find nodes on the same level, append them to result list when all nodes on current level have been seen
    # def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    #     if not root:
    #         return []
    #
    #     result = []
    #     q = collections.deque()
    #     q.append(root)
    #
    #     while q:
    #         level = []
    #
    #         for i in range(len(q)):
    #             node = q.popleft()
    #             if node:
    #                 level.append(node.val)
    #                 q.append(node.left)
    #                 q.append(node.right)
    #
    #         if level:
    #             result.append(level)
    #
    #     return result

    # 111. Minimum Depth of Binary Tree | Diff: Easy | Tags: Tree, Binary Tree, BFS | Date: 05/09/2023
    # QUEUE BFS IMPLEMENTATION
    # def minDepth(self, root: Optional[TreeNode]) -> int:
    #     if not root:
    #         return 0
    #
    #     queue = collections.deque([])
    #     queue.append(root)
    #     depth = 1
    #     while queue:
    #         for i in range(len(queue)):
    #             node = queue.popleft()
    #             if not node:
    #                 continue
    #             if not node.left and not node.right:
    #                 return depth
    #             queue.append(node.left)
    #             queue.append(node.right)
    #         depth += 1

    # 1046. Last Stone Weight | Diff: Easy | Tags: Array, Heap | Date: 05/09/2023
    # use a heap to find the rock with the highest weight
    # def lastStoneWeight(self, stones: List[int]) -> int:
    #     for index, weight in enumerate(stones):
    #         stones[index] = -weight
    #
    #     heapify(stones)
    #
    #     while stones:
    #         stone1 = -heappop(stones)
    #
    #         if not stones:
    #             return stone1
    #
    #         stone2 = -heappop(stones)
    #
    #         # push -(stone1 - stone2) => push stone2 - stone 1
    #         heappush(stones, stone2 - stone1)
    #
    #     return 0

    # def missingNumber(self, nums: List[int]) -> int:
    #     missing = 0
    #     for num in nums:
    #         missing = missing ^ num
    #
    #     return missing

    # 199. Binary Tree Right Side View | Diff: Medium | Tags: Tree, Binary Tree, BFS | Date: 06/05/2023
    # BFS approach, loop all nodes in queue, if node exists then put its children in queue; the last node in the queue is the right side one
    # def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    #     queue = collections.deque([root])
    #     result = []
    #
    #     while queue:
    #         right = None
    #         for i in range(len(queue)):
    #             node = queue.popleft()
    #             if node:
    #                 right = node
    #                 queue.append(node.left)
    #                 queue.append(node.right)
    #         if right:
    #             result.append(right.val)
    #
    #     return result

    # DFS approach, faster than BFS
    # def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    #     result = []
    #
    #     def dfs(node, level):
    #         if not node:
    #             return
    #
    #         if len(result) <= level:
    #             result.append(None)
    #
    #         dfs(node.left, level + 1)
    #         dfs(node.right, level + 1)
    #         result[level] = node.val
    #
    #     dfs(root, 0)
    #     return result

    # 1448. Count Good Nodes in Binary Tree | Diff: Medium | Tags: Tree, Binary Tree, DFS
    # DFS search, keep in mind the max value that was encountered from the parents when calling dfs again
    # !!!
    # def goodNodes(self, root: TreeNode) -> int:
    #     if not root:
    #         return 0
    #
    #     def dfs(node, maxVal):
    #         if not node:
    #             return 0
    #
    #         result = 1 if node.val >= maxVal else 0
    #         maxVal = max(node.val, maxVal)
    #         result += dfs(node.left, maxVal)
    #         result += dfs(node.right, maxVal)
    #
    #         return result
    #
    #     return dfs(root, root.val)

    # 215. Kth Largest Element in an Array | Diff: Medium | Tags: Array, Heap, Quickselect | Date: 06/09/2023
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     for index, val in enumerate(nums):
    #         nums[index] = -val
    #
    #     heapq.heapify(nums)
    #
    #     result = None
    #     while k:
    #         result = heapq.heappop(nums)
    #         k -= 1
    #
    #     return -result

    # 70. Climbing Stairs | Diff: Easy | Tags: Dynamic Programming, Memoization
    # either we climbed one stair from the (n-1)th stair or we climbed two stairs from the (n-2)th stair.
    # use DP top to bottom with memoization
    # def climbStairs(self, n: int) -> int:
    #     steps = [0] * (n + 1)
    #
    #     steps[0] = 1
    #     steps[1] = 1
    #
    #     for i in range(2, n + 1):
    #         steps[i] = steps[i - 1] + steps[i - 2]
    #
    #     return steps[n]

    # 746. Min Cost Climbing Stairs | Diff: Easy | Tags: Array, Dynamic Programming | Date: 06/09/2023
    # Recurrence Relation: min-cost(i) = cost[i]+min(min-cost(i-1), min-cost(i-2))

    # simple recursion
    # def minCostClimbingStairs(self, cost: List[int]) -> int:
    #     def recursive(n):
    #         if n < 2:
    #             return cost[n]
    #
    #         return cost[n] + min(recursive(n - 1), recursive(n - 2))
    #
    #     return min(recursive(len(cost) - 1), recursive(len(cost) - 2))

    ###############
    # DP, bottom up
    # def minCostClimbingStairs(self, cost: List[int]) -> int:
    #     dp = [-1] * len(cost)
    #
    #     dp[0] = cost[0]
    #
    #     if len(cost) >= 2:
    #         dp[1] = cost[1]
    #
    #     for i in range(2, len(cost)):
    #         dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
    #
    #     return min(dp[-1], dp[-2])

    # 198. House Robber | Diff: Medium | Tags: Array, Dynamic Programming | Date: 06/09/2023
    # A robber has 2 options: a) rob current house i; b) don't rob current house.
    # If an option "a" is selected it means he can't rob previous i-1 house but can safely proceed to the one before previous i-2 and gets all cumulative loot that follows.
    # If an option "b" is selected the robber gets all the possible loot from robbery of i-1 and all the following buildings.
    # So it boils down to calculating what is more profitable:
    # robbery of current house + loot from houses before the previous
    # loot from the previous house robbery and any loot captured before that
    # rob(i) = Math.max( rob(i - 2) + currentHouseValue, rob(i - 1) )

    # robber can choose to:
    # a). rob current house -> it means he can ALSO rob house i-2 -> total cost(current) + cost(i-2)
    # b). not rob current house -> it means he can ONLY rob house i-1 -> total cost(i-1)

    # RECURSIVE - too slow
    # def rob(self, nums: List[int]) -> int:
    #     def recursive(index):
    #         if index < 0:
    #             return 0
    #         return max(nums[index] + recursive(index - 2), recursive(index - 1))
    #
    #     return recursive(len(nums) - 1)

    # DP - BOTTOM UP
    # def rob(self, nums: List[int]) -> int:
    #     if len(nums) == 0:
    #         return 0
    #     if len(nums) == 1:
    #         return nums[0]
    #     if len(nums) == 2:
    #         return max(nums)
    #
    #     memo = [0] * len(nums)
    #     memo[0] = nums[0]
    #     memo[1] = max(nums[0], nums[1])
    #
    #     for i in range(2, len(nums)):
    #         memo[i] = max(memo[i - 1], nums[i] + memo[i - 2])
    #
    #     return memo[-1]

    # 200. Number of Islands | Diff: Medium | Tags: Matrix,Graph, BFS, DFS, Union Find | Date: 09/09/2023
    # BFS approach - check all cells in grid, if cell is 1 then use bfs to find all its neighbours and mark them as visited; for each new 1 value that wasn't seen before increment the number of islands
    # def numIslands(self, grid: List[List[str]]) -> int:
    #     rows, cols = len(grid), len(grid[0])
    #     visited = set()
    #     islands = 0
    #
    #     #  bfs receives an origin land and is used to mark the neighbours of that land as visited // all the land of the island, so they will not be counted for the next island
    #     def bfs(row, col):
    #         q = collections.deque()
    #         q.append((row, col))
    #         visited.add((row, col))
    #
    #         directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    #
    #         while q:
    #             curr_row, curr_col = q.popleft()
    #             # for cardinal directions UP, DOWN, LEFT, RIGHT
    #             for row_offset, col_offset in directions:
    #                 new_row, new_col = curr_row + row_offset, curr_col + col_offset
    #
    #                 # check if indexes are in bounds, if the grid values is one <=> is an island, and if the cell was not visited before
    #                 if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] == "1" and (new_row, new_col) not in visited:
    #                     # if the cell is part of the island which contains the original cell then add the current cell to visited, and add it to queue to explore its neighbours
    #                     visited.add((new_row, new_col))
    #                     q.append((new_row, new_col))
    #
    #     # check all cells in the grid
    #     for row in range(rows):
    #         for col in range(cols):
    #             # if cell is land check if it was visited before or not <=> if it's part of a new island or land from an island that was visited before
    #             if grid[row][col] == "1" and (row, col) not in visited:
    #                 # if it's part of a new island use bfs to find its neighbours and add them to the visited set and increment the number of islands
    #                 bfs(row, col)
    #                 islands += 1
    #
    #     return islands

    # DFS APPROACH - SIMILAR WITH 79. Word Search faster than BFS
    # use dfs to mark cell as visited and explore all its neighbours to mark them as well
    # def numIslands(self, grid: List[List[str]]) -> int:
    #     rows, cols = len(grid), len(grid[0])
    #     islands = 0
    #
    #     def dfs(row, col):
    #         if not (0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == "1"):
    #             return
    #
    #         grid[row][col] = "#"
    #         dfs(row + 1, col)
    #         dfs(row - 1, col)
    #         dfs(row, col + 1)
    #         dfs(row, col - 1)
    #
    #     for row in range(rows):
    #         for col in range(cols):
    #             # if cell is land check if it was visited before or not <=> if it's part of a new island or land from an island that was visited before
    #             if grid[row][col] == "1":
    #                 # if it's part of a new island use bfs to find its neighbours and add them to the visited set and increment the number of islands
    #                 dfs(row, col)
    #                 islands += 1
    #
    #     return islands

    # Bubble Sort Unoptimized, right side is sorted part
    # Best: O(n) | Average: O(n^2) | Worst: O(n^2)


if __name__ == '__main__':
    # sol = Solution()
    # res = sol.sortArray([19, 2, 0, 55, 33])
    # print(res)

    a = [(x, x + 1) for x in range(1, 5)]
    print(a)
