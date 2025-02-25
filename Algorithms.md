# Binary Search
```csharp
public int Search(int[] nums, int target)
{
	if (nums.Length == 0) return -1;

	int left = 0;
	int right = nums.Length - 1;

	while (left <= right)
	{
		int middle = (left + right) / 2;

		if (nums[middle] == target)
		{
			return middle;
		}

		if (nums[middle] > target)
		{
			right = middle - 1;
		}
		else
		{
			left = middle + 1;
		}
	}

	return -1;
}
```

# Insertion Sort
```csharp
public void InsertionSort(int[] arr)
{
    for (int i = 1; i < arr.Length; i++)
    {
        int key = arr[i];
        int j = i - 1;

        // Move elements of arr[0, ..., i-1], that are greater than key
        // to one position ahead of their current position
        while (j >= 0 && arr[j] > key)
        {
            arr[j + 1] = arr[j];
            j--;
        }

        arr[j + 1] = key;
    }
}
```

```csharp
public void InsertionSort(int[] arr)
{
    for (int i = 1; i < arr.Length; i++)
    {
        int j = i - 1;
        while (j >= 0 && arr[j + 1] < arr[j])
        {
            int tmp = arr[j + 1];
            arr[j + 1] = arr[j];
            arr[j] = tmp;
            j--;
        }
    }
}
```

# Merge Sort
```csharp
public void MergeSort(int[] arr, int left, int right)
{
    if (left < right)
    {
        int middle = (left + right) / 2;

        MergeSort(arr, left, middle);
        MergeSort(arr, middle + 1, right);

        Merge(arr, left, middle, right);
    }
}

// Merges two subarrays of arr[]
// First subarray is arr[l, ..., m]
// Second subarray is arr[m+1, ..., r]
private void Merge(int[] arr, int left, int middle, int right)
{
    // Find sizes of two subarrays to be merged
    int n1 = middle - left + 1;
    int n2 = right - middle;

    // Create tmp arrays
    int[] Left = new int[n1];
    int[] Right = new int[n2];

    // Copy values to the temp arrays
    for (int i = 0; i < n1; i++)
        Left[i] = arr[left + i];
    for (int i = 0; i < n2; i++)
        Right[i] = arr[middle + 1 + i];

    // Merge the temp arrays
    // Initial indexes of first and second subarrays
    int i1 = 0, i2 = 0;

    // Initial index of merged subarray array
    int k = left;
    while (i1 < n1 && i2 < n2)
    {
        if (Left[i1] <= Right[i2])
        {
            arr[k] = Left[i1];
            i1++;
        }
        else
        {
            arr[k] = Right[i2];
            i2++;
        }

        k++;
    }

    // Copy remaining elements of Left[] if any
    while (i1 < n1)
    {
        arr[k] = Left[i1];
        i1++;
        k++;
    }

    // Copy remaining elements of Right[] if any
    while (i2 < n2)
    {
        arr[k] = Right[i2];
        i2++;
        k++;
    }
}
```


# BFS

# DFS
## DFS Iterative with stack
```csharp
public void DFSIterative(TreeNode root)
{
    Stack<TreeNode> stack = new Stack<TreeNode>();
    stack.Push(root);

    while (stack.Count > 0)
    {
        TreeNode current = stack.Pop();

        if (current.right != null)
        {
            stack.Push(current.right);
        }

        if (current.left != null)
        {
            stack.Push(current.left);
        }
    }
}
```