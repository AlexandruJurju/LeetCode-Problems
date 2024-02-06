# 1. Two Sum
## 
### Java
#### Method 1 - Two pass method

1. make a hashmap and put all index and value pairs in it <K=index,V=val>
2. loop over all elements in the array and calculate for the complement each one, the difference between target and itself
3. then search the hashmap using the complement as the key => find the elements so that their sum == target

```
public static int[] twoSum(int[] nums, int target) {
	HashMap<Integer, Integer> diffMap = new HashMap<>();
	// create the hashmap with <index,value>
	for (int i = 0; i < nums.length; i++) {
		diffMap.put(nums[i], i);
	}

	for (int i = 0; i < nums.length; i++) {
		int complement = target - nums[i];
		// check if complement can be found in the hashmap & check if the index found in the hashmap is not the same as the current element
		if (diffMap.containsKey(complement) && diffMap.get(complement) != i) {
			return new int[]{i, diffMap.get(complement)};
		}
	}

	return new int[]{};
}
```

#### Method 2 - One Pass Method
loop over all values in the array and check for each one if complement is in hashMap if it is then return it as a result otherwise insert the current element index and val in the hashmap and continue searching

```
public static int[] twoSum(int[] nums, int target) {
	HashMap<Integer, Integer> valMap = new HashMap<>();
	for (int i = 0; i < nums.length; i++) {
		int complement = target - nums[i];
		// check if complement can be found in the hashmap
		if (valMap.containsKey(complement)) {
			return new int[]{i, valMap.get(complement)};
		}
		// if not then add element to hashmap
		valMap.put(nums[i], i);
	}

	return new int[]{};
}
```



# 2. Add two numbers
##
### Java
at the start make a resultNode and a dummyNode
while l1 is not empty, l2 not empty and carry is not empty do
if l1 is not null then add the value to current sum and go to next node
if l2 is not null then add the value to current sum and go to next node
add carry to the current sum, sum = l1.val + l2.val + carry
the value of the node will be sum % 10 to get the smaller val
the value of carry will be sum / 10
make a new node with the value = sum%10 and

public static ListNode addTwoNumbers(ListNode l1, ListNode l2) {
	int carry = 0;
	ListNode dummyHead = new ListNode();
	ListNode result = dummyHead;

	while (l1 != null || l2 != null || carry == 1) {
		int sum = 0;

		if (l1.val != null) {
			sum += l1.val;
			l1 = l1.next;
		}

		if (l2.val != null) {
			sum += l2.val;
			l2 = l2.next;
		}

		sum += carry;
		carry = sum / 10;
		int val = sum % 10;

		ListNode node = new ListNode(val);
		result.next = node;
		result = result.next;

	}

	return dummyHead.next;
}

# 3. Longest Substring Without Repeating Characters
##
### Java
#### Method 1 - use 2 pointers to move in the array and a hashset to store the seen characters
When you see a character that isn't in the hashset add it and increase right index, recalculate max with current hashset size
When you see a character that is in the hashset, remove it, increase left pointer

```
public static int lengthOfLongestSubstring(String s) {
	HashSet<Character> hashSet = new HashSet<>();
	int i = 0;
	int j = 0;
	int max = 0;

	while (j < s.length()) {
		if (hashSet.contains(s.charAt(j))) {
			hashSet.remove(s.charAt(i));
			i++;
		} else {
			hashSet.add(s.charAt(j));
			j++;
			max = Math.max(max, hashSet.size());
		}
	}
	return max;
}
```

# 20. Valid Parenthesis
##
###
####
use a stack to store all open parentheses found in the string
loop over all chars in string, if it finds an open parenthesis it pushes it to the stack
when you find a closing parenthesis, pop the last element from the stack and check if it's a match 
if stack is empty when trying to pop then there are pairs without a match -> false
at the end check if stack still has elements in it, if there are values without a pair -> if yes return false

```
public static boolean isValid(String s) {
	if (s.length() % 2 == 1) {
		return false;
	}

	Stack<Character> charStack = new Stack<>();

	char[] chars = s.toCharArray();
	for (char c : chars) {
		if (c == '(' || c == '[' || c == '{') {
			charStack.push(c);
		} else {
			if (charStack.isEmpty()) {
				return false;
			}
			char popped = charStack.pop();

			if ((c == ')' && popped != '(') ||
					(c == ']' && popped != '[') ||
					(c == '}' && popped != '{')) {
				return false;
			}
		}
	}


	return charStack.isEmpty();
}
```

