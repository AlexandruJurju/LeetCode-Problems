import java.util.*;

public class Main {
    public static class ListNode {
        int val;
        ListNode next;

        ListNode() {
        }

        ListNode(int val) {
            this.val = val;
        }

        ListNode(int val, ListNode next) {
            this.val = val;
            this.next = next;
        }
    }

    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        TreeNode() {
        }

        TreeNode(int val) {
            this.val = val;
        }

        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }


    // 1. Two Sum, 60% faster

    //    two pass method,
    //    1. make a hashmap and put all index and value pairs in it <K=index,V=val>
    //    2. loop over all elements in the array and calculate for each one the complement, the difference between target and itself
    //    then search the hashmap using the complement as the key <=> find the elements so that their sum == target

//    public static int[] twoSum(int[] nums, int target) {
//        HashMap<Integer, Integer> diffMap = new HashMap<>();
//        // create the hashmap with <index,value>
//        for (int i = 0; i < nums.length; i++) {
//            diffMap.put(nums[i], i);
//        }
//
//        for (int i = 0; i < nums.length; i++) {
//            int complement = target - nums[i];
//            // check if complement can be found in the hashmap & check if the index found in the hashmap is not the same as the current element
//            if (diffMap.containsKey(complement) && diffMap.get(complement) != i) {
//                return new int[]{i, diffMap.get(complement)};
//            }
//        }
//
//        return new int[]{};
//    }

    // one pass method, 99% faster
    // loop over all values in the array and check for each one if complement is in hashMap
    // if it is then return it as a result
    // otherwise insert the current element index and val in the hashmap and continue searching

//    public static int[] twoSum(int[] nums, int target) {
//        HashMap<Integer, Integer> valMap = new HashMap<>();
//        for (int i = 0; i < nums.length; i++) {
//            int complement = target - nums[i];
//            // check if complement can be found in the hashmap
//            if (valMap.containsKey(complement)) {
//                return new int[]{i, valMap.get(complement)};
//            }
//            // if not then add element to hashmap
//            valMap.put(nums[i], i);
//        }
//
//        return new int[]{};
//    }

    // 2. Add two numbers
    // at the start make a resultNode and a dummyNode
    // while l1 is not empty, l2 not empty and carry is not empty do
    // if l1 is not null then add the value to current sum and go to next node
    // if l2 is not null then add the value to current sum and go to next node
    // add carry to the current sum, sum = l1.val + l2.val + carry
    // the value of the node will be sum % 10 to get the smaller val
    // the value of carry will be sum / 10
    // make a new node with the value = sum%10 and


//    public static ListNode addTwoNumbers(ListNode l1, ListNode l2) {
//        int carry = 0;
//        ListNode dummyHead = new ListNode();
//        ListNode result = dummyHead;
//
//        while (l1 != null || l2 != null || carry == 1) {
//            int sum = 0;
//
//            if (l1.val != null) {
//                sum += l1.val;
//                l1 = l1.next;
//            }
//
//            if (l2.val != null) {
//                sum += l2.val;
//                l2 = l2.next;
//            }
//
//            sum += carry;
//            carry = sum / 10;
//            int val = sum % 10;
//
//            ListNode node = new ListNode(val);
//            result.next = node;
//            result = result.next;
//
//        }
//
//        return dummyHead.next;
//    }


// 48. Rotate Image
//   * clockwise rotate
//   * first reverse up to down, then swap the symmetry
//   * 1 2 3     7 8 9     7 4 1
//   * 4 5 6  => 4 5 6  => 8 5 2
//   * 7 8 9     1 2 3     9 6 3
//
//   * anticlockwise rotate
//   * first reverse left to right, then swap the symmetry
//   * 1 2 3     3 2 1     3 6 9
//   * 4 5 6  => 6 5 4  => 2 5 8
//   * 7 8 9     9 8 7     1 4 7

//    public static int[][] transposeMatrix(int[][] matrix) {
//        int rows = matrix.length;
//        int cols = matrix[0].length;
//
//        for (int i = 0; i < rows - 1; i++) {
//            for (int j = i + 1; j < cols; j++) {
//                int temp = matrix[i][j];
//                matrix[i][j] = matrix[j][i];
//                matrix[j][i] = temp;
//            }
//        }
//
//        return matrix;
//    }
//
//    public static int[][] reverseVertical(int[][] matrix) {
//        int rows = matrix.length;
//        int cols = matrix[0].length;
//
//        for (int i = 0; i < rows; i++) {
//            for (int j = 0; j < cols / 2; j++) {
//                int temp = matrix[i][j];
//                matrix[i][j] = matrix[i][cols - 1 - j];
//                matrix[i][cols - 1 - j] = temp;
//            }
//        }
//
//        return matrix;
//    }
//
//    public static int[][] rotate90DegreesClockwise(int[][] matrix) {
//        return reverseVertical(transposeMatrix(matrix));
//    }

    // 271. Contains Duplicate | Easy | 12/10/2023
    // sorting approach - sort the array and check the next element if it equals the current one
//    public static boolean containsDuplicate(int[] nums) {
//        Arrays.sort(nums);
//        for (int i = 0; i < nums.length - 1; i++) {
//            if (nums[i] == nums[i + 1]) {
//                return true;
//            }
//        }
//        return false;
//    }

    // hashset method -
    // create a hashset then loop over elements in array for each element check if its already in the hashset
    // if it is then the array contains a duplicate -> return true
    // otherwise add it to the hashset and continue checking
    // if loop finishes without finding any elements in the hashset then there are no duplicates -> return false
