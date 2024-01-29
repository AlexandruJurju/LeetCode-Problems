namespace CSharpLeet
{
    class Solution
    {
        public static int[] TwoSum(int[] nums, int target)
        {
            Dictionary<int, int> remainder = new Dictionary<int, int>();
            for (int i = 0; i < nums.Length; i++)
            {
                remainder.Add(i, nums[i] - target);
            }

            for (int i = 0; i < nums.Length; i++)
            {
                if (remainder.ContainsValue(nums[i]))
                {
                    return new []{i,remainder}
                }
            }
        }

        static void Main(string[] args)
        {
            Console.WriteLine("Hello, .NET Core!");
        }
    }
}