# 22. Generate Parentheses 
## Diff: Medium | Tags: Backtracking | Date: ?
### Java
#### Method 1 - Use backtracking
https://leetcode.com/problems/generate-parentheses/solutions/3512769/c-java-python-javascript-using-recursion-with-explanation/
We define a helper function, generateParentheses, that takes the following parameters:
	result: a reference to the vector of strings where we store the generated combinations.
	current: the current combination being generated.
	open: the count of opening parentheses "(" included in the current combination.
	close: the count of closing parentheses ")" included in the current combination.
	n: the total number of pairs of parentheses to be included.

In the generateParentheses function, we first check if the length of the current string is equal to 2n. If it is, we have generated a valid combination, so we add it to the result vector and return.

If the length of current is not equal to 2n, we have two choices:
	If the count of opening parentheses open is less than n, we can add an opening parenthesis to the current combination and make a recursive call to generateParentheses, incrementing the open count by 1.
	If the count of closing parentheses close is less than the open count, we can add a closing parenthesis to the current combination and make a recursive call to generateParentheses, incrementing the close count by 1.

In the generateParenthesis function, we initialize an empty result vector and call the generateParentheses function with the initial values of current as an empty string, open and close counts as 0, and n as the input value.

Finally, we return the result vector containing all the generated combinations of well-formed parentheses.

```
public List<String> generateParenthesis(int n) {
	List<String> res = new ArrayList<String>();
	backtrack(res, "", 0, 0, n);
	return res;
}

private void backtrack(List<String> results, String current, int open, int closed, int max) {
	if (current.length() == max * 2) {
		results.add(current);
		return;
	}

	if (open < max) {
		backtrack(results, current + "(", open + 1, closed, max);
	}

	if (closed < open) {
		backtrack(results, current + ")", open, closed + 1, max);
	}

}
```


# 26. Remove Duplicates from Sorted Array
##
### Java
https://leetcode.com/problems/remove-duplicates-from-sorted-array/solutions/3676877/best-method-100-c-java-python-beginner-friendly/
The Intuition is to use two pointers, i and j, to iterate through the array. The variable j is used to keep track of the current index where a unique element should be placed. The initial value of j is 1 since the first element in the array is always unique and doesn't need to be changed

```
public int removeDuplicates(int[] nums) {
	int j = 1;
	for (int i = 1; i < nums.length; i++) {
		if (nums[i] != nums[i - 1]) {
			nums[j] = nums[i];
			j++;
		}
	}
	return j;
}
```

# 27. Remove Element
## Diff: Easy | Tags: Array, Two Pointers | Date: 25/10/2023
### Java
#### Method 1 - use an index to keep track of the numbers of val values AND as a pointer to the current element in nums to be replaced

```
public static int removeElement(int[] nums, int val) {
	int index = 0;

	for (int i = 0; i < nums.length; i++) {
		if (nums[i] != val) {
			nums[index] = nums[i];
			index++;
		}
	}

	return index;
}
```



# 36. Valid Sudoku
## Diff: Medium | Tags: Array, Hash Table, 
### Java
####
use a hashset to store all the seen values in the sudoku board
the square elements can be obtained by dividing row and col numbers by 3
1, 2, 3 -> box 1; 4,5,6 -> box 2; 7,8,9 -> box 3

```
public boolean isValidSudoku(char[][] board) {
	HashSet<String> seen = new HashSet<>();

	for (int i = 0; i < board.length; i++) {
		for (int j = 0; j < board[0].length; j++) {
			char elem = board[i][j];
			if (elem != '.') {
				if (!seen.add(elem + "r" + i) || !seen.add(elem + "c" + j) || !seen.add(elem + "b" + i / 3 + j / 3)) {
					return false;
				}
			}
		}
	}
	return true;
}
```

# 39. Combination Sum
## 
### Java
####
```
public List<List<Integer>> combinationSum(int[] candidates, int target) {
	List<List<Integer>> result = new ArrayList<>();
	backtrack(result, new ArrayList<>(), candidates, target, 0);
	return result;
}

public void backtrack(List<List<Integer>> result, List<Integer> temp, int[] candidates, int remainder, int index) {
	if (remainder == 0) {
		result.add(new ArrayList<>(temp));
	}

	if (remainder < 0) {
		return;
	}

	for (int i = index; i < candidates.length; i++) {
		temp.add(candidates[i]);
		// not i+1 because same candidate can be reused
		backtrack(result, temp, candidates, remainder - candidates[i], i);
		temp.remove(temp.size() - 1);
	}
}
```

