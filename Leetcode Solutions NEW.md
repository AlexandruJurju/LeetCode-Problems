# 1. Two Sum
## Difficulty: Easy
## Topics: Hash Map
#### Method 1 - Dictionary / HashMap
- Calculate a complement (current - target) value for each number in the array. Use a dictonary to store the complements and the ideces that have been found
- In each pass check if complement of the current value can be found in the dict

```csharp
public int[] TwoSum(int[] nums, int target)
{
	// dictionary to store the complements <Value, Index>
	var dictionary = new Dictionary<int, int>();

	for (int i = 0; i < nums.Length; i++)
	{
		// calculate the complement, the difference required to make up the target
		var complement = target - nums[i];

		// if the target value is contained in the dictionary
		if (dictionary.TryGetValue(complement, out var index) && index != i)
		{
			// return current index and the index of the complement
			return [i, index];
		}

		// if the complement hasn't been found in the dictionary then add the current value to the dictionary
		dictionary.TryAdd(nums[i], i);
	}

	return [0];
}
```

# 3. Longest Substring Without Repeating Characters
## Difficulty: Medium
## Topics: Sliding Window, Hash Map

### Solution 1 - Sliding window and hashset
#### Beats: 68%
- Sliding window and hashset to store seen characters
- While `s[right]` isn't contained in hashSet continue to increment right
- When a duplicate is found remove character `s[left]` from hashSet and increment left until the duplicate is removed from the hashSet
  - This allows the search to continue in a new substring without duplicate characters 
  - Ex: a b c d e, if c is added a,b,c get removed from the hashSet -> the resulting hashSet is d, e, c left is on d and right is on c

```csharp
public int LengthOfLongestSubstring(string s)
{
	// use a set to store the chars that have been seen already
	var seen = new HashSet<char>();
	int maxLength = 0;
	int left = 0;

	for (int right = 0; right < s.Length; right++)
	{
		// if seen doesn't contain s[right] then it's a new unique char
		if (!seen.Contains(s[right]))
		{
			// add it to seen and update maxLength
			seen.Add(s[right]);
			maxLength = Math.Max(maxLength, right - left + 1);
		}
		// if current char has been seen then left pointer needs to be moved until the duplicate is removed from the set
		// after left is moved the duplicate character from right can be added to continue the search in a new substring
		else
		{
			while (seen.Contains(s[right]))
			{
				seen.Remove(s[left]);
				left++;
			}

			seen.Add(s[right]);
		}
	}

	return maxLength;
}
```

# 11. Container With Most Water
## Difficulty: Medium
## Topics: Two Pointers, Greedy

### Solution 1 
- Two pointers, one at the start and one at the end of the array
- In each iteration:
  - calculate current area of the box by picking the smallest of the 2 walls and multiply with the length
  - update the pointers so that the pointer of the smallest wall gets moved to the next position

```csharp
public class Solution
{
    public int MaxArea(int[] height)
    {
        int left = 0;
        int right = height.Length - 1;
        int maxWater = 0;

        while (left < right)
        {
            // The lowest wall gives the limit for the water
            int currentArea = Math.Min(height[left], height[right]) * (right - left);

            maxWater = Math.Max(maxWater, currentArea);

            if (height[left] < height[right])
            {
                left++;
            }
            else
            {
                right--;
            }
        }

        return maxWater;
    }
}
```


# 13. Roman to Integer
## Difficulty: Easy
## Topics: Hash Map, Math, String
###
- The value of some numerals change based on the next highest value
- To solve this compare the current value to the next one
  - If the `current value` is bigger than the next value then current value is added
  - If the `current value` is smaller than the next value then current value is subtracted

```csharp
public int RomanToInt(string s)
{
	var sum = 0;
	var chars = s.ToCharArray();

	for (int i = 0; i < chars.Length - 1; i++)
	{
		var currentValue = GetNumeralValue(chars[i]);
		var nextValue = GetNumeralValue(chars[i + 1]);

		sum += (currentValue < nextValue ? -1 : 1) * currentValue;
	}

	sum += GetNumeralValue(chars[chars.Length - 1]);

	return sum;
}

public int GetNumeralValue(char c)
{
	switch (c)
	{
		case 'I': return 1;
		case 'V': return 5;
		case 'X': return 10;
		case 'L': return 50;
		case 'C': return 100;
		case 'D': return 500;
		case 'M': return 1000;
		default: return 0;
	}
}
```

# 14. Longest Common Prefix
## Difficulty: Easy
## Topics: String, Trie

### Solution 1 - Sort the array
- Sorting the strings and then comparing the first and last elements will make it possible to find the common prefix for all the strings

```csharp
using System.Text;

public class Solution
{
    public string LongestCommonPrefix(string[] strs)
    {
        var sBuilder = new StringBuilder();

        Array.Sort(strs);
        var first = strs[0];
        var second = strs[strs.Length - 1];
		// only look for the mininum string length
        int minLength = Math.Min(first.Length, second.Length);

        for (int i = 0; i < minLength; i++)
        {
            if (first[i] != second[i]) break;
            sBuilder.Append(first[i]);
        }

        return sBuilder.ToString();
    }
}
```

### Solution 2 - Loop over all strings
- Find the length of the smallest string 
- Compare the characters of the smallest word for all the words
- If there are any mismatches return

```csharp
using System.Text;

public class Solution
{
    public string LongestCommonPrefix(string[] strs)
    {
        int minLength = Int32.MaxValue;
        foreach (var str in strs)
        {
            minLength = Math.Min(minLength, str.Length);
        }

        int index = 0;
        while (index < minLength)
        {
            foreach (var s in strs)
            {
                if (s[index] != strs[0][index])
                {
                    return s.Substring(0, index);
                }
            }
            index++;
        }

        return strs[0].Substring(0, index);
    }
}
```



# 15. 3Sum
## Difficulty: Medium
## Topics: Binary Search, Two Pointers, Sorting

### Solution 1 
- Like 2Sum but an element is a pivot and doesn't change

```csharp
using System;
using System.Collections.Generic;

class Solution
{
    public IList<IList<int>> ThreeSum(int[] nums)
    {
        var result = new List<IList<int>>();

        Array.Sort(nums);

        for (int i = 0; i < nums.Length; i++)
        {
            // Skip checking for duplicate values - have been checked in the last iteration
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            
            int target = -nums[i];

            // Start checking from the next element to the end
            int left = i + 1;
            int right = nums.Length - 1;
            while (left < right)
            {
                int currentSum = nums[left] + nums[right];
                if (currentSum == target)
                {
                    result.Add(new List<int>() { nums[i], nums[left], nums[right] });
                    
                    // Skip duplicate left and right elements
                    while (left < right && nums[left] == nums[left + 1]) left++;
                    while (left < right && nums[right] == nums[right - 1]) right--;
                    
                    // Jump to next elements
                    left++;
                    right--;
                }
                // If currentSum < target it means we need a bigger element - because array is sorted incrementing left index will increase the sum 
                else if (currentSum < target)
                {
                    left++;
                }
                // If currentSum > target it means we need a lower element - because array is sorted decrementing right index will lower the sum 
                else
                {
                    right--;
                }
            }
        }

        return result;
    }
}
```

# 20. Valid Parentheses
## Difficulty: Easy  
## Topics: Stack, String  
### Solution 1 - Stack for pairs
- **Loop over all characters in the input string:**
   - If the character is an opening parenthesis (`(`, `[`, `{`), push it onto the stack
   - If the character is a closing parenthesis (`)`, `]`, `}`), pop the top element from the stack and check if it matches the corresponding opening parenthesis, if they dont match → return `false`
   - If no element can be popped (stack is empty), the parentheses are not valid → return `false`
---

```csharp
public bool IsValid(string s)
{
    // If the string length is odd, it cannot be valid
    if (s.Length % 2 == 1) return false;

    Stack<char> parenthesesStack = new Stack<char>();

    foreach (char c in s)
    {
        if (c == '(' || c == '[' || c == '{')
        {
            // Push opening parentheses onto the stack
            parenthesesStack.Push(c);
        }
        else
        {
            // If the stack is empty then there is no matching paranthesis -> false
            if (!parenthesesStack.TryPop(out var popped))
            {
                return false;
            }

            // Check if the popped parenthesis matches the current closing one
            if ((c == ')' && popped != '(') || 
                (c == ']' && popped != '[') || 
                (c == '}' && popped != '{'))
            {
                return false;
            }
        }
    }

    // If the stack is not empty, some parentheses are unpaired
    return parenthesesStack.Count == 0;
}
```

### Solution 2 - Stack optimized
- When encountering an opening paranthesis put the closing one in the stack
- When encountering a closing paranthesis pop the stack and see if they match

