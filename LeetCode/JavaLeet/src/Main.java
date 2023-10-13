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

//    public boolean isValidSudoku(char[][] board) {
//
//        // HashSet solution
//        // use a hashset to store all the seen values in the sudoku board
//        // the square elements can be obtained by dividing row and col numbers by 3
//        // 1, 2, 3 -> box 1; 4,5,6 -> box 2; 7,8,9 -> box 3
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
//
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


    public boolean searchMatrix(int[][] matrix, int target) {

        int col = 0, row = 0;
        int rows = matrix.length, cols = matrix[0].length;

        while (row < rows && col < cols) {
            if (target > matrix[row][cols - 1]) {
                row++;
            } else {
                col++;
            }

            if
        }
    }


    public static void main(String[] args) {
//        int[][] matrix = {{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}, {13, 14, 15, 16}};
//
//        ListNode l13 = new ListNode(3);
//        ListNode l12 = new ListNode(4);
//        l12.next = l13;
//        ListNode l11 = new ListNode(2);
//        l11.next = l12;
//
//        ListNode l23 = new ListNode(4);
//        ListNode l22 = new ListNode(6);
//        l22.next = l23;
//        ListNode l21 = new ListNode(5);
//        l21.next = l22;
//
//        System.out.println(addTwoNumbers(l11, l21).val);

        int[] input = new int[]{0, 3, 7, 2, 5, 8, 4, 6, 0, 1};
        System.out.println(longestConsecutive(input));

    }
}