# 46. Permutations
##
### Java
####
```
public static List<List<Integer>> permute(int[] nums) {
	List<List<Integer>> solution = new ArrayList<>();
	backtrack(solution, new ArrayList<>(), 0, nums);
	return solution;
}

public static void backtrack(List<List<Integer>> solution, List<Integer> temp, int index, int[] nums) {
	if (temp.size() == nums.length) {
		solution.add(new ArrayList<>(temp));
	}

	for (int i = index; i < nums.length; i++) {
		if (temp.contains(nums[i])) {
			continue;
		}
		temp.add(nums[i]);
		backtrack(solution, temp, index, nums);
		temp.remove(temp.size() - 1);
	}
}
```

# 48. Rotate Image
##
###
#### Method 1 - Use ??? theorem
clockwise rotate
first reverse up to down, then swap the symmetry
1 2 3     7 8 9     7 4 1
4 5 6  => 4 5 6  => 8 5 2
7 8 9     1 2 3     9 6 3

anticlockwise rotate
first reverse left to right, then swap the symmetry
1 2 3     3 2 1     3 6 9
4 5 6  => 6 5 4  => 2 5 8
7 8 9     9 8 7     1 4 7


```
public static int[][] transposeMatrix(int[][] matrix) {
	int rows = matrix.length;
	int cols = matrix[0].length;

	for (int i = 0; i < rows - 1; i++) {
		for (int j = i + 1; j < cols; j++) {
			int temp = matrix[i][j];
			matrix[i][j] = matrix[j][i];
			matrix[j][i] = temp;
		}
	}

	return matrix;
}

public static int[][] reverseVertical(int[][] matrix) {
	int rows = matrix.length;
	int cols = matrix[0].length;

	for (int i = 0; i < rows; i++) {
		for (int j = 0; j < cols / 2; j++) {
			int temp = matrix[i][j];
			matrix[i][j] = matrix[i][cols - 1 - j];
			matrix[i][cols - 1 - j] = temp;
		}
	}

	return matrix;
}

public static int[][] rotate90DegreesClockwise(int[][] matrix) {
	return reverseVertical(transposeMatrix(matrix));
}
```

# 49. Group Anagrams
##
### Java
#### Method 1 -
Use a hashmap that contains the sorted string as a key, and a list of all words that have the sorted characters as a value
For each word in strs: sort the characters, check if hashmap contains the sorted word, if not then init a blank ArrayList, at the end add the word to the ArrayList using the key
```
public List<List<String>> groupAnagrams(String[] strs) {
	HashMap<String, List<String>> anagramMap = new HashMap<>();
	for (int i = 0; i < strs.length; i++) {
		char[] strChars = strs[i].toCharArray();
		Arrays.sort(strChars);

		// tried using char[] as key, but the map says it cannot find the key
		String sortedWord = new String(strChars);

		// if hashmap doesn't have the anagram, then add it with an empty list
		if (!anagramMap.containsKey(sortedWord)) {
			anagramMap.put(sortedWord, new ArrayList<>());
		}

		// get the list of the anagram and add the word to it
		anagramMap.get(sortedWord).add(strs[i]);
	}
	return new ArrayList<>(anagramMap.values());
}
```


# 61. Rotate List
## Diff: Medium | Tags: Linked List, Two Pointers | Date: Date: 17/10/2023
### Java
#### Method 1 - https://www.youtube.com/watch?v=UcGtPs2LE_c
public static ListNode rotateRight(ListNode head, int k) {
	// if head is null return null
	if (head == null) {
		return null;
	}

	// find length and tail node of the list
	int length = 1;
	ListNode tail = head;
	while (tail.next != null) {
		tail = tail.next;
		length++;
	}

	// if number of rotates is multiple of k then the list stays the same, use k%length to find the number of real rotates
	k = k % length;

	// if k == 0 then number of rotates is divisible by k, so the resulting list would be the same
	if (k == 0) {
		return head;
	}

	// find the cutoff position in the linked list, the kth node from the tail of the list
	ListNode current = head;
	for (int i = 0; i < length - k - 1; i++) {
		current = current.next;
	}

	ListNode newHead = current.next;
	current.next = null;
	tail.next = head;

	return newHead;
}