```csharp
public bool IsValid(string s) {
	var k = new Stack<char>();

	foreach(char c in s) {

		if (c == '(') { k.Push(')'); continue; }

		if (c == '{') { k.Push('}'); continue; }

		if (c == '[') { k.Push(']'); continue; }

		if (k.Count == 0 || c != k.Pop()) return false;
	}

	return k.Count == 0;
}
```

# 22. Generate Parantheses
## Difficulty: Medium
## Topics: Backtracking, Dynamic Programming

### Soltution 1 - Backtracking

```
https://leetcode.com/problems/generate-parentheses/solutions/1131364/clear-and-simple-explanation-with-intuition-100-faster
Concept: In every backtracking problem , there are two things to keep in mind , which we will explore here as well :

Base Case: Every problem of backtracking has some base case which tells us at which point we have to stop with the recursion process. In our case, when the length of our string has reached the maximum length(n*2), we stop with the recursion for that case and that is our base case.

Conditions: On observing carefully we find that there are two conditions present:

For adding (: If number of opening brackets(open) is less than the the given length(n) i.e.
if max<n, then we can add (,else not.
For adding ): If number of close brackets(close) is less than the opening brackets(open), i.e.
if open<close, we can add ), else not
```

```csharp
public class Solution
{
    public IList<string> GenerateParenthesis(int n)
    {
        var result = new List<string>();
        Solve(result, "", 0, 0, n);
        return result;
    }

    private void Solve(IList<string> result, string current, int open, int close, int max)
    {
        // Base case: if the current string length is equal to 2 * max, there are max number of pairs in the string - the string is a result
        if (current.Length == max * 2)
        {
            result.Add(current);
            return;
        }

        // If the number of open parentheses is lower than the max number of pairs -> try adding a new opening parenthesis
        if (open < max)
        {
            Solve(result, current + "(", open + 1, close, max);
        }

        // If the number of open parentheses is bigger than the number of closed parentheses -> try adding a closing parenthesis to make a pair
        // This condition makes it so the opening parentheses can never be more than closing ones, '(()' cannot add a new '('
        if (open > close)
        {
            Solve(result, current + ")", open, close + 1, max);
        }
    }
}
```

# 26. Remove Duplicates from Sorted Array
## Difficulty: Medium
## Topics: Two Pointers

### Solution 1 - Two pointers
- Left pointer is on the last element without a duplicate, right pointer is incremented until the end of the array
- In each iteration check if `nums[left]` != `nums[right]`
  - If not then increment right pointer (move right until a new element is found)
  - If yes then overwrite the element at `left+1` with the element at `nums[right]` and increment left pointer (overwrite duplicate elements with new ones)
- Return `left` as the number of unique elements

```csharp
public int RemoveDuplicates(int[] nums)
{
	int left = 0;
	int right = 1;
	
	while (right < nums.Length)
	{
		// if a new element is found - overwrite duplicate at left + 1 with the new element
		// move left to point to the new unique element
		if (nums[right] != nums[left])
		{
			nums[left + 1] = nums[right];
			left++;
		}

		right++;
	}

	return left + 1;
}
```

# 27. Remove Element
## Difficulty: Easy
## Topics: Two Pointers

### Solution 1 - Two Pointers
- Similar to #26 - use two pointers
  - left is the index where val was found, the index where a new value needs to be put
  - right is the index where the first non val value is found
- In each iteration check if `nums[right] != val`
  - if not then keep incrementing right
  - if yes then overwrite `nums[left]` with `nums[right]`

```csharp
public int RemoveElement(int[] nums, int val)
{
	int left = 0;
	int right = 0;

	while (right < nums.Length)
	{
		if (nums[right] != val)
		{
			nums[left] = nums[right];
			left++;
		}

		right++;
	}

	return left;
}
```

### Solution 1.1 - 
```csharp
public int RemoveElement(int[] nums, int val)
{
	int left = 0;

	for (int right = 0; right < nums.Length; right++)
	{
		if (nums[right] != val)
		{
			nums[left] = nums[right];
			left++;
		}
	}

	return left;
}
```

# 36. Valid Sudoku
## Difficulty: Medium
## Topics: Hash table

### Solution 1 - Hashset
- Can't have same number in the row, column, or 3x3 subgrid
- To check for duplicates use a hashset using a string made up of the number and the position
- To check for the duplicates inside a box divide row and column by 3 => rows 0,1,2 - box 0, rows 3,4,5 - box 1

```csharp
public bool IsValidSudoku(char[][] board)
{
	HashSet<string> seen = new();
	for (int row = 0; row < 9; row++)
	{
		for (int col = 0; col < 9; col++)
		{
			char current = board[row][col];
			if (current == '.') continue;

			if (!seen.Add(current + "in row" + row) ||
				!seen.Add(current + "in column" + col) ||
				!seen.Add(current + "in block" + row / 3 + "-" + col / 3))
				return false;
		}
	}

	return true;
}
```

# 49. Group Anagrams
## Difficulty: Medium
## Topics: Hash Map
### Solution 1 - Dictionary with sorted word as the key
- Use a dictionary to keep the words that make up the same anagram
- Use the sorted word as the key for the dictionary

```csharp
public IList<IList<string>> GroupAnagrams(string[] strs)
{
	var anagrams = new Dictionary<string, IList<string>>();

	foreach (var str in strs)
	{
		// the key is a new string that is the sorted original word
		char[] ch = str.ToCharArray();
		Array.Sort(ch);
		string key = new string(ch);

		if (!anagrams.ContainsKey(key))
		{
			anagrams[key] = new List<string>();
		}

		anagrams[key].Add(str);
	}

	return anagrams.Values.ToList();
}
```

### Solution 2 - Dictionary with sum of chars as the key
- Use a dictionary to store the anagrams, the key is the sum of the chars and the value is a list of all the anagrams that have that sum / those letters
- Because the sum can be made with different words, the key is a string made up of the count of each char

```csharp
public IList<IList<string>> GroupAnagrams(string[] strs)
{
	var anagrams = new Dictionary<string, IList<string>>();

	foreach (var str in strs)
	{
		int[] charsCount = new int[26];
		
		foreach (char c in str)
			charsCount[c - 'a']++;
		
		string key = string.Join(", ", charsCount);

		if (!anagrams.ContainsKey(key))
		{
			anagrams[key] = new List<string>();
		}
		anagrams[key].Add(str);
	}

	return anagrams.Values.ToList();
}
```

### Solutin 3 - LINQ GroupBy
```csharp
public IList<IList<string>> GroupAnagrams(string[] strs)
{
	return strs
		.GroupBy(str => new string(str.OrderBy(c => c).ToArray()))
		.Select(g => g.ToList() as IList<string>)
		.ToList();
}
```

# 58. Length of Last Word
## Difficulty: Easy
## Topics: String

### Solution 1 
```csharp
public class Solution {
    public int LengthOfLastWord(string s)
    {
        s = s.Trim();
        int length = 0;
        
        for (int i = s.Length - 1; i >= 0; i--)
        {
            if (s[i] != ' ')
            {
                length++;
            }
            else
            {
                return length;
            }
        }

        return length;
    }
}
```

# 74. Search a 2D Matrix
## Difficulty: Medium
## Topics: Binary Search

### Solution 1 -
```csharp
public class Solution
{
    public bool SearchMatrix(int[][] matrix, int target)
    {
        int rowLength = matrix.Length;
        int colLength = matrix[0].Length;
        int left = 0;
        int right = rowLength * colLength - 1;
        
        int minValue = matrix[0][0];
        int maxValue = matrix[rowLength - 1][colLength - 1];
        if (target < minValue || target > maxValue) return false;

        while (left <= right)
        {
            int mid = left + (right - left) / 2;
            
            int row = mid / n; 
            int col = mid % n;
            
            int midVal = matrix[row][col];

            if (midVal == target) return true;

            if (midVal < target)
                left = mid + 1;
            else
                right = mid - 1;
        }

        return false;
    }
}
```

### Solution 2 -
- Each row contains an array of sorted elements, so each element in a row is in interval `leftElement < element < rightElement`
- Searching is done

```csharp
public class Solution
{
    public bool SearchMatrix(int[][] matrix, int target)
    {
        int row = 0;
        int col = 0;
        int rowLength = matrix.Length;
        int colLength = matrix[0].Length;

        int minValue = matrix[0][0];
        int maxValue = matrix[rowLength - 1][colLength - 1];

		// if target is less than min value of the matrix or bigger than max value -> false
        if (target < minValue || target > maxValue) return false;

        while (row < rowLength && col < colLength)
        {
            // First and last elements of the current sorted array 
            int left = matrix[row][col];
            int right = matrix[row][colLength - 1];

            // If target is bigger than the last element of current row it means that we need to try searching in the next row with bigger elements 
            // jump to next row and reset column index
            if (target > right)
            {
                row++;
                col = 0;
                continue;
            }

            // If target can be found in the current row / sorted array then search for it
            if (target >= left && target <= right)
            {
                while (col < colLength)
                {
                    if (matrix[row][col] == target)
                    {
                        return true;
                    }
                    
                    // Jump to the next column
                    col++;
                }
            }
            // If target is bigger than the max of the last row, but cannot be found in current row -> false
            else
            {
                return false;
            }
        }

        return false;
    }
}
```

