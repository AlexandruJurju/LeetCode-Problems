# 1. Two Sum
## Difficulty: Easy
## Topics: Hash map
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

# 13. Roman to Integer
## Difficulty: Easy
## Topics: Hash table, Math, String
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


# 20. Valid Parentheses
## Difficulty: Easy  
## Topics: Stack, String  
### Solution 1 - Stack for pairs
- **Loop over all characters in the input string:**
   - If the character is an opening parenthesis (`(`, `[`, `{`), push it onto the stack
   - If the character is a closing parenthesis (`)`, `]`, `}`), pop the top element from the stack and check if it matches the corresponding opening parenthesis, if they dont match → return `false`
   - If no element can be popped (stack is empty), the parentheses are not valid → return `false`

- **Edge cases:**
   - If the input string length is odd, there will always be an unpaired parenthesis → return `false`
   - If the stack is not empty after processing all characters, there are unpaired parentheses → return `false`
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




# 49. Group Anagrams
## Difficulty: Medium
## Topics: Hashmap
### Solution 1 - Dictionary with sum of chars as the key
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

### Solution 2 - Dictionary with sorted word as the key
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

# 347. Top K Frequent Elements
## Dificulty: Medium
## Topics: Hashmap, Heap


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