# 78. Subsets
## 
### Java
#### Method 1 - backtracking loop from index to num length
```
public static List<List<Integer>> subsets(int[] nums) {
	List<List<Integer>> result = new ArrayList<>();
	List<Integer> current = new ArrayList<>();
	int index = 0;

	backtrack(result, current, index, nums);
	return result;
}

public static void backtrack(List<List<Integer>> results, List<Integer> current, int index, int[] nums) {
	results.add(new ArrayList<>(current));

	for (int i = index; i < nums.length; i++) {
		current.add(nums[i]);
		backtrack(results, current, i + 1, nums);
		current.remove(current.size() - 1);
	}
}
```

#### Method 2 - changed backtrack function
```
public static List<List<Integer>> subsets(int[] nums) {
	List<List<Integer>> result = new ArrayList<>();
	List<Integer> current = new ArrayList<>();
	int index = 0;

	backtrack(result, current, index, nums);
	return result;
}

public static void backtrack(List<List<Integer>> results, List<Integer> current, int index, int[] nums) {
	if (index == nums.length) {
		results.add(new ArrayList<>(current));
		return;
	}

	current.add(nums[index]);
	backtrack(results, current, index + 1, nums);

	current.remove(current.size() - 1);
	backtrack(results, current, index + 1, nums);
}
```

# 94. Binary Tree Inorder Traversal - Inorder S,R,D
##
### Java
#### Method 1. Recursive with another function
public List<Integer> inorderTraversal(TreeNode root) {
	List<Integer> list = new ArrayList<Integer>();
	inorder(root, list);
	return list;
}

public void inorder(TreeNode root, List<Integer> nums) {
	if (root == null) return;
	inorder(root.left, nums);
	nums.add(root.val);
	inorder(root.right, nums);
}

#### Method 2. Iterative method
public List<Integer> inorderTraversal(TreeNode root) {
	List<Integer> list = new ArrayList<Integer>();
	Stack<TreeNode> stack = new Stack<TreeNode>();
	TreeNode cur = root;

	while (cur != null || !stack.empty()) {
		while (cur != null) {
			stack.add(cur);
			cur = cur.left;
		}
		cur = stack.pop();
		list.add(cur.val);
		cur = cur.right;
	}

	return list;
}

# ?. Is Same Tree
##
### Java
#### Method 1 - Recursive method
https://leetcode.com/problems/same-tree/solutions/3746149/recursive-approach-with-easy-steps/

```
public boolean isSameTree(TreeNode p, TreeNode q) {
	if (p != null && q != null) {
		return p.val == q.val && isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
	} else {
		return p == q;
	}
}

public boolean isSameTree(TreeNode p, TreeNode q) {
	if (p == null && q == null) // Same Tree
		return true;
	if (p == null || q == null) // Different Size
		return false;
	if (p.val != q.val) // Different Nodes
		return false;
	return isSameTree(p.left, q.left) && // check left subtree
			isSameTree(p.right, q.right); // check right subtree
}
```

# 104. Maximum Depth of Binary Tree
##
### Java
public int maxDepth(TreeNode root) {
	if (root == null) {
		return 0;
	}

	return Math.max(maxDepth(root.left) + 1, maxDepth(root.right) + 1);
}


# 108. Convert Sorted Array to Binary Search Tree
## Diff: Easy | Tags: Binary Search Tree, Tree, Binary Tree, Divide and Conquer | Date: 04/02/2023
### Java
#### Method 1 - Binary Search
Nums is a sorted list, so the middle element nums[mid] is the root of the BST
The next elements of the tree are found by taking the middle elements of the subarrays

public TreeNode sortedArrayToBST(int[] nums) {
	return toBST(nums, 0, nums.length - 1);
}

public TreeNode toBST(int nums[], int left, int right) {
	if (left > right) {
		return null;
	}

	int mid = (left + right) / 2;
	TreeNode root = new TreeNode(nums[mid]);
	root.left = toBST(nums, left, mid - 1);
	root.right = toBST(nums, mid + 1, right);
	return root;
}

