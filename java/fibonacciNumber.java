import java.util.Scanner;

class Solution {
    public int fib(int n) {
        int prev = 0, curr = 1;
        if (n <= 0) {
            return n;
        }
        int i = 1;
        while (i <= n) {
            int temp = prev + curr;
            prev = curr;
            curr = temp;
            ++i;
        }
        return prev;
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        Solution obj = new Solution();
        System.out.println(obj.fib(scan.nextInt()));
    }
}


// 0 1 1 2