//    public static boolean containsDuplicate(int[] nums) {
//        HashSet<Integer> seen = new HashSet<>();
//
//        for (int num : nums) {
//            if (seen.contains(num)) {
//                return true;
//            }
//            seen.add(num);
//        }
//
//        return false;
//    }

    // 242. Valid Anagram | 12/10/2023
//    public static boolean isAnagram(String s, String t) {
//        // Method 1 - Sort char letters approach
//        // sort the letters in the string and then compare the sorted arrays
////        if (s.length() != t.length()) {
////            return false;
////        }
//
////        char[] sChars = s.toCharArray();
////        char[] tChars = t.toCharArray();
////
////        Arrays.sort(sChars);
////        Arrays.sort(tChars);
////
////        return sChars == tChars;
//
//        // Method 2 - HashTable
//        // make a hashtable for each string, each table contains the letters found in the strings and their frequency
//
//        // Method 2.1
//        // make a single hashtable to keep track of the frequencies, for chars in s add frequencies to hashmap, for chars in t subtract them
//        // at the end check if there is any element != 0
//
////        if (s.length() != t.length()) {
////            return false;
////        }
////
////        HashMap<Character, Integer> freqMap = new HashMap<>();
////        for (char c : s.toCharArray()) {
////            freqMap.put(c, freqMap.getOrDefault(c, 0) + 1);
////        }
////
////        for (char c : t.toCharArray()) {
////            freqMap.put(c, freqMap.getOrDefault(c, 0) - 1);
////        }
////
//////        for (char val : freqMap.keySet()) {
//////            if (freqMap.get(val) != 0) {
//////                return false;
//////            }
//////        }
////
////        // improvement, check only values, don't use get on the hashmap
////        for (int val : freqMap.values()) {
////            if (val != 0) {
////                return false;
////            }
////        }
////        return true;
//
//
//        // Method 3
//        // use a count array - make an array of size 26 that counts the frequency  of characters found
////        int[] freq = new int[26];
////
////        if (s.length() != t.length()) {
////            return false;
////        }
////
////        for (int i = 0; i < s.length(); i++) {
////            // smart subtraction of ASCII "a", so that "a" corresponds to element in first index
////            freq[s.charAt(i) - 'a']++;
////        }
////
////        for (int i = 0; i < t.length(); i++) {
////            freq[t.charAt(i) - 'a']--;
////        }
////
////        for (int val : freq) {
////            if (val != 0) {
////                return false;
////            }
////        }
////        return true;
//    }

    // 49. Group Anagrams
    // use a hashmap that contains the sorted string as a key, and a list of all words that have the sorted characters as a value
    // for each word in strs: sort the characters, check if hashmap contains the sorted word, if not then init a blank ArrayList, at the end add the word to the ArrayList using the key
//    public List<List<String>> groupAnagrams(String[] strs) {
//        HashMap<String, List<String>> anagramMap = new HashMap<>();
//
//        for (String word : strs) {
//            char[] wordChars = word.toCharArray();
//            Arrays.sort(wordChars);
//            String sortedWord = new String(wordChars);
//
//            if (!anagramMap.containsKey(sortedWord)) {
//                anagramMap.put(sortedWord, new ArrayList<>());
//            }
//            anagramMap.get(sortedWord).add(word);
//        }
//
//        return new ArrayList<>(anagramMap.values());
//    }

    // 36. Valid Sudoku
    // HashSet solution
    // use a hashset to store all the seen values in the sudoku board
    // the square elements can be obtained by dividing row and col numbers by 3
    // 1, 2, 3 -> box 1; 4,5,6 -> box 2; 7,8,9 -> box 3
//    public boolean isValidSudoku(char[][] board) {
//        HashSet<String> seen = new HashSet<>();
//
//        for (int i = 0; i < board.length; i++) {
//            for (int j = 0; j < board[0].length; j++) {
//                char elem = board[i][j];
//                if (elem != '.') {
//                    if (!seen.add(elem + "r" + i) || !seen.add(elem + "c" + j) || !seen.add(elem + "b" + i / 3 + j / 3)) {
//                        return false;
//                    }
//                }
//            }
//        }
//        return true;
//    }

    // 128. Longest Consecutive Sequence

//    public static int longestConsecutive(int[] nums) {
//        // 1 - HashSet method
//        // use a hashset that contains all numbers in the array
//        // init an int value to be global longest = 0
//        // for each number in the array: init an int currentMax that stores the maximum length of the current chain to 1
//        // search the hashset for previous number, while set contains previous number, remove it from set, and increment currentMax
//        // search the hashset for next number, while set contains the next number, remove it from set, and increment currentMax
//        // at the end of the iteration, update maximum to be Math.max(longest,currentMax)
////        HashSet<Integer> numSet = new HashSet<>();
////
////        for (int num : nums) {
////            numSet.add(num);
////        }
////
////        int longest = 0;
////        for (int current : nums) {
////            int next = current + 1;
////            int prev = current - 1;
////            int currentMax = 1;
////
////            while (numSet.contains(prev)) {
////                numSet.remove(prev--);
////                currentMax++;
////            }
////
////            while (numSet.contains(next)) {
////                numSet.remove(next++);
////                currentMax++;
////            }
////
////            longest = Math.max(longest, currentMax);
////        }
////        return longest;
//    }

    // 704. Binary Search