# 88. Merge Sorted Array
## Difficulty: Easy
## Topics: Two Pointers, Sorting

### Solution 1 - 
- Use 2 pointers, one for each array starting on the right side
- Only need to process until index2 is 0, nums1 is already sorted so if all the elements of num2 are placed correctly then its already sorted
- Start comparing elements from the end
  - if `nums1[index1]` > `nums2[index2]` then `nums1[index1]` needs to be set on the value

```csharp
public void Merge(int[] nums1, int m, int[] nums2, int n)
{
	int index1 = m - 1;
	int index2 = n - 1;
	int indexResult = m + n - 1;

	// only need to process the elements of nums2, nums1 is already sorted
	while (index2 >= 0)
	{
		if (index1 >= 0 && nums1[index1] > nums2[index2])
		{
			nums1[indexResult] = nums1[index1];
			indexResult--;
			index1--;
		}
		else
		{
			nums1[indexResult] = nums2[index2];
			indexResult--;
			index2--;
		}
	}
}
```

# 121. Best Time to Buy and Sell Stock
## Difficulty: Easy
## Topics: Dynamic Programming, Two pointers
### Method 1 - Two Pointers
- use two pointers to represent the buy and sell indeces
- `left` pointer is the buy index and `right` pointer is the sell index 
- in every iteration check the prices
  - if `prices[left]` is smaller than `prices[right]` it means that there is a profit by selling -> check if the profit is bigger than the global profit
  - if `prices[right]` is smaller than `prices[left]` it means that a better buying day has been found, update `left` with the new buy index
  - at the end increase `right`
  
```csharp
public int MaxProfit(int[] prices)
{
	int left = 0;
	int right = 1;
	int maxProfit = 0;

	while (right < prices.Length)
	{
		// if the trade is profitable check if the profit is bigger than the current profit
		if (prices[left] < prices[right])
		{
			int profit = prices[right] - prices[left];
			if (profit > maxProfit)
			{
				maxProfit = profit;
			}
		}
		// if the trade isn't profitable (right value is smaller than left value), then update left value to the current smallest value and continue searching
		else
		{
			left = right;
		}

		// go to the next value
		right++;
	}

	return maxProfit;
}
```

# 125. Valid Palindrome
## Difficulty: Easy
## Topics: Two Pointers
### Method 1 - Two Pointers
- Use to pointers to store the current chars
- Left pointer starts at index 0 and Right pointers starts at the last char
- In each iteration move left pointer to the right and right pointer to the left, then check if the chars are the same

```csharp
public bool IsPalindrome(string s)
{
	if (String.IsNullOrEmpty(s)) return true;

	int leftIndex = 0;
	int rightIndex = s.Length - 1;

	while (leftIndex < rightIndex)
	{
		// increment left index until a letter is found
		while (leftIndex < rightIndex && !Char.IsLetterOrDigit(s[leftIndex])) leftIndex++;

		// increment right index until a letter is found
		while (leftIndex < rightIndex && !Char.IsLetterOrDigit(s[rightIndex])) rightIndex--;
		
		// if the chars are different then return false
		if (char.ToLower(s[leftIndex]) != char.ToLower(s[rightIndex])) return false;
		
		// move the pointers to their next positions
		leftIndex++;
		rightIndex--;
	}

	return true;
}
```
<br/>

### 
- The input can be cleaned before processing for simpler logic, but worse performance
```csharp
public bool IsPalindrome(string s)
{
	if (String.IsNullOrEmpty(s)) return true;

	var chars = s.ToLower().Where(char.IsLetterOrDigit).ToArray();

	int leftIndex = 0;
	int rightIndex = chars.Length - 1;

	while (leftIndex < rightIndex)
	{
		// if the chars are different then return false
		if (char.ToLower(chars[leftIndex]) != char.ToLower(chars[rightIndex])) return false;

		// move the pointers to their next positions
		leftIndex++;
		rightIndex--;
	}

	return true;
}
```
<br/>

###
```csharp
public bool IsPalindrome(string s)
{
	string cleaned = new string(s.ToLower().Where(char.IsLetterOrDigit).ToArray());
	return cleaned.SequenceEqual(cleaned.Reverse());
}
```

# 128. Longest Consecutive Sequence
## Difficulty: Medium
## Topics: Hash Map, Union find

### Solution 1 - Sorting
#### Beats: 33%
```csharp
public int LongestConsecutive(int[] nums)
{
	if (nums.Length == 0) return 0;

	Array.Sort(nums);
	int maxLength = 1;
	int currentLength = 1;

	for (int i = 1; i < nums.Length; i++)
	{
		// Skip duplicates
		if (nums[i] == nums[i - 1])
			continue;

		// If current element is consecutive to previous
		if (nums[i] == nums[i - 1] + 1)
		{
			currentLength++;
		}
		else
		{
			// Reset current streak
			currentLength = 1;
		}

		maxLength = Math.Max(maxLength, currentLength);
	}

	return maxLength;
}
```

### Solution 2 - Hashset
#### Beats: 74%
- Put all numbers in a hashset to remove duplicates and enable O(1) lookups
- Only start counting sequences from numbers that have no predecessors (num-1 not in set)
- For each valid starting number, count consecutive elements by checking `num+1`, `num+2`, ... .

```csharp
public int LongestConsecutive(int[] nums)
{
	if (nums.Length == 0)
	{
		return 0;
	}

	HashSet<int> hashSet = new HashSet<int>(nums);

	int maxLength = 1;
	foreach (int num in hashSet)
	{ 
		// Check if current number is the start of a new sequence
		if (!hashSet.Contains(num - 1))
		{
			int length = 1;
			while (hashSet.Contains(num + length))
			{
				length++;
			}

			maxLength = Math.Max(length, maxLength);
		}
	}

	return maxLength;
}
```

# 150. Evaluate Reverse Polish Notation
## Difficulty: Medium
## Topics: Stack

### Solution 1 
- Process each token,
  - if it's a number then push it to the stack
  - if it's an operator then pop 2 numbers from the stack, do that operation, and push the result to the stack

```csharp
public int EvalRPN(string[] tokens)
{
	Stack<int> numbers = new();
	int a, b;
	
	foreach (var token in tokens)
	{
		switch (token)
		{
			case "+":
				b = numbers.Pop();
				a = numbers.Pop();
				numbers.Push(a + b);
				break;
			case "-":
				b = numbers.Pop();
				a = numbers.Pop();
				numbers.Push(a - b);
				break;
			case "*":
				b = numbers.Pop();
				a = numbers.Pop();
				numbers.Push(a * b);
				break;
			case "/":
				b = numbers.Pop();
				a = numbers.Pop();
				numbers.Push(a / b);
				break;
			default:
				if (int.TryParse(token, out int number))
				{
					numbers.Push(number);
				}
				break;
		}
	}

	return numbers.Pop();
}
```

### Solution 2 - Dictionary with funcs for operators
```csharp
public int EvalRPN(string[] tokens)
{
	Stack<int> numbers = new();
	var operators = new Dictionary<string, Func<int, int, int>>
	{
		{ "+", (a, b) => a + b },
		{ "-", (a, b) => a - b },
		{ "*", (a, b) => a * b },
		{ "/", (a, b) => a / b }
	};

	foreach (var token in tokens)
	{
		if (operators.TryGetValue(token, out var operation))
		{
			int b = numbers.Pop();
			int a = numbers.Pop();
			numbers.Push(operation(a, b));
		}
		else if (int.TryParse(token, out int number))
		{
			numbers.Push(number);
		}
	}
	
	return numbers.Pop();
}
```

# 151. Reverse Words in a String
## Difficulty: Medium XD
## Topics: String

### Solution 1 - 
- Trim and split the array
- Start looking at words from the end and append them using a stringBuilder

```csharp
using System.Text;

public class Solution
{
    public string ReverseWords(string s)
    {
        s = s.Trim();
        var words = s.Split(' ', StringSplitOptions.RemoveEmptyEntries);
        var stringBuilder = new StringBuilder();

        for (int i = words.Length - 1; i >= 0; i--)
        {
            stringBuilder.Append(words[i]);
            if (i > 0)
            {
                stringBuilder.Append(' ');
            }
        }

        return stringBuilder.ToString();
    }
}
```

### Solution 2 - Sort and reverse
```csharp
public class Solution {
    public string ReverseWords(string s) {
        s = s.Trim();

        string[] words = s.Split(new char[] { ' ' }, StringSplitOptions.RemoveEmptyEntries);

        Array.Reverse(words);

        return string.Join(" ", words);
    }
}
```