# 110. Balanced Binary Tree
##
### Java
####
```
public int height(TreeNode root) {
	if (root == null) {
		return 0;
	}

	return Math.max(height(root.left) + 1, height(root.right) + 1);
}

public boolean isBalanced(TreeNode root) {
	if (root == null) {
		return true;
	}
	if (Math.abs(height(root.left) - height(root.right)) > 1) {
		return false;
	} else {
		return isBalanced(root.left) && isBalanced(root.right);
	}
}
```

# 128. Longest Consecutive Sequence
## Diff: Medium | Tags: Array, Hash Table, Union Find
### Java
#### Method 1 - Use a hashset
Use a hashset that contains all the values inside the array. Loop over all values in array and search the hashset to find all values in an incrementing sequence and all values in a decrementing sequence from the current value, for each value in sequence increment the max;

```
public int longestConsecutive(int[] nums) {
	HashSet<Integer> numSet = new HashSet<>();

	// init HasSet with array values
	for (int num : nums) {
		numSet.add(num);
	}

	int longest = 0;
	for (int current : nums) {
		int next = current + 1;
		int prev = current - 1;
		int max = 1;

		// loop over values that are smaller than the current one in order
		while (numSet.contains(prev)) {
			numSet.remove(prev--);
			max++;
		}

		// loop over values that are bigger than the current one in order
		while (numSet.contains(next)) {
			numSet.remove(next++);
			max++;
		}

		longest = Math.max(longest, max);
	}
	return longest;
}
```

# 150. Evaluate Reverse Polish Notation
##
### Java
#### Method 1 - If it's a number add it to the stack, if it's an operator pop 2 values, apply operator, push result to the stack
```
public static int evalRPN(String[] tokens) {
	Stack<Integer> stack = new Stack<>();
	for (String token : tokens) {
		switch (token) {
			case "+" -> {
				int val1 = stack.pop();
				int val2 = stack.pop();
				stack.push(val2 + val1);
			}
			case "-" -> {
				int val1 = stack.pop();
				int val2 = stack.pop();
				stack.push(val2 - val1);
			}
			case "*" -> {
				int val1 = stack.pop();
				int val2 = stack.pop();
				stack.push(val2 * val1);
			}

			case "/" -> {
				int val1 = stack.pop();
				int val2 = stack.pop();
				stack.push(val2 / val1);
			}

			default -> stack.push(Integer.valueOf(token));
		}
	}
	return stack.pop();
}
```

# 153. Find Minimum in Rotated Sorted Array
## Diff: Med | Tags: Binary Search | Date: ?
### Java
```
public int findMin(int[] nums) {
    int left = 0;
    int right = nums.length - 1;

    while (left <= right) {
        int middle = (left + right) / 2;
        int middleElement = nums[middle];

        if (left == right) {
            return middleElement;
        }

        if (middleElement > nums[right]) {
            left = middle + 1;
        } else {
            right = middle;
        }

    }

    return -1;
}
```

# 167. Two Sum II - Input Array Is Sorted
##
###
#### Method 1 - use 2 pointers
use 2 pointers, left and right to choose elements in the sorted array
if sum of num1 and num2 is bigger than the target then decrement right to lower the value of the sum
if sum of num1 and num2 is smaller than the target then increment left to raise the value of the sum

```
public int[] twoSum(int[] numbers, int target) {
	int left = 0, right = numbers.length - 1;

	while (left <= right) {
		int sum = numbers[left] + numbers[right];

		if (sum == target) {
			return new int[]{left + 1, right + 1};
		} else if (sum > target) {
			right--;
		} else {
			left++;
		}
	}

	return new int[]{-1, -1};
}
```

# 200. Number of islands ???
```
public static int numIslands(char[][] grid) {
	int islandCount = 0;
	for (int i = 0; i < grid.length; i++) {
		for (int j = 0; j < grid[0].length; j++) {
			if (grid[i][j] == '1') {
				islandCount++;
				DFSSink(grid, i, j);
			}
		}
	}
	return islandCount;
}

// recursive DFS function
public static void DFSSink(char[][] grid, int i, int j) {
	if (i < 0 || j < 0 || i >= grid.length || j >= grid[0].length || grid[i][j] != '1') {
		return;
	}

	grid[i][j] = '0';
	DFSSink(grid, i + 1, j);
	DFSSink(grid, i - 1, j);
	DFSSink(grid, i, j + 1);
	DFSSink(grid, i, j - 1);
}
```