//    public int search(int[] nums, int target) {
////        int length = nums.length;
////
////        if (length == 0) {
////            return -1;
////        }
////
////        // length is total number of elements
////        // right is the rightmost index, and because numbering is from 0, right should be length - 1
////        int right = length - 1;
////        int left = 0;
////
////        while (left <= right) {
////            int middle = (left + right) / 2;
////            int element = nums[middle];
////
////            if (element == target) {
////                return middle;
////            }
////
////            if (target < element) {
////                right = middle - 1;
////            }
////
////            if (target > element) {
////                left = middle + 1;
////            }
////        }
////
////        return -1;
////    }

    // 74. Search a 2D Matrix
//    public static boolean searchMatrix(int[][] matrix, int target) {
//
//        // Method 1 - My Solution
//        // the matrix is just multiple sorted arrays on different rows
//        // for each row check if the target is <= than the element on the last column
//        // basically if the target could potentially be found in the sorted row
//        // an improvement could be to use BINARY SEARCH FOR THE ROW instead of iteratively searching the cols
////        int col = 0, row = 0;
////        int rows = matrix.length, cols = matrix[0].length;
////
////        while (row < rows) {
////            if (target > matrix[row][cols - 1] && target < matrix[row][col]) {
////                return false;
////            }
////
////            if (target <= matrix[row][cols - 1]) {
////                while (col < cols) {
////                    if (matrix[row][col] == target) {
////                        return true;
////                    }
////                    col++;
////                }
////                return false;
////            }
////            row++;
////        }
////        return false;
//
//        // Method 1.1 - Simpler conditions, start the search at the element in the last col
//        // if element is < target then jump to next row
//        // if element > target then decrement cols until you find the element or reach the first col without finding anything
//
////        int i = 0, j = matrix[0].length - 1;
////        while (i < matrix.length && j >= 0) {
////            if (matrix[i][j] == target)
////                return true;
////            else if (matrix[i][j] > target)
////                j--;
////            else if (matrix[i][j] < target)
////                i++;
////        }
////        return false;
//    }

    // 240. Search a 2D Matrix II
//    public boolean searchMatrix(int[][] matrix, int target) {
//
//        // Method 1 - use 2 pointers
//        // start looking in the matrix from the bottom left element and value of current element
//        // bottom left element was chosen because if we go up then there are only smaller values and if we go right there are bigger values
//        // if current element < target then increment col index to find bigger number
//        // if current element > target then increment row index to find lower number
//
//        int rows = matrix.length, cols = matrix[0].length;
//        int row = matrix.length - 1, col = 0;
//
//        while (row >= 0 && col < cols) {
//            int elem = matrix[row][col];
//
//            if (elem == target) {
//                return true;
//            }
//
//            if (target > elem) {
//                col += 1;
//            }
//            if (target < elem) {
//                row -= 1;
//            }
//        }
//        return false;
//    }

    // 153. Find Minimum in Rotated Sorted Array
//    public int findMin(int[] nums) {
//        int left = 0;
//        int right = nums.length - 1;
//
//        while (left <= right) {
//            int middle = (left + right) / 2;
//            int middleElement = nums[middle];
//
//            if (left == right) {
//                return middleElement;
//            }
//
//            if (middleElement > nums[right]) {
//                left = middle + 1;
//            } else {
//                right = middle;
//            }
//
//        }
//
//        return -1;
//    }

    // 167. Two Sum II - Input Array Is Sorted
//    public int[] twoSum(int[] numbers, int target) {
    // Method 1
//        // use 2 pointers, left and right to choose elements in the sorted array
//        // if sum of num1 and num2 is bigger than the target then decrement right to lower the value of the sum
//        // if sum of num1 and num2 is smaller than the target then increment left to raise the value of the sum
//
//        int left = 0, right = numbers.length - 1;
//
//        while (left <= right) {
//            int sum = numbers[left] + numbers[right];
//
//            if (sum == target) {
//                return new int[]{left + 1, right + 1};
//            } else if (sum > target) {
//                right--;
//            } else {
//                left++;
//            }
//        }
//
//        return new int[]{-1, -1};
//    }


    // Bubble Sort

//    public static int[] bubbleSort(int[] arr) {
//        int length = arr.length;
//        for (int i = 0; i < length; i++) {
//            // add -i to j limit to skip the last i items that were already sorted
//            for (int j = 0; j < length - i - 1; j++) {
//                if (arr[j] > arr[j+1]) {
//                    int tmp = arr[j];
//                    arr[j] = arr[j + 1];
//                    arr[j + 1] = tmp;
//                }
//            }
//        }
//        return arr;
//    }

    // Insertion Sort

//    public static int[] insertionSort(int[] arr) {
//        int n = arr.length;
//        for (int i = 1; i < n; ++i) {
//            int key = arr[i];
//            int j = i - 1;
//
//            // Move elements of arr[0..i-1], that are greater than key, to one position ahead  of their current position
//            while (j >= 0 && arr[j] > key) {
//                arr[j + 1] = arr[j];
//                j = j - 1;
//            }
//            arr[j + 1] = key;
//        }
//        return arr;
//    }

    // Selection Sort

//    public static int[] selectionSort(int[] arr) {
//        int n = arr.length;
//        for (int i = 0; i < n - 1; i++) {
//            int minIndex = i;
//            for (int j = i + 1; j < n; j++) {
//                if (arr[minIndex] > arr[j]) {
//                    minIndex = j;
//                }
//            }
//
//            int minNumber = arr[minIndex];
//            arr[minIndex] = arr[i];
//            arr[i] = minNumber;
//        }
//        return arr;
//    }

    // Merge Sort