# 155. Min Stack
## Difficulty: Medium
## Topics: Stack, Design

### Solution 1 - 2 Stacks
- Use 2 stacks, one that stores values normally and one that always store the min value at every moment
- When pushing - push value normally to main stack, for minStack push the min between `value` and `currentMinimum` 
  - Minstack will contain the min value for every value inserted in the stack

```csharp
public class MinStack
{
	Stack<int> stack;
	Stack<int> minStack;
	int minValue;

	public MinStack()
	{
		stack = new Stack<int>();
		minStack = new Stack<int>();
	}

	public void Push(int val)
	{
		if(stack.Count == 0)
		{
			minValue = val;
		}
		
		stack.Push(val);
		
		minValue = Math.Min(minValue, val);
		minStack.Push(minValue);
	}

	public void Pop()
	{
		stack.Pop();
		minStack.Pop();
		if (minStack.Count > 0)
		{
			minValue = minStack.Peek();
		}
	}

	public int Top()
	{
		return stack.Peek();
	}

	public int GetMin()
	{
		return minValue;
	}
}
```

### Solution 2 - Tuple with value and min
```csharp
public class MinStack
{
	private Stack<(int Value, int Min)> _stack;

	public MinStack()
	{
		_stack = new Stack<(int Value, int Min)>();
	}

	public void Push(int val)
	{
		// if stack count is 0 push the first element without extra logic
		if (_stack.Count == 0)
		{
			_stack.Push((val, val));
			return;
		}

		// when pushing new element check the current min value
		var prevMin = _stack.Peek().Min;
		_stack.Push((val, val < prevMin ? val : prevMin));
	}

	public void Pop() => _stack.Pop();
	public int Top() => _stack.Peek().Value;
	public int GetMin() => _stack.Peek().Min;
}
```

# 167. Two Sum II - Input Array is Sorted
## Difficulty: Medium
## Topics: Two Pointers, Binary Search

### Solution 1 - Two pointers
- There is always one solution for each array
- Because the array is sorted left side contains lower numbers and right side higher numbers
- Use 2 pointers left and right and compare their sum to the target:
  - If sum > target then the sum need to be lower, decrement right
  - If sum < target then the sum need to be higher, increment left

```csharp
public int[] TwoSum(int[] numbers, int target)
{
	int left = 0;
	int right = numbers.Length - 1;

	while (left < right)
	{
		int sum = numbers[left] + numbers[right];
		if (sum == target) break;
		if (sum < target) left++;
		if (sum > target) right--;
	}

	return new int[] { left + 1, right + 1 };
}
```

### Solution 2 - (Worse) Use dictionary for complement like Two Sum I
```csharp
public int[] TwoSum(int[] numbers, int target)
{
	Dictionary<int, int> dict = new Dictionary<int, int>();

	for (int i = 0; i < numbers.Length; i++)
	{
		var complement = target - numbers[i];
		if (dict.ContainsKey(complement))
		{
			return [dict[complement] + 1, i + 1];
		}

		dict[numbers[i]] = i;
	}

	return numbers;
}
```

# 169. Majority Element
## Difficulty: Easy
## Topics: Hash table, Heap, Sorting, Counting, Divide and conquer

### Solution 1 - Moore's Voting Algorithm
- Initialize two variables: `count` and `candidate`. Set `count` to 0 and `candidate` to an arbitrary value
- Iterate through the array nums:
  - a. If `count` is 0, assign the current element as the new `candidate` and increment `count` by 1
  - b. If the `current` element is the same as the `candidate`, increment `count` by 1
  - c. If the `current` element is different from the `candidate`, decrement `count` by 1
- After the iteration, the `candidate` variable will hold the majority element

```csharp
public int MajorityElement(int[] nums)
{
	int count = 0;
	int candidate = 0;

	foreach (int num in nums)
	{
		if (count == 0)
		{
			candidate = num;
		}

		if (num == candidate)
		{
			count++;
		}
		else
		{
			count--;
		}
	}

	return candidate;
}
```

### Solution 2 - Frequency Map
```csharp
public int MajorityElement(int[] nums)
{
	int majoritySize = nums.Length / 2;

	var frequencyMap = new Dictionary<int, int>();
	foreach (var num in nums)
	{
		if (!frequencyMap.ContainsKey(num))
		{
			frequencyMap[num] = 0;
		}

		frequencyMap[num]++;

		if (frequencyMap[num] > majoritySize)
		{
			return num;
		}
	}

	// there's always a majority element
	return -1;
}
```


### Solution 3 - Sort array and get element at n/2
```csharp
public int MajorityElement(int[] nums)
{
	Array.Sort(nums);
	int majority = nums.Length / 2;
	return nums[majority];
}
```

# 200. Number of Islands
## Difficulty: Medium
## Topics: DFS, BFS
### Solution
- Use a for loop to iterate over all the cells of the matrix:
  - If the value of the cell is 0 then an island hasn't been found, continue iterating
  - If the value of the cell is 1 then an island has been found:
    - Increment the `number of islands`
	- Process all the adjacent cells that make up the island and set them to `0` so that they cannot be processed again
	- A cell is connected to land only in the directions `UP`, `DOWN`, `LEFT` and `RIGHT`

### Solution 1 - Iterative DFS with stacks
#### Beats 37.05%
```csharp
public int NumIslands(char[][] grid)
{
	int islands = 0;
	for (int row = 0; row < grid.Length; row++)
	{
		for (int col = 0; col < grid[row].Length; col++)
		{
			// If the cell is an island then process all the cells that make up that island
			if (grid[row][col] == '1')
			{
				DFSStack(grid, row, col);
				islands++;
			}
		}
	}

	return islands;
}

private void DFSStack(char[][] grid, int i, int j)
{
	// Define a stack to hold the cells to be visited
	Stack<(int row, int col)> stack = new();
	stack.Push((row: i, col: j));

	// Loop until the stack is empty
	while (stack.Count > 0)
	{
		(int row, int col) = stack.Pop();

		// Check if the current cell is out of bounds or already visited
		if (row < 0 || row >= grid.Length || col < 0 || col >= grid[0].Length || grid[row][col] == '0')
		{
			continue;
		}

		// Mark the current cell as visited
		grid[row][col] = '0';

		// Push all four neighbors onto the stack using tuples
		stack.Push((row - 1, col)); // Up
		stack.Push((row + 1, col)); // Down
		stack.Push((row, col - 1)); // Left
		stack.Push((row, col + 1)); // Right
	}
}
```

### Solution 2 - DFS Recursive
#### Beats 80.82%
```csharp
public int NumIslands(char[][] grid)
{
	int numIslands = 0;
	for (int row = 0; row < grid.Length; row++)
	{
		for (int col = 0; col < grid[row].Length; col++)
		{
			if (grid[row][col] == '1')
			{
				ProcessIslands(grid, row, col);
				numIslands++;
			}
		}
	}

	return numIslands;
}

private void ProcessIslands(char[][] grid, int row, int col)
{
	if (row < 0 || row >= grid.Length || col < 0 || col >= grid[0].Length || grid[row][col] == '0')
	{
		return;
	}

	grid[row][col] = '0';

	ProcessIslands(grid, row - 1, col);
	ProcessIslands(grid, row + 1, col);
	ProcessIslands(grid, row, col - 1);
	ProcessIslands(grid, row, col + 1);
}
```

# 205. Isomorphic String
## Difficulty: Easy
## Topics: Hash Table

### Solution 1 - 2 dictionaries
```csharp
public class Solution {
	public bool IsIsomorphic(string s, string t)
	{
		var sToT = new Dictionary<char, char>();
		var tToS = new Dictionary<char, char>();

		for (int i = 0; i < s.Length; i++)
		{
			char sChar = s[i];
			char tChar = t[i];

			// check if s was mapped to a t
			if (sToT.ContainsKey(sChar))
			{
				if (sToT[sChar] != tChar) return false;
			}
			// check if t was mapped to an s
			else if (tToS.ContainsKey(tChar))
			{
				if (tToS[tChar] != sChar) return false;
			}
			else
			{
				sToT[sChar] = tChar;
				tToS[tChar] = sChar;
			}
		}

		return true;
	}
}
```

### Solution 1' - 1 dictionary
- Use a dictionary to store the mappings from the letters of s to the letters of t
- Loop over all chars of the words and check if there's a mapping from `sChar` to `tChar`
  - if a mapping exists from `sChar` to `tChar` check if `tChar` is equal to the existing mapping
  - if there is no mapping from `sChar` to `tChar` check if `tChar` was already used in another mapping