# 206. Reverse Linked List
##
###
####
```
public ListNode reverseList(ListNode head) {
	ListNode current = head;
	ListNode previous = null;

	while (current != null) {
		ListNode next = current.next;
		current.next = previous;
		previous = current;
		current = next;
	}

	return previous;
}
```

# 226. Invert Binary Tree
##
###
####
```
public static TreeNode invertBinaryTree(TreeNode root) {
	if (root == null) {
		return root;
	}

	invertBinaryTree(root.left);
	invertBinaryTree(root.right);

	// when the 2 recursion calls are done, the root node contains the edge left node and the edge right node
	// swap the nodes before returning root
	TreeNode tmp = root.left;
	root.left = root.right;
	root.right = tmp;

	return root;
}
```

# 238. Product of Array Except Self
## Diff: Medium | Tags: Array, Prefix Sum
### Java
#### Method 1 - https://www.youtube.com/watch?v=bNvIQI2wAjk
For each number calculate a prefix product of all elements before the value, and postfix product of all elements after the value
The product of all values except self is the previous value in prefix and the next value in postfix

```
public static int[] productExceptSelf(int[] nums) {
	int length = nums.length;
	int[] prefix = new int[length], postfix = new int[length], res = new int[length];

	prefix[0] = nums[0];
	postfix[length - 1] = nums[length - 1];

	for (int i = 1; i < length; i++) {
		prefix[i] = prefix[i - 1] * nums[i];
	}

	for (int i = length - 2; i >= 0; i--) {
		postfix[i] = postfix[i + 1] * nums[i];
	}

	for (int i = 0; i < length; i++) {
		int pref = 1;
		int post = 1;
		if (i > 0) {
			pref = prefix[i - 1];
		}
		if (i < length - 1) {
			post = postfix[i + 1];
		}

		res[i] = pref * post;
	}

	return res;
}
```

# 240. Search a 2d Matrix
##
### Java
#### Method 1 - use 2 pointers
start looking in the matrix from the bottom left element and value of current element
bottom left element was chosen because if we go up then there are only smaller values and if we go right there are bigger values
if current element < target then increment col index to find bigger number
if current element > target then increment row index to find lower number

```
public boolean searchMatrix(int[][] matrix, int target) {
	int rows = matrix.length, cols = matrix[0].length;
	int row = matrix.length - 1, col = 0;

	while (row >= 0 && col < cols) {
		int elem = matrix[row][col];

		if (elem == target) {
			return true;
		}

		if (target > elem) {
			col += 1;
		}
		if (target < elem) {
			row -= 1;
		}
	}
	return false;
}
```


# 242. Valid Anagram
##
###
#### Method 1 - Sort the chars
Anagrams - if the letters of word 1 can be arranged to form word 2 -> then they are anagrams
Convert the strings int char arrays, sort the arrays and then compare them, if they are different that means that the words cannot be anagrams

```
public boolean isAnagram(String s, String t) {
	// if they are different length that => not anagrams
	if (s.length() != t.length()) {
		return false;
	}

	char[] sChars = s.toCharArray();
	char[] tChars = t.toCharArray();

	Arrays.sort(sChars);
	Arrays.sort(tChars);

	return Arrays.equals(sChars, tChars);
}
```

#### Method 2 -

# 271. Contains Duplicate
##
### Java
#### Method 1 - Sorting -> the array and check the next element if it equals the current one

```
public boolean containsDuplicate(int[] nums) {
	Arrays.sort(nums);
	for (int i = 0; i < nums.length - 1; i++) {
		if (nums[i] == nums[i + 1]) {
			return true;
		}
	}
	return false;
}
```

#### Method 2 - Hashset
create a hashset then loop over elements in array for each element check if its already in the hashset
if it is then the array contains a duplicate -> return true otherwise add it to the hashset and continue checking
if loop finishes without finding any elements in the hashset then there are no duplicates -> return false

```
public static boolean containsDuplicate(int[] nums) {
	HashSet<Integer> seen = new HashSet<>();

	for (int num : nums) {
		if (seen.contains(num)) {
			return true;
		}
		seen.add(num);
	}

	return false;
}
```

# 347. Top K Frequent Elements
##
### Java
#### Method 1 - Use a maxheap
Use a hashmap with <Key=NumValue,Value=Frequency> to find the frequency of the elements in the array. Then use a maxheap to get the max element, the element with the hightest frequency from the map