//    public static void mergeSort(int[] arr) {
//        int length = arr.length;
//
//        if (length == 1) {
//            return;
//        }
//
//        int mid = length / 2;
//
//        int[] leftArray = new int[mid];
//        int[] rightArray = new int[length - mid];
//
//        int j = 0;
//        for (int i = 0; i < length; i++) {
//            if (i < mid) {
//                leftArray[i] = arr[i];
//            } else {
//                rightArray[j] = arr[i];
//                j++;
//            }
//        }
//
//        mergeSort(leftArray);
//        mergeSort(rightArray);
//        merge(leftArray, rightArray, arr);
//    }
//
//    private static void merge(int[] leftArray, int[] rightArray, int[] arr) {
//        int leftSize = arr.length / 2;
//        int rightSize = arr.length - leftSize;
//        int i = 0, leftIndex = 0, rightIndex = 0;
//
//        while (leftIndex < leftSize && rightIndex < rightSize) {
//            if (leftArray[leftIndex] < rightArray[rightIndex]) {
//                arr[i] = leftArray[leftIndex];
//                i++;
//                leftIndex++;
//            } else {
//                arr[i] = rightArray[rightIndex];
//                i++;
//                rightIndex++;
//            }
//        }
//
//        while (leftIndex < leftSize) {
//            arr[i] = leftArray[leftIndex];
//            i++;
//            leftIndex++;
//        }
//
//        while (rightIndex < rightSize) {
//            arr[i] = rightArray[rightIndex];
//            i++;
//            rightIndex++;
//        }
//    }

    // Quick Sort
    // moves smaller elements to left of a pivot and bigger elements to the right of the pivot
    // recursively divide array in 2 partitions
    // Time Complexity:
    //      Best Case - O(n log(n))
    //      Average Case - O (n log(n))
    //      Worst Case - O (n^2)
    // Space Complexity:
    //      O(log(n))
//    public static void quicksort(int[] arr, int low, int high) {
//        if (low >= high) {
//            return;
//        }
//
//        int pivot = partition(arr, low, high);
//        quicksort(arr, low, pivot - 1);
//        quicksort(arr, pivot + 1, high);
//    }
//
//    public static int partition(int[] arr, int low, int high) {
//        int pivot = arr[high];
//        int i = low - 1;
//
//        // use 2 pointers - i and j to swap elements
//        // j - points to the current element in the given array
//        // i - points to the biggest element to the left of j
//        // when arr[j] < pivot then swap arr[i] and arr[j]
//        // at the high, when all elements have been look at then swap arr[i] with arr[high], put the pivot so that
//        // elements to the left are <= and elements to the right are >= than pivot value
//
//        for (int j = low; j <= high - 1; j++) {
//            if (arr[j] < pivot) {
//                i++;
//                int temp = arr[i];
//                arr[i] = arr[j];
//                arr[j] = temp;
//            }
//        }
//        i++;
//        int temp = arr[i];
//        arr[i] = arr[high];
//        arr[high] = temp;
//
//        return i;
//    }

    // 20. Valid Parenthesis
//    public static boolean isValid(String s) {
//        // if length is not even then there is one extra bracket without a match -> not valid
//        if (s.length() % 2 == 1) {
//            return false;
//        }
//
//        // Method 1
//        // use a stack to store all open parentheses found in the string
//        // loop over all chars in string, if it finds an open parenthesis it pushes it to the stack
//        // when you find a closing parenthesis, pop the last element from the stack and check if it's a match )( ][ }{
//        // if stack is empty when trying to pop then there are pairs without a match -> false
//        // at the end check if stack still has elements in it, if there are values without a pair -> if yes return false
//        Stack<Character> charStack = new Stack<>();
//
//        char[] chars = s.toCharArray();
//        for (char c : chars) {
//            if (c == '(' || c == '[' || c == '{') {
//                charStack.push(c);
//            } else {
//                if (charStack.isEmpty()) {
//                    return false;
//                }
//                char popped = charStack.pop();
//
//                if ((c == ')' && popped != '(') ||
//                        (c == ']' && popped != '[') ||
//                        (c == '}' && popped != '{')) {
//                    return false;
//                }
//            }
//        }
//
//
//        return charStack.isEmpty();
//    }

    // 155. Min Stack
    // use 2 stacks, one stack has normal behaviour and one is a min stack
    // whenever an element is pushed on the normal stack check what the min value is and push the min value on the min stack
//    class MinStack {
//        Stack<Integer> normalStack;
//        Stack<Integer> minStack;
//
//        public MinStack() {
//            normalStack = new Stack<>();
//            minStack = new Stack<>();
//            minStack.push(Integer.MAX_VALUE);
//        }
//
//        public void push(int val) {
//            normalStack.push(val);
//            minStack.push(Math.min(val, minStack.peek()));
//        }
//
//        public void pop() {
//            normalStack.pop();
//            minStack.pop();
//        }
//
//        public int top() {
//            return normalStack.peek();
//        }
//
//        public int getMin() {
//            return minStack.peek();
//        }
//    }

    // 226. Invert Binary Tree
//    public static TreeNode invertBinaryTree(TreeNode root) {
//        if (root == null) {
//            return root;
//        }
//
//        invertBinaryTree(root.left);
//        invertBinaryTree(root.right);
//
//        // when the 2 recursion calls are done, the root node contains the edge left node and the edge right node
//        // swap the nodes before returning root
//        TreeNode tmp = root.left;
//        root.left = root.right;
//        root.right = tmp;
//
//        return root;
//    }

    // 61. Rotate List | Diff: Medium | Tags: LinkedList, TwoPointers | Date: 17/10/2023 |