```csharp
public bool IsIsomorphic(string s, string t)
{
	var sToT = new Dictionary<char, char>();

	for (int i = 0; i < t.Length; i++)
	{
		char sChar = s[i];
		char tChar = t[i];

		// if dict doesn't contain a mapping for the original char
		if (!sToT.TryGetValue(sChar, out var existingMapping))
		{
			// check if second word char is used in multiple places
			// if the mapping was already used for another char return false
			// ex: "badc" -> "baba", dict contains b->b, a->a, and now d->b which is wrong
			if (sToT.ContainsValue(tChar)) return false;

			// put the mapping in the dict
			sToT[sChar] = tChar;
			continue;
		}

		// check if first word char is used in multiple places
		// if the mapping that needs to be done for the char of s is different from the existing mapping -> return false
		// ex: "abb" -> "abc", b is used for both b->b and b->c
		if (tChar != existingMapping) return false;
	}

	return true;
}
```

### Solution 2 - Char array for frequencies
```csharp
public bool IsIsomorphic(string s, string t)
{
	int[] map1 = new int[128]; // Stores frequency of s
	int[] map2 = new int[128]; // Stores frequency of t

	for (int i = 0; i < s.Length; i++)
	{
		char s_ch = s[i];
		char t_ch = t[i];

		// if there is no mapping from s->t or t->s
		if (map1[s_ch] == 0 && map2[t_ch] == 0)
		{
			map1[s_ch] = t_ch;
			map2[t_ch] = s_ch;
		}
		else if (map1[s_ch] != t_ch || map2[t_ch] != s_ch)
		{
			return false;
		}
	}

	return true;
}
```

# 215. Kth Largest Element in an Array
## Difficulty: Medium
## Topics: Divide and Conquer, Heap, Quickselect
### Solution - Heap
- Use a minheap of size k to process items
- If heap size size is > k then dequeue
- Return the root of the heap as the k-th element

```csharp
public int FindKthLargest(int[] nums, int k)
{
	PriorityQueue<int, int> minHeap = new PriorityQueue<int, int>();
	foreach (var num in nums)
	{
		minHeap.Enqueue(num, num);

		if (minHeap.Count > k)
		{
			minHeap.Dequeue();
		}
	}

	return minHeap.Dequeue();
}
```

### Solution - Sort the array and the the k-th element from the end
- Is faster than heap method, maybe because k ~= n in the tests?
```csharp
public int FindKthLargest(int[] nums, int k)
{
	Array.Sort(nums);
	return nums[nums.Length - k];
}
```

# 217. Contains Duplicate
## Difficulty: Easy
## Topics: Hash table, Sorting

### Solution 1 - Check if hashset contains
```csharp
public bool ContainsDuplicate(int[] nums) {
	HashSet<int> set = new HashSet<int>();
	foreach (var num in nums)
	{
		if (set.Contains(num))
		{
			return true;
		}
		set.Add(num);
	}

	return false;
}
```

### Solution - Sort array and check if next element is duplicate
```csharp
public bool ContainsDuplicate(int[] nums)
{
	Array.Sort(nums);
	for (int i = 0; i < nums.Length - 1; i++)
	{
		if (nums[i] == nums[i + 1])
		{
			return true;
		}
	}

	return false;
}
```

# 238. Product of array except self
## Difficulty: Medium
## Topics: Prefix sum

### Solution 1 - Brute force
#### Beats: Time Limit Exceeded :\
- 2 for loops, outer loop over all the elements, inner loop that calculates the product for all the elements except the current one 
```csharp
public int[] ProductExceptSelf(int[] nums)
{
	var result = new int[nums.Length];
	for (int i = 0; i < nums.Length; i++)
	{
		int temp = 1;
		for (int j = 0; j < nums.Length; j++)
		{
			if (i != j)
			{
				temp *= nums[j];
			}
		}

		result[i] = temp;
	}

	return result;
}
```

### Solution 2 - Suffix and prefix
#### Beats: 30.57%
- Use 2 arrays for each element
  - prefix array contains the product of all the elements before `i`
  - postfix array contains the product of all the elements after `i`
  - product of the array except `element[i]` is `prefix[i] * postfix[i]`

```csharp
public int[] ProductExceptSelf(int[] nums)
{
    int n = nums.Length;
    var result = new int[n];
    var prefix = new int[n];
    var postfix = new int[n];

    // Compute prefix products
    prefix[0] = 1; // No elements to the left of first element
    for (int i = 1; i < n; i++)
    {
        prefix[i] = prefix[i - 1] * nums[i - 1];
    }

    // Compute postfix products
    postfix[n - 1] = 1; // No elements to the right of last element
    for (int i = n - 2; i >= 0; i--)
    {
        postfix[i] = postfix[i + 1] * nums[i + 1];
    }

    for (int i = 0; i < n; i++)
    {
        result[i] = prefix[i] * postfix[i];
    }

    return result;
}
```

### Solution 3 - Optimized Solution 2, compute prefix on output array
#### Beats: 66%
- Use the result array as the prefix values
- Calculate result at the same time with the postfix


```csharp
public int[] ProductExceptSelf(int[] nums)
{
	int n = nums.Length;
	var result = new int[n];

	// Calculate prefix of all elements to the left of each element
	result[0] = 1; // No elements to the left of the first element
	for (int i = 1; i < n; i++)
	{
		result[i] = result[i - 1] * nums[i - 1];
	}

	// Calculate products of all elements to the right and multiply with the postfix
	int postfix = 1;
	for (int i = n - 1; i >= 0; i--)
	{
		result[i] *= postfix;
		postfix *= nums[i];
	}

	return result;
}
```

# 242. Valid Anagram
## Difficulty: Easy
## Topics: Hash table, Sorting

### Solution 1 - Sort strings and check if they are equal
#### Beats: 30%
```csharp
public bool IsAnagram(string s, string t)
{
	if (s.Length != t.Length) return false;

	var sCharArray = s.ToCharArray();
	var tCharArray = t.ToCharArray();
	
	Array.Sort(sCharArray);
	Array.Sort(tCharArray);
	
	return sCharArray.SequenceEqual(tCharArray);
}
```

### Solution 2 - Frequency map
#### Beats: 80%
- Use a dictionary for the frequency map of the first string
- For the second
  - if char isn't found in freqMap => return false
  - decrement the count of that char and if it's lower than 0 => return false

```csharp
public bool IsAnagram(string s, string t)
{
	if (s.Length != t.Length) return false;
	
	Dictionary<char, int> freqMap = new();

	foreach (var c in s)
	{
		if (!freqMap.ContainsKey(c))
		{
			freqMap[c] = 0;
		}
		freqMap[c]++;
	}

	foreach (var c in t)
	{
		if (!freqMap.ContainsKey(c))
		{
			return false;
		}
		
		freqMap[c]--;

		if (freqMap[c] < 0)
		{
			return false;
		}
	}

	return true;
}
```

# 271. Encode and Decode Strings
## Difficulty: Medium
## Topics: Two Pointers, Sliding Window

### Solution 
- Encode the string by putting the word length and a delimiter before each word
- Decoding is done using 2 pointers
  - i is the start of the encoded word, at the first number that makes up the length
  - j is moved until # to find the word length, use substring and the calculated length to get the word
  - move i to the start of the next word length `j + 1 + wordLength`

```csharp
public string Encode(IList<string> strs)
{
	StringBuilder result = new StringBuilder();
	foreach (var str in strs)
	{
		result.Append(str.Length + "#" + str);
	}

	return result.ToString();
}

public List<string> Decode(string s)
{
	List<string> result = new List<string>();
	int i = 0;
	while (i < s.Length)
	{
		// find all numbers that make up the length of the word
		int j = i;
		while (j < s.Length && s[j] != '#')
		{
			j++;
		}

		// i is the start of the number, j is the end, use the length j-i to extract the length of the word
		int wordLength = Int32.Parse(s.Substring(i, j - i));

		// j is on the '#', j+1 is the first letter of the word
		string word = s.Substring(j + 1, wordLength);
		result.Add(word);

		// continue looking for new words after the last word that was found
		i = j + 1 + wordLength;
	}

	return result;
}
```

# 290. Word Pattern
## Difficulty: Easy
## Topics: Hash table
## Similar to: #205

### Solution 1 - 1 Dictionary
```csharp
public class Solution
{
    public bool WordPattern(string pattern, string s)
    {
        // pattern to word mapping dictionary
        var dictionary = new Dictionary<char, string>();
        var words = s.Split(' ');

        if (words.Length != pattern.Length) return false;

        for (int i = 0; i < pattern.Length; i++)
        {
            var currentWord = words[i];
            var currentPattern = pattern[i];

            if (!dictionary.TryGetValue(currentPattern, out var existingWordMapping))
            {
                // if mapping is different from existing mapping
                if (currentWord != existingWordMapping) return false;
                continue;
            }

            // if current word was already used for another pattern char
            if (dictionary.ContainsValue(currentWord)) return false;

            dictionary[currentPattern] = currentWord;
        }

        return true;
    }
}
```

### Solution 2 - 2 Dictionaries