```
public int[] topKFrequent(int[] nums, int k) {
	HashMap<Integer, Integer> frequencyMap = new HashMap<>();
	for (int elem : nums) {
		// increment value in map if key is present, otherwise use 0 as default value to increment
		frequencyMap.put(elem, frequencyMap.getOrDefault(elem, 0) + 1);
	}

	// define the priority of the queue, max value
	PriorityQueue<Integer> maxHeap = new PriorityQueue<>((a, b) -> frequencyMap.get(b) - frequencyMap.get(a));
	maxHeap.addAll(frequencyMap.keySet());

	int[] res = new int[k];
	for (int i = 0; i < k; i++) {
		res[i] = maxHeap.poll();
	}
	return res;
}
```

# 463. Island Perimeter
## Diff: Easy | Tags: DFS, BFS | Date: 29/01/2024

Use BFS or DFS to iterate over all 1s inside of an island
When 1 is encountered increment the counter and replace 1 with another value
Then look at the neighbours

### Java
public int islandPerimeter(int[][] grid) {
	if (grid == null) {
		return 0;
	}

	for (int i = 0; i < grid.length; i++) {
		for (int j = 0; j < grid[0].length; j++) {
			if (grid[i][j] == 1) {
				return calculatePerimeter(grid, i, j);
			}
		}
	}

	return 0;
}

public static int calculatePerimeter(int[][] grid, int i, int j) {
	if (i < 0 || i >= grid.length || j < 0 || j >= grid[0].length) {
		return 1;
	}

	if (grid[i][j] == 0) {
		return 1;
	}

	if (grid[i][j] == -1) {
		return 0;
	}

	int count = 0;
	grid[i][j] = -1;
	count += calculatePerimeter(grid, i + 1, j);
	count += calculatePerimeter(grid, i - 1, j);
	count += calculatePerimeter(grid, i, j + 1);
	count += calculatePerimeter(grid, i, j - 1);

	return count;
}

# 572. Subtree of Another Tree
##
### Java
#### Method 1 - recursive use isSameTree function
```
public boolean isSameTree(TreeNode p, TreeNode q) {
	if (p == null && q == null) {
		return true;
	}

	if (p == null || q == null || p.val != q.val) {
		return false;
	}

	return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
}

public boolean isSubtree(TreeNode root, TreeNode subRoot) {
	if (subRoot == null) {
		return true;
	}

	if (root == null) {
		return false;
	}

	return isSameTree(root, subRoot) || isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot);
}
```

# 682. Baseball Game
## Diff: Easy | Tags: Stack | Date: 25/10/2023
### Java
```
public static int calPoints(String[] operations) {
	Stack<Integer> vals = new Stack<Integer>();
	int total = 0;

	for (String s : operations) {
		switch (s) {
			case "+" -> {
				int num1 = vals.pop();
				int res = (vals.peek() + num1);
				vals.push(num1);
				vals.push(res);
			}
			case "D" -> vals.push(vals.peek() * 2);
			case "C" -> vals.pop();
			default -> vals.push(Integer.valueOf(s));
		}
	}

	while (!vals.isEmpty()) {
		total += vals.pop();
	}

	return total;
}
```

# 700. Search in a Binary Search Tree
## ???
### Java
public TreeNode searchBST(TreeNode root, int val) {
	if (root == null) {
		return null;
	}

	if (root.val == val) {
		return root;
	}

	if (root.val > val) {
		return searchBST(root.left, val);
	} else {
		return searchBST(root.right, val);
	}
}

# 704. Binary Search 
##
###
####
```
public int search(int[] nums, int target) {
	int length = nums.length;

	if (length == 0) {
		return -1;
	}

	// length is total number of elements
	// right is the rightmost index, and because numbering is from 0, right should be length - 1
	int right = length - 1;
	int left = 0;

	while (left <= right) {
		int middle = (left + right) / 2;
		int element = nums[middle];

		if (element == target) {
			return middle;
		}

		if (target < element) {
			right = middle - 1;
		}

		if (target > element) {
			left = middle + 1;
		}
	}

	return -1;
}
```

# Isogram
public static boolean isIsogram(String input) {

    input = input.toLowerCase();
    HashSet<Character> characters = new HashSet<>();

    for (char c : input.toCharArray()) {
        if (characters.contains(c)) {
            return false;
        } else {
            characters.add(c);
        }
    }

    return true;
}