//    public static ListNode rotateRight(ListNode head, int k) {
//        // Method 1
//        // https://www.youtube.com/watch?v=UcGtPs2LE_c
//
//        // if head is null return null
//        if (head == null) {
//            return null;
//        }
//
//        // find length and tail node of the list
//        int length = 1;
//        ListNode tail = head;
//        while (tail.next != null) {
//            tail = tail.next;
//            length++;
//        }
//
//        // if number of rotates is multiple of k then the list stays the same, use k%length to find the number of real rotates
//        k = k % length;
//
//        // if k == 0 then number of rotates is divisible by k, so the resulting list would be the same
//        if (k == 0) {
//            return head;
//        }
//
//        // find the cutoff position in the linked list, the kth node from the tail of the list
//        ListNode current = head;
//        for (int i = 0; i < length - k - 1; i++) {
//            current = current.next;
//        }
//
//        ListNode newHead = current.next;
//        current.next = null;
//        tail.next = head;
//
//        return newHead;
//    }

    //206. Reverse Linked List
//    public ListNode reverseList(ListNode head) {
//        ListNode current = head;
//        ListNode previous = null;
//
//        while (current != null) {
//            ListNode next = current.next;
//            current.next = previous;
//            previous = current;
//            current = next;
//        }
//
//        return previous;
//    }

    // 200. Number of Islands
//    public static int numIslands(char[][] grid) {
//        int islandCount = 0;
//        for (int i = 0; i < grid.length; i++) {
//            for (int j = 0; j < grid[0].length; j++) {
//                if (grid[i][j] == '1') {
//                    islandCount++;
//                    DFSSink(grid, i, j);
//                }
//            }
//        }
//        return islandCount;
//    }

    // recursive DFS function
//    public static void DFSSink(char[][] grid, int i, int j) {
//        if (i < 0 || j < 0 || i >= grid.length || j >= grid[0].length || grid[i][j] != '1') {
//            return;
//        }
//
//        grid[i][j] = '0';
//        DFSSink(grid, i + 1, j);
//        DFSSink(grid, i - 1, j);
//        DFSSink(grid, i, j + 1);
//        DFSSink(grid, i, j - 1);
//    }
//
//    public static void DFSSinkIterative(char[][] grid, int i, int j) {
//        Pair<Integer, String> pair = new Pair<>(1, "One");
//
//    }

    // 21. Merge Two Sorted Lists
//    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
//        // Method 1
//        // make a dummy list, use a loop while the 2 lists are still not null, check current values of each list
//        // if val1<=val2 then dummy.next is list1, advance list1, advance dummy
//        // else dummy.next = list2, advance list2, advance dummy
//        // when exiting loop, at least one list will be null, add the remained of the other list to the dummy
//
//        if (list1 == null) {
//            return list2;
//        }
//        if (list2 == null) {
//            return list1;
//        }
//
//        ListNode newHead = new ListNode();
//        ListNode dummy = newHead;
//
//        while (list1 != null && list2 != null) {
//            int val1 = list1.val;
//            int val2 = list2.val;
//
//            if (val1 <= val2) {
//                dummy.next = list1;
//                list1 = list1.next;
//            } else {
//                dummy.next = list2;
//                list2 = list2.next;
//            }
//            dummy = dummy.next;
//        }
//
////        while (list1 != null) {
////            dummy.next = list1;
////            list1 = list1.next;
////        }
////
////        while (list2 != null) {
////            dummy.next = list2;
////            list2 = list2.next;
////        }
//
//        if (list1 != null) {
//            dummy.next = list1;
//        }
//        if (list2 != null) {
//            dummy.next = list2;
//        }
//
//        return newHead.next;
//    }

    // 700. Search in a Binary Search Tree
//    public TreeNode searchBST(TreeNode root, int val) {
//        if (root == null) {
//            return null;
//        }
//
//        if (root.val == val) {
//            return root;
//        }
//
//        if (root.val > val) {
//            return searchBST(root.left, val);
//        } else {
//            return searchBST(root.right, val);
//        }
//    }


    // 104. Maximum Depth of Binary Tree
//    public int maxDepth(TreeNode root) {
//        if (root == null) {
//            return 0;
//        }
//
//        return Math.max(maxDepth(root.left) + 1, maxDepth(root.right) + 1);
//    }


    // 94. Binary Tree Inorder Traversal - Inorder S,R,D
    // Method 1. Recursive with another function
//    public List<Integer> inorderTraversal(TreeNode root) {
//        List<Integer> list = new ArrayList<Integer>();
//        inorder(root, list);
//        return list;
//    }
//
//    public void inorder(TreeNode root, List<Integer> nums) {
//        if (root == null) return;
//        inorder(root.left, nums);
//        nums.add(root.val);
//        inorder(root.right, nums);
//    }

    // Method 2. Iterative method
//    public List<Integer> inorderTraversal(TreeNode root) {
//        List<Integer> list = new ArrayList<Integer>();
//        Stack<TreeNode> stack = new Stack<TreeNode>();
//        TreeNode cur = root;
//
//        while (cur != null || !stack.empty()) {
//            while (cur != null) {
//                stack.add(cur);
//                cur = cur.left;
//            }
//            cur = stack.pop();
//            list.add(cur.val);
//            cur = cur.right;
//        }
//
//        return list;
//    }

    // 1929. Concatenation of Array
    // Method - init result array with empty array of size nums.length*2
    // result[i] = arr[i], result[i+length] = arr[i]