```csharp
public class Solution
{
    public bool WordPattern(string pattern, string s)
    {
        var wordToPattern = new Dictionary<string, char>();
        var patternToWord = new Dictionary<char, string>();

        string[] words = s.Split(' ');

        if (words.Length != pattern.Length) return false;

        for (int i = 0; i < words.Length; i++)
        {
            var word = words[i];
            var patternChar = pattern[i];

            if (wordToPattern.ContainsKey(word))
            {
                if (wordToPattern[word] != patternChar) return false;
            }

            if (patternToWord.ContainsKey(patternChar))
            {
                if (patternToWord[patternChar] != word) return false;
            }

            if (!wordToPattern.ContainsKey(word) && !patternToWord.ContainsKey(patternChar))
            {
                wordToPattern[word] = patternChar;
                patternToWord[patternChar] = word;
            }
        }

        return true;
    }
}
```

# 347. Top K Frequent Elements
## Dificulty: Medium
## Topics: Hash Map, Heap

### Solution 1- Use a dictionary to store and sort frequencies
#### Beats: 38%
```csharp
public int[] TopKFrequent(int[] nums, int k)
{
	// Step 1: Create the frequency map
	var freqMap = new Dictionary<int, int>();
	foreach (var num in nums)
	{
		// If value doesn't exist in dictionary init it with 0
		freqMap.TryAdd(num, 0);

		// Increment the frequency
		freqMap[num]++;
	}

	// Step 2: Arrange the elements based on their frequency
	Dictionary<int, List<int>> buckets = new Dictionary<int, List<int>>();
	foreach (var num in freqMap.Keys)
	{
		int freq = freqMap[num];

		// If the frequency key doesn't exist in the dictionary, add a new list
		if (!buckets.ContainsKey(freq))
		{
			buckets[freq] = new List<int>();
		}

		// Add the number to the list for the corresponding frequency
		buckets[freq].Add(num);
	}

	var result = new List<int>();

	// Sort frequencies in descending order
	var sortedFrequencies = buckets.Keys.OrderByDescending(f => f).ToList();
	foreach (var freq in sortedFrequencies) {
		// Add all numbers with this frequency to the result
		result.AddRange(buckets[freq]);

		// Stop if we have enough elements
		if (result.Count >= k) {
			break;
		}
	}

	return result.Take(k).ToArray();
}
```
###
#### Beats: 42%
- Slightly faster due to sorting directly without the second dictionary
```csharp
public int[] TopKFrequent(int[] nums, int k)
{
    // Step 1: Create the frequency map
    var freqMap = new Dictionary<int, int>();
    foreach (var num in nums)
    {
        if (!freqMap.ContainsKey(num))
            freqMap[num] = 0;
        freqMap[num]++;
    }
    
    // Sort elements by frequency directly and take top k
    return freqMap.OrderByDescending(pair => pair.Value)
                  .Take(k)
                  .Select(pair => pair.Key)
                  .ToArray();
}
```


### Solution 2 - Use a minheap
#### Beats: 64%
- A dictionary is used to store the frequencies of the values
- A PriorityQueue / MinHeap is used to keep track of the top k most frequent elements
- For each key (number) in the frequency map:
	- The number is enqueued into the heap with its frequency as the priority
	- If the heap size exceeds k, the element with the smallest frequency is removed

```csharp
public int[] TopKFrequent(int[] nums, int k)
{
	// Step 1: Create the frequency map
	var freqMap = new Dictionary<int, int>();
	foreach (var num in nums)
	{
		// If value doesn't exist in dictionary init it with 0
		freqMap.TryAdd(num, 0);

		// Increment the frequency
		freqMap[num]++;
	}

	// Step 2: Use a minheap to keep the top k elements
	var minHeap = new PriorityQueue<int, int>();
	foreach (var key in freqMap.Keys)
	{
		// Enqueue the number with its frequency as the priority
		minHeap.Enqueue(key, freqMap[key]);

		// If the heap size exceeds k, remove the element with the smallest frequency
		if (minHeap.Count > k)
		{
			minHeap.Dequeue();
		}
	}

	var result = new List<int>();
	while (minHeap.Count > 0)
	{
		result.Add(minHeap.Dequeue());
	}

	return result.ToArray();
}
```

### Solution ? - Use Linq to group the numbers, sort desc, and take k elements
```csharp
public int[] TopKFrequent(int[] nums, int k)
{
	return nums
		.GroupBy(num => num)
		.OrderByDescending(num => num.Count())
		.Take(k)
		.Select(num => num.Key)
		.ToArray();
}
```

# 383. Ransom Note
## Difficulty: Easy
## Topics: Hash table, Counting

### Solution 1 - Char couting array
```csharp
public bool CanConstruct(string ransomNote, string magazine)
{
	if (ransomNote.Length > magazine.Length) return false;

	int[] charCounter = new int[26];

	foreach (var c in magazine)
	{
		charCounter[c - 'a']++;
	}

	foreach (var c in ransomNote)
	{
		if (charCounter[c - 'a'] == 0) return false;
		charCounter[c - 'a']--;
	}

	return true;
}
```

### Solution 2 - Dictionary for frequencies
```csharp
public bool CanConstruct(string ransomNote, string magazine)
{
	if(ransomNote.Length > magazine.Length) return false;

	// frequency for ransom note characters
	var ransomDict = new Dictionary<char, int>();
	foreach (var c in ransomNote)
	{
		if (!ransomDict.ContainsKey(c))
		{
			ransomDict[c] = 0;
		}
		ransomDict[c]++;
	}
	
	// frequency for magazine characters
	var magazineDict = new Dictionary<char, int>();
	foreach (var c in magazine)
	{
		magazineDict.TryAdd(c, 0);
		magazineDict[c]++;
	}

	foreach (var ransomPair in ransomDict)
	{
		// if magazine doesn't contain the ransom note key -> return false
		if (!magazineDict.TryGetValue(ransomPair.Key, out var magazineFrequency))
		{
			return false;
		}
		
		// if magazine char frequency is less than what is required for the ransom note -> return false
		if (magazineFrequency < ransomPair.Value)
		{
			return false;
		}
	}

	return true;
}
```

### Solution 2 - Counting array for chars

# 392. Is Subsequence
## Difficulty: Easy
## Topics: Two Pointers, Dynamic Programming

### Solution 1 - Two Pointers
- Use 2 pointers both starting at 0, one for `s` and one for `t`
- In each iteration
  - check if `s[sIndex] == t[tIndex]` and increment `sIndex` to point on the next char if true
  - increment `tIndex`
- If there are missing chars in s, ex `acx` - `abcd`, `sIndex` will be less than `s.Length`
- 2 pointer method checks if chars appear in the same order `abc` - `acb` -> `sIndex` will be 1 -> `false` 

```csharp
public class Solution
{
    public bool IsSubsequence(string s, string t)
    {
        int sIndex = 0;
        int tIndex = 0;
        
        while (sIndex < s.Length && tIndex < t.Length)
        {
            if (s[sIndex] == t[tIndex])
            {
                sIndex++;
            }

            tIndex++;
        }

        return sIndex == s.Length;
    }
}
```

# 424. Longest Repeating Character Replacement
## Difficulty: Medium
## Topics: Sliding Window, Hash table

### Solution 1 - 
- The solution is the size of the biggest valid window
- A window is valid if the number of characters that arent the majority can be replaced using k chars, so the condition is `window.Legth - countOfMajorityElement <= k`
- If a window respects the condition that it can be counted for the max window length

- To solve this use a sliding window, left & right both start at 0
- In each iteration
  - Right is incremented
  - The current window is checked for validity
    - If the current window is valid then try to update max
	- If the current window is invalid then left gets incremented until the window becomes valid

``` csharp
public class Solution
{
    public int CharacterReplacement(string s, int k)
    {
        int maxValue = 0;
        
        int left = 0;
        int right = 0;
        var freqMap = new Dictionary<char, int>();
        // Track the maximum frequency in the current window
        int maxElementCount = 0; 

        while (right < s.Length)
        {
            char current = s[right];

            // If current character doesn't exist in the hashmap init it with 0
            freqMap.TryAdd(current, 0);
            
            // Update the frequency of the current character
            freqMap[current]++;

            // Update the maximum frequency in the current window
            maxElementCount = Math.Max(maxElementCount, freqMap[current]);

            // Calculate the length of the current window
            int windowLength = right - left + 1;

            // If the window is not valid, move the left pointer to the right
            if (windowLength - maxElementCount > k)
            {
                freqMap[s[left]]--;
                left++;
            }
            else
            {
                // Update the maximum length of the valid window
                maxValue = Math.Max(maxValue, windowLength);
            }

            right++;
        }
        
        return maxValue;
    }
}
```


# 451. Sort Characters By Frequency
## Difficulty: Medium
## Topics: Hash Map, Heap, Bucket Sort

### Solution 1 - Heap
#### Beats: 86%
- Use a dictionary to create the frequency map
- Use a maxHeap to enqueue the elements
- Pop each element to get the sorted chars in decreasing order of their frequencies

```csharp
public string FrequencySort(string s)
{
	Dictionary<char, int> frequencyMap = new();

	// create the frequency map with the char and its frequency
	foreach (var c in s)
	{
		if (!frequencyMap.ContainsKey(c))
		{
			frequencyMap[c] = 0;
		}

		frequencyMap[c]++;
	}

	// create the maxHeap, top contains the element with the highest frequency
	var maxHeapComparer = Comparer<int>.Create((x, y) => y.CompareTo(x));
	PriorityQueue<char, int> maxHeap = new(maxHeapComparer);

	//OR maxHeap.EnqueueRange(frequencyMap.Select(kvp => (kvp.Key, kvp.Value)));
	foreach (var kvp in frequencyMap)
	{
	    maxHeap.Enqueue(kvp.Key, kvp.Value);
	}

	// deque each element and create the string using the frequency / priority
	StringBuilder sb = new();
	while (maxHeap.TryDequeue(out char c, out int frequency))
	{
		for (int i = 0; i < frequency; i++)
		{
			sb.Append(c);
		}
	}

	return sb.ToString();
}
```

# 496. Next Greater Element I
## Difficulty: Easy
## Topics: Monotonic Stack, Hash Table

### Solution
- Use a monotonic stack to store the nums with no higher element
- When a higher element is found pop the nums from the stack until the stack becomes monotonic again (until the stack is empty or the current element is <= than the element in the stack)
- For each popped element put them in a dictionary with the popped value as the key and the num as the value [element, nextHighest]
- At the end loop over all values in num1 and seach the dictionary, if the element is contained then it has a nextHighest element, otherwise it doesn't

```csharp
public class Solution
{
    public int[] NextGreaterElement(int[] nums1, int[] nums2)
    {
        if (nums1.Length == 0) return [];

        var decreasingStack = new Stack<int>();
        var nextHighestDict = new Dictionary<int, int>();

        foreach (var num in nums2)
        {
            // If a bigger element than the one on top of the stack is found then keep popping the elements
            // and add them to a dictionary with [element, nextHighest]
            while (decreasingStack.Count > 0 && num > decreasingStack.Peek())
            {
                nextHighestDict.Add(decreasingStack.Pop(), num);
            }

            decreasingStack.Push(num);
        }

        // Construct the result array by looking for the array values in the dictionary
        int[] res = new int[nums1.Length];
        for (int i = 0; i < nums1.Length; i++)
        {
            // If dictionary doesn't contain the element then it has no element higher than it
            res[i] = nextHighestDict.ContainsKey(nums1[i])? nextHighestDict[nums1[i]] : -1;
        }

        return res;
    }
}
```

# 692. Top K Frequent Words
## Difficulty: Medium
## Topics: Hash map, Heap, Bucket sort, Sorting

### Solution 1 - Max heap with custom comparer
#### Beats: 85%
```csharp
public IList<string> TopKFrequent(string[] words, int k)
{
	// create the frequency map for the words
	Dictionary<string, int> frequencyMap = new();
	foreach (var word in words)
	{
		frequencyMap.TryAdd(word, 0);
		frequencyMap[word]++;
	}

	// use a minheap to keep just the k top words with the highest frequencies
	var maxHeapComparer = Comparer<(int Priority, string Value)>.Create((x, y) =>
	{
		// First, compare by priority in descending order
		int priorityComparison = y.Priority.CompareTo(x.Priority);
		if (priorityComparison != 0)
		{
			return priorityComparison;
		}

		// If priorities are the same, compare by string in ascending order
		return string.Compare(x.Value, y.Value, StringComparison.Ordinal);
	});

	PriorityQueue<string, (int Priority, string Value)> maxHeap = new(maxHeapComparer);
	foreach (var kvp in frequencyMap)
	{
		maxHeap.Enqueue(kvp.Key, (kvp.Value, kvp.Key));
	}

	int currentK = 0;
	List<string> result = new();
	while (currentK < k)
	{
		result.Add(maxHeap.Dequeue());
		currentK++;
	}

	return result;
}
```

# 704. Binary Search 
## Difficulty: Easy
## Topics: Binary Search
#### Solution
- Use 2 indeces, left and right to create the lookup window
- in each iteration look at the middle of the array and compare the value to the target
  - if the value is bigger than the target then continue looking in the left side of the array
  - if the value is smaller than the target then continue looking in the right side of the array

```csharp
public int Search(int[] nums, int target)
{
	if (nums.Length == 0) return -1;

	int left = 0;
	int right = nums.Length - 1;

	while (left <= right)
	{
		// calcualate middle index
		int middle = (left + right) / 2;

		// check if target has been found
		if (nums[middle] == target)
		{
			return middle;
		}

		// if target is smaller than middle value keep searching in the left side of the array
		if (nums[middle] > target)
		{
			right = middle - 1;
		}
		// if targer is bigger than middle value keep searching in the right side of the array
		else
		{
			left = middle + 1;
		}
	}

	return -1;
}
```



# 739. Daily Temperatures
## Difficulty: Medium
## Topics: Monotonoic Stack

### Solution
- Use a monotonic stack to store the indeces of the temperatures
- If a higher temperature found then while there are smaller elements on the stack pop them and calculate the index difference

```csharp
public class Solution
{
    public int[] DailyTemperatures(int[] temperatures)
    {
        Stack<int> monotonicDecreasing = new();
        var result = new int[temperatures.Length];

        for (int i = 0; i < temperatures.Length; i++)
        {
            while (monotonicDecreasing.Count > 0 && temperatures[i] > temperatures[monotonicDecreasing.Peek()])
            {
                int index = monotonicDecreasing.Pop();
                result[index] = i - index;
            }

            monotonicDecreasing.Push(i);
        }

        return result;
    }
}
```

# 853. Car Fleet
## Difficulty: Medium
## Topics: Monotonic Stack, Sorting

### Solution 1 - Monotonic Stack
- By sorting the cars based on their starting positions, we can iterate from the one closest to the destination to the one furthest from it - this allows us to determine which cars will catch up to each other
- we calculate the time t it takes for each car to reach the destination `t = (target - position[i]) / speed[i]`
- When a faster car reaches a slower one - the speed of both becomes that of the slower car -> monotonic decreasing stack
- Return the size of the stack for the number of fleets

```csharp
public class Solution {
    public int CarFleet(int target, int[] position, int[] speed)
    {
        var stack = new Stack<double>();

		// Sort the cars by their starting position (ascending order)
        Array.Sort(position, speed);

        for (int i = 0; i < position.Length; i++)
        {
			// Calculate the time it takes for the current car to reach the target
            var current = (double)(target - position[i]) / speed[i];

			// Check if the current car catches up to the car ahead of it
            // If the current car's time is less than or equal to the time of the car ahead, it means the current car will catch up and form a fleet with the car ahead
			// Pop the car that is ahead from the stack
            while (stack.Any() && current >= stack.Peek())
            {
                stack.Pop();
            }

			// Push the current car's time onto the stack
            stack.Push(current);
        }
		
        return stack.Count();
    }
}
```

# 875. Koko Eating Bananas
## Difficulty: Medium
## Topics: Binary search

### Solution 2 - Binary Search
- The minimum possible eating speed is 1, the maximum possible is the max pile size
- We can apply a binary search on the eating speed
  - if mid eating speed is too slow then move left pointer
  - if mid eating speed is too high then try to move right pointer to the left

```csharp
public class Solution
{
    public int MinEatingSpeed(int[] piles, int h)
    {
        // The minimum possible eating speed is 1
        int left = 1;
        // The maximum possible eating speed is the maximum pile size
        int right = piles.Max();

        // Perform binary search to find the minimum eating speed
        while (left < right)
        {
            int mid = left + (right - left) / 2;

            // Calculate the total hours needed for the current eating speed (mid)
            int totalHours = 0;
            foreach (int pile in piles)
            {
                totalHours += (int)Math.Ceiling((double)pile / mid);
            }

            // If the total hours is within the limit, try a smaller eating speed
            if (totalHours <= h)
            {
                right = mid;
            }
            // Otherwise, increase the eating speed
            else
            {
                left = mid + 1;
            }
        }

        // When left == right, we've found the minimum eating speed
        return left;
    }
}
```

### Solution 1 - Brute force (time excedded)
```csharp
public class Solution
{
    public int MinEatingSpeed(int[] piles, int h)
    {
        int k = 1;
        while (true)
        {
            int timeSum = 0;
            bool valid = true;

            // Calculate the total time required for the current k
            for (int i = 0; i < piles.Length; i++)
            {
                int pileSize = piles[i];
                int time = (pileSize + k - 1) / k; // Equivalent to Math.Ceiling(pileSize / k)
                timeSum += time;

                // Early exit if the current k is invalid
                if (timeSum > h)
                {
                    valid = false;
                    break;
                }
            }

            // If the current k is valid, return it
            if (valid)
                return k;

            // Otherwise, increment k and try again
            k++;
        }
    }
}
```