//    public static int[] getConcatenation(int[] nums) {
//        int length = nums.length;
//        int[] result = new int[length * 2];
//
//        for (int i = 0; i < length; i++) {
//            result[i] = nums[i];
//            result[i + length] = nums[i];
//        }
//
//        return result;
//    }

    // 27. Remove Element | Diff: Easy | Tags: Array, Two Pointers | Date: 25/10/2023
    // Method 1 - use an index to keep track of the numbers of val values AND as a pointer to the current element in nums to be replaced
//    public static int removeElement(int[] nums, int val) {
//        int index = 0;
//
//        for (int i = 0; i < nums.length; i++) {
//            if (nums[i] != val) {
//                nums[index] = nums[i];
//                index++;
//            }
//        }
//
//        return index;
//    }


    // 26. Remove Duplicates from Sorted Array
    // https://leetcode.com/problems/remove-duplicates-from-sorted-array/solutions/3676877/best-method-100-c-java-python-beginner-friendly/
    // The Intuition is to use two pointers, i and j, to iterate through the array. The variable j is used to keep track of the current index where a unique element should be placed. The initial value of j is 1 since the first element in the array is always unique and doesn't need to be changed
//    public int removeDuplicates(int[] nums) {
//        int j = 1;
//        for (int i = 1; i < nums.length; i++) {
//            if (nums[i] != nums[i - 1]) {
//                nums[j] = nums[i];
//                j++;
//            }
//        }
//        return j;
//    }

    // 682. Baseball Game | Diff: Easy | Tags: Stack | Date: 25/10/2023
//    public static int calPoints(String[] operations) {
//        Stack<Integer> vals = new Stack<Integer>();
//        int total = 0;
//
//        for (String s : operations) {
//            switch (s) {
//                case "+" -> {
//                    int num1 = vals.pop();
//                    int res = (vals.peek() + num1);
//                    vals.push(num1);
//                    vals.push(res);
//                }
//                case "D" -> vals.push(vals.peek() * 2);
//                case "C" -> vals.pop();
//                default -> vals.push(Integer.valueOf(s));
//            }
//        }
//
//        while (!vals.isEmpty()) {
//            total += vals.pop();
//        }
//
//        return total;
//    }

    // 707. Design Linked List
//    public class Node {
//        int val;
//        Node next;
//
//        public Node(int val) {
//            this.val = val;
//        }
//    }
//
//    class MyLinkedList {
//
//        Node head;
//        int length;
//
//        public MyLinkedList() {
//            head = null;
//            length = 0;
//        }
//
//        public int get(int index) {
//            if (index > length) {
//                return -1;
//            }
//
//            int count = 0;
//            Node current = head;
//            while (count < index) {
//                count++;
//                current = current.next;
//            }
//            return current.val;
//        }
//
//        public void addAtHead(int val) {
//            Node newHead = new Node(val);
//            newHead.next = head;
//            head = newHead;
//        }
//
//        public void addAtTail(int val) {
//            Node tail = head;
//            while (tail.next != null) {
//                tail = tail.next;
//            }
//            tail.next = new Node(val);
//        }
//
//        public void addAtIndex(int index, int val) {
//            if (index > length)
//                return;
//            if (index == 0)
//                addAtHead(val);
//            else {
//                int counter = 1;
//                Node temp = head;
//                while (counter < index) {
//                    temp = temp.next;
//                    counter++;
//                }
//                Node newNode = new Node(val);
//                Node next = temp.next;
//                temp.next = newNode;
//                newNode.next = next;
//                length++;
//            }
//        }
//
//        public void deleteAtIndex(int index) {
//            if (index >= length) {
//                return;
//            }
//            if (index == 0) {
//                head = head.next;
//                length--;
//            } else {
//                int counter = 1;
//                Node temp = head;
//                while (counter < index) {
//                    temp = temp.next;
//                    counter++;
//                }
//                temp.next = temp.next.next;
//                length--;
//            }
//        }
//    }

    // 347. Top K Frequent Elements
    // Method 1. Use a maxheap
//    public static int[] topKFrequent(int[] nums, int k) {
//        Map<Integer, Integer> map = new HashMap<>();
//        for (int val : nums) {
//            map.put(val, map.getOrDefault(val, 0) + 1);
//        }
//
//        // define the priority of the queue, max value
//        PriorityQueue<Integer> maxHeap = new PriorityQueue<>((a, b) -> map.get(b) - map.get(a));
//        maxHeap.addAll(map.keySet());
//
//        int[] res = new int[k];
//        for (int i = 0; i < k; i++) {
//            res[i] = maxHeap.poll();
//        }
//        return res;
//    }


    // 238. Product of Array Except Self
    // Method 1 -
    // For each number calculate a prefix product of all elements before the value, and postfix product of all elements after the value
    // The product of all values except self is the previous value in prefix and the next value in postfix
//    public static int[] productExceptSelf(int[] nums) {
//        int length = nums.length;
//        int[] prefix = new int[length], postfix = new int[length], res = new int[length];
//
//        prefix[0] = nums[0];
//        postfix[length - 1] = nums[length - 1];
//
//        for (int i = 1; i < length; i++) {
//            prefix[i] = prefix[i - 1] * nums[i];
//        }
//
//        for (int i = length - 2; i >= 0; i--) {
//            postfix[i] = postfix[i + 1] * nums[i];
//        }
//
//        for (int i = 0; i < length; i++) {
//            int pref = 1;
//            int post = 1;
//            if (i > 0) {
//                pref = prefix[i - 1];
//            }
//            if (i < length - 1) {
//                post = postfix[i + 1];
//            }
//
//            res[i] = pref * post;
//        }
//
//        return res;
//    }

    // Method 1 - Use 2 pointers, left and right, if character is not letter or digit then advance it
//    public static boolean isPalindrome(String s) {
//        if (s.isEmpty()) {
//            return true;
//        }
//
//        int left = 0;
//        int right = s.length() - 1;
//        while (left <= right) {
//            char leftChar = s.charAt(left);
//            char rightChar = s.charAt(right);
//            if (!Character.isLetterOrDigit(leftChar)) {
//                left++;
//            } else if (!Character.isLetterOrDigit(rightChar)) {
//                right--;
//            } else {
//                if (Character.toLowerCase(leftChar) != Character.toLowerCase(rightChar)) {
//                    return false;
//                }
//                left++;
//                right--;
//            }
//        }
//
//        return true;
//    }

    // Method 2 - use string buffer to reverse the string and compare it to the original one, if it's different then it's not a palindrome
//    public boolean isPalindrome(String s) {
//        String actual = s.replaceAll("[^A-Za-z0-9]", "").toLowerCase();
//        String rev = new StringBuffer(actual).reverse().toString();
//        return actual.equals(rev);
//    }


    // 150. Evaluate Reverse Polish Notation
    // Method 1 - If it's a number add it to the stack, if it's an operator pop 2 values, apply operator, push result to the stack
//    public static int evalRPN(String[] tokens) {
//        Stack<Integer> stack = new Stack<>();
//        for (String token : tokens) {
//            switch (token) {
//                case "+" -> {
//                    int val1 = stack.pop();
//                    int val2 = stack.pop();
//                    stack.push(val2 + val1);
//                }
//                case "-" -> {
//                    int val1 = stack.pop();
//                    int val2 = stack.pop();
//                    stack.push(val2 - val1);
//                }
//                case "*" -> {
//                    int val1 = stack.pop();
//                    int val2 = stack.pop();
//                    stack.push(val2 * val1);
//                }
//
//                case "/" -> {
//                    int val1 = stack.pop();
//                    int val2 = stack.pop();
//                    stack.push(val2 / val1);
//                }
//
//                default -> stack.push(Integer.valueOf(token));
//            }
//        }
//        return stack.pop();
//    }

    // 22. Generate Parentheses | Diff: Medium | Tags: Backtracking
    // Method 1 - Use backtracking
    // https://leetcode.com/problems/generate-parentheses/solutions/3512769/c-java-python-javascript-using-recursion-with-explanation/
    // We define a helper function, generateParentheses, that takes the following parameters:
    //result: a reference to the vector of strings where we store the generated combinations.
    //current: the current combination being generated.
    //open: the count of opening parentheses "(" included in the current combination.
    //close: the count of closing parentheses ")" included in the current combination.
    //n: the total number of pairs of parentheses to be included.
    //In the generateParentheses function, we first check if the length of the current string is equal to 2n. If it is, we have generated a valid combination, so we add it to the result vector and return.
    //If the length of current is not equal to 2n, we have two choices:
    //If the count of opening parentheses open is less than n, we can add an opening parenthesis to the current combination and make a recursive call to generateParentheses, incrementing the open count by 1.
    //If the count of closing parentheses close is less than the open count, we can add a closing parenthesis to the current combination and make a recursive call to generateParentheses, incrementing the close count by 1.
    //In the generateParenthesis function, we initialize an empty result vector and call the generateParentheses function with the initial values of current as an empty string, open and close counts as 0, and n as the input value.
    //Finally, we return the result vector containing all the generated combinations of well-formed parentheses.
//    public List<String> generateParenthesis(int n) {
//        List<String> res = new ArrayList<String>();
//        backtrack(res, "", 0, 0, n);
//        return res;
//    }
//
//    private void backtrack(List<String> results, String current, int open, int closed, int max) {
//        if (current.length() == max * 2) {
//            results.add(current);
//            return;
//        }
//
//        if (open < max) {
//            backtrack(results, current + "(", open + 1, closed, max);
//        }
//
//        if (closed < open) {
//            backtrack(results, current + ")", open, closed + 1, max);
//        }
//
//    }


    // 739. Daily Temperatures | Diff: Medium | Tags: Stack, Monotonic Stack ???
//    public int[] dailyTemperatures(int[] temperatures) {
//
//    }


    // 875. Koko Eating Bananas
    // Method 1 - Use a binary search for piles value, start search at the middle value (k) between min of piles (1) and max of piles
    // Loop the array and find the number of hours it takes koko to eat all piles for current k
    // if current time is bigger than h then increase k
    // if current time is lower than h then decrease k
    // at the end return left value
//    public static int minEatingSpeed(int[] piles, int h) {
//        int left = 1;
//        // int right = Arrays.streams(piles).max.asInt(); is slower
//        int right = 1000000000;
//
//        while (left <= right) {
//            int mid = (left + right) / 2;
//            int currentH = 0;
//            for (int i = 0; i < piles.length; i++) {
//                currentH += Math.ceil(1.0 * piles[i] / mid);
//            }
//            if (currentH > h) {
//                left = mid + 1;
//            } else {
//                right = mid - 1;
//            }
//        }
//        return left;
//    }

    // 3. Longest Substring Without Repeating Characters | Tags: Sliding Window, Hash Table
    // Method 1 - use 2 pointers to move in the array and a hashset to store the seen characters
    // when you see a character that isn't in the hashset add it and increase right index, recalculate max with current hashset size
    // when you see a character that is in the hashset, remove it, increase left pointer