# 973. K Closest Points to Origin
## Difficulty: Medium
## Topics: Heap, Sorting, Quickselect

### Solution 1 - Maxheap
- Use a maxHeap with the distance as the priority
- Dequeue the elements if heap count is > k

```csharp
public int[][] KClosest(int[][] points, int k)
{
	if (k == points.Length) return points;

	// Create a max heap using a custom comparer
	var maxHeapComparer = Comparer<int>.Create((a, b) => b.CompareTo(a));
	PriorityQueue<int[], int> maxHeap = new(maxHeapComparer);

	foreach (int[] point in points)
	{
		int distSquared = point[0] * point[0] + point[1] * point[1];
		maxHeap.Enqueue(point, distSquared);

		if (maxHeap.Count > k)
		{
			maxHeap.Dequeue();
		}
	}

	// Create result array
	int[][] result = new int[maxHeap.Count][];
	
	for (int i = 0; i < result.Length; i++)
	{
		result[i] = maxHeap.Dequeue();
	}

	return result;
}
```


# 1011. Capacity To Ship Packages Within D Days
## Difficulty: Medium
## Topics: Binary Search

### Solution
- Consider the ship transport weight as the binary search value
- Left value is the biggest weight of the packages (can't move the biggest package otherwise) and right value is the sum of all packages (move all packages in a day)
- For each capacity search calculate the number of days it would take to move the packages
  - Store the number of days needed to transport all packages `daysNeeded` and the `currentWeight` of the packages
  - For each package weight check if it can be transported with the previous packages, 
    - if yes add it to `currentWeight`
	- if not then increase `daysNeeded` and reset `currentWeight` because the previous packages have been delivered


```csharp
public class Solution
{
    public int ShipWithinDays(int[] weights, int days)
    {
        // Left is max weight of the array - minimum possible ship carry weight otherwise the heviest package can't be carried
        int left = -1;
        
        // Right is the sum of all weights - ship can transport all the items at once
        int right = 0;
        foreach (int weight in weights)
        {
            left = Math.Max(left, weight);
            right += weight;
        }

        while (left < right)
        {
            int currentCapacity = (left + right) / 2;
            
            // If ship can move more items at once store the weights in currWeight
            int daysNeeded = 1;
            int currWeight = 0;
            foreach (int weight in weights)
            {
                // If weight of the package is more than the capacity then jump to the next day and transport packages (remove currWeight)
                if (currWeight + weight > currentCapacity)
                {
                    daysNeeded++;
                    currWeight = 0;
                }

                // Add package weight to currentWeight
                currWeight += weight;
            }

            // If the ship needs more days to transport the packages than the limit then increase the capacity
            if (daysNeeded > days)
            {
                left = currentCapacity + 1;
            }
            else
            {
                right = currentCapacity;
            }
        }

        return left;
    }
}
```

# 1046. Last Stone Weight
## Difficulty: Easy
## Topics: Heap

### Solution 1 - Maxheap
```csharp
public class Solution
{
    public int LastStoneWeight(int[] stones)
    {
        var maxHeapComparer = Comparer<int>.Create((x, y) => y.CompareTo(x));
        var maxHeap = new PriorityQueue<int, int>(maxHeapComparer);

        foreach (var stone in stones)
        {
            maxHeap.Enqueue(stone, stone);
        }

        while (maxHeap.Count >= 2)
        {
            var stone1 = maxHeap.Dequeue();
            var stone2 = maxHeap.Dequeue();

            var newStone = stone1 - stone2;
            maxHeap.Enqueue(newStone, newStone);
        }

        return maxHeap.Dequeue();
    }
}
```

# 1475. Final Prices With a Special Discount in a Shop
## Difficulty: Easy
## Topics: Two pointers, Monotonic stack

### Solution 1 - Two pointers (faster than monotonic stack)
- Loop over each element and calculate the discount with the first price lower than it
- Left is on the current price and right is moved from the next element until the end
  - If a number is found so prices[right] <= prices[left] then calcualte the discount

```csharp
public class Solution
{
    public int[] FinalPrices(int[] prices)
    {
        int[] discountedPrices = new int[prices.Length];

        for (int i = 0; i < prices.Length; i++)
        {
            discountedPrices[i] = prices[i];
            for (int j = i + 1; j < prices.Length; j++)
            {
                if (prices[j] <= prices[i])
                {
                    discountedPrices[i] -= prices[j];
                    break;
                }
            }
        }

        return discountedPrices;
    }
}
```

```csharp
public class Solution
{
    public int[] FinalPrices(int[] prices)
    {
        int[] discountedPrices = new int[prices.Length];
        
        int left = 0;
        while (left < prices.Length)
        {
            discountedPrices[left] = prices[left];
            
            int right = left + 1;
            while (right < prices.Length)
            {
                if (prices[right] <= prices[left])
                {
                    discountedPrices[left] -= prices[right];
                    break;
                }
                right++;
            }
            
            left++;
        }

        return discountedPrices;
    }
}
```

### Solution 2 - Increasint monotonic stack
- Use a monotonic stack to store the prices with no lower price for the discount
- When a lower price is found then pop the elements from the stack until the top of the stack is empty or it has >= value than the current price
- Store the popped elements in a dictionary with [index, discountPrice]

```csharp
public class Solution
{
    public int[] FinalPrices(int[] prices)
    {
        // Stack to store indices of prices
        var increasingStack = new Stack<int>(); 
        
        // Dictionary to store discounts for each index
        var discountDict = new Dictionary<int, int>(); 

        for (int i = 0; i < prices.Length; i++)
        {
            // While the stack is not empty and the current price is less than or equal to the price at the top of the stack
            while (increasingStack.Count > 0 && prices[i] <= prices[increasingStack.Peek()])
            {
                // Get the index of the previous price
                int prevIndex = increasingStack.Pop(); 
                
                // Store the discount for the previous index
                discountDict[prevIndex] = prices[i]; 
            }

            // Push the current index onto the stack
            increasingStack.Push(i); 
        }

        int[] discountedPrices = new int[prices.Length];
        for (int i = 0; i < prices.Length; i++)
        {
            // If the current index has a discount, subtract it from the price; otherwise, use the original price
            discountedPrices[i] = discountDict.ContainsKey(i) ? prices[i] - discountDict[i] : prices[i];
        }

        return discountedPrices;
    }
}
```

# 2404. Most Frequent Even Element
## Difficulty: Easy
## Topics: Hash table, Sorting, Heap

### Solution 1 - Dictionary with frequencies
- Use a dictionary to find frequencies of each num
- Loop over all the kvps in the dictionary and update the element

```csharp
public int MostFrequentEven(int[] nums)
{
	Dictionary<int, int> freqMap = new Dictionary<int, int>();

	foreach (var num in nums)
	{
		if (num % 2 == 0)
		{
			if (!freqMap.ContainsKey(num))
			{
				freqMap[num] = 0;
			}

			freqMap[num]++;
		}
	}
	
	if (freqMap.Count == 0)
	{
		return -1;
	}
	
	(int mostFrequentEven, int maxFrequency) = (-1, -1);

	foreach (var kvp in freqMap)
	{
		if (kvp.Value > maxFrequency || (kvp.Value == maxFrequency && kvp.Key < mostFrequentEven))
		{
			mostFrequentEven = kvp.Key;
			maxFrequency = kvp.Value;
		}
	}
	
	return mostFrequentEven;
}
```


# 2594. Minimum Time to Repair Cars
## Difficulty: Medium
## Topics: Binary Search

### Solution 
- Apply a binary search on the time that each engineer takes to repair a car
- Maximum possible value for the binary search is the time that the lowest rank takes to repair every car

```csharp
public class Solution
{
    public long RepairCars(int[] ranks, int cars)
    {
        // Min time to repair
        long  left = 0;

        // Max time to repair all the cars
        // Given by considering if the lowest rank tries to repair all the cars
        long  right = 1L * ranks.Min() * cars * cars;

        while (left <= right)
        {
            long  mid = (left + right) / 2;

            // time = r * c^2 => cars repaired in a time t are sqrt( time / r)
            long repairedCars = 0;
            foreach (var rank in ranks)
                repairedCars += (long)Math.Sqrt(1.0d * mid / rank);                

            // If the total cars that could be repaired in time frame is less than target
            // Then there is not enough time to repair the cars - increase time needed to repair
            if (repairedCars < cars)
                left = mid + 1;

            // If the total cars that could be repaired in time frame is greater than target
            // Then there is too much time to repair the cars - try to reduce time taken to repair
            if (repairedCars >= cars)
                right = mid - 1;
        }

        return left;
    }
}
```