//    public static int lengthOfLongestSubstring(String s) {
//        HashSet<Character> hashSet = new HashSet<>();
//        int i = 0;
//        int j = 0;
//        int max = 0;
//
//        while (j < s.length()) {
//            if (hashSet.contains(s.charAt(j))) {
//                hashSet.remove(s.charAt(i));
//                i++;
//            } else {
//                hashSet.add(s.charAt(j));
//                j++;
//                max = Math.max(max, hashSet.size());
//            }
//        }
//        return max;
//    }

    // 110. Balanced Binary Tree
    // | heightLeftSubtree - heightRightSubtree | <= 1
    // use max height function for each node in the tree
//    public int height(TreeNode root) {
//        if (root == null) {
//            return 0;
//        }
//
//        return Math.max(height(root.left) + 1, height(root.right) + 1);
//    }
//
//    public boolean isBalanced(TreeNode root) {
//        if (root == null) {
//            return true;
//        }
//        if (Math.abs(height(root.left) - height(root.right)) > 1) {
//            return false;
//        } else {
//            return isBalanced(root.left) && isBalanced(root.right);
//        }
//    }

    // 100. Same Tree
    // Method 1 - Recursive method
    // https://leetcode.com/problems/same-tree/solutions/3746149/recursive-approach-with-easy-steps/
//    public boolean isSameTree(TreeNode p, TreeNode q) {
//        if (p != null && q != null) {
//            return p.val == q.val && isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
//        } else {
//            return p == q;
//        }
//    }

//    public boolean isSameTree(TreeNode p, TreeNode q) {
//        if (p == null && q == null) // Same Tree
//            return true;
//        if (p == null || q == null) // Different Size
//            return false;
//        if (p.val != q.val) // Different Nodes
//            return false;
//        return isSameTree(p.left, q.left) && // check left subtree
//                isSameTree(p.right, q.right); // check right subtree
//    }

    // Method 2 - Iterative ???


    // 572. Subtree of Another Tree
    // Method 1 - recursive use isSameTree function
//    public boolean isSameTree(TreeNode p, TreeNode q) {
//        if (p == null && q == null) {
//            return true;
//        }
//
//        if (p == null || q == null || p.val != q.val) {
//            return false;
//        }
//
//        return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
//    }
//
//    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
//        if (subRoot == null) {
//            return true;
//        }
//
//        if (root == null) {
//            return false;
//        }
//
//        return isSameTree(root, subRoot) || isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot);
//    }

    // 78. Subsets
    // Method 1 - backtracking loop from index to num length
//    public static List<List<Integer>> subsets(int[] nums) {
//        List<List<Integer>> result = new ArrayList<>();
//        List<Integer> current = new ArrayList<>();
//        int index = 0;
//
//        backtrack(result, current, index, nums);
//        return result;
//    }
//
//    public static void backtrack(List<List<Integer>> results, List<Integer> current, int index, int[] nums) {
//        results.add(new ArrayList<>(current));
//
//        for (int i = index; i < nums.length; i++) {
//            current.add(nums[i]);
//            backtrack(results, current, i + 1, nums);
//            current.remove(current.size() - 1);
//        }
//    }

    // Method 2 - changed backtrack function
//    public static List<List<Integer>> subsets(int[] nums) {
//        List<List<Integer>> result = new ArrayList<>();
//        List<Integer> current = new ArrayList<>();
//        int index = 0;
//
//        backtrack(result, current, index, nums);
//        return result;
//    }
//
//    public static void backtrack(List<List<Integer>> results, List<Integer> current, int index, int[] nums) {
//        if (index == nums.length) {
//            results.add(new ArrayList<>(current));
//            return;
//        }
//
//        current.add(nums[index]);
//        backtrack(results, current, index + 1, nums);
//
//        current.remove(current.size() - 1);
//        backtrack(results, current, index + 1, nums);
//
//    }


    // 39. Combination Sum
//    public List<List<Integer>> combinationSum(int[] candidates, int target) {
//        List<List<Integer>> result = new ArrayList<>();
//        backtrack(result, new ArrayList<>(), candidates, target, 0);
//        return result;
//    }
//
//    public void backtrack(List<List<Integer>> result, List<Integer> temp, int[] candidates, int remainder, int index) {
//        if (remainder == 0) {
//            result.add(new ArrayList<>(temp));
//        }
//
//        if (remainder < 0) {
//            return;
//        }
//
//        for (int i = index; i < candidates.length; i++) {
//            temp.add(candidates[i]);
//            // not i+1 because same candidate can be reused
//            backtrack(result, temp, candidates, remainder - candidates[i], i);
//            temp.remove(temp.size() - 1);
//        }
//    }


    // 46. Permutations
//    public static List<List<Integer>> permute(int[] nums) {
//        List<List<Integer>> solution = new ArrayList<>();
//        backtrack(solution, new ArrayList<>(), 0, nums);
//        return solution;
//    }
//
//    public static void backtrack(List<List<Integer>> solution, List<Integer> temp, int index, int[] nums) {
//        if (temp.size() == nums.length) {
//            solution.add(new ArrayList<>(temp));
//        }
//
//        for (int i = index; i < nums.length; i++) {
//            if (temp.contains(nums[i])) {
//                continue;
//            }
//            temp.add(nums[i]);
//            backtrack(solution, temp, index, nums);
//            temp.remove(temp.size() - 1);
//        }
//    }

//    public boolean exist(char[][] board, String word) {
//
//    }
//
//    public boolean backtrack() {
//
//    }

    public static void main(String[] args) {
        int[] nums = new int[]{30, 11, 23, 4, 20};
        String[] vals = new String[]{"4", "13", "5", "/", "+"};
        String test = "abcabcbb";
    }
}