class Solution {
    public int[] plusOne(int[] digits) {
        int carry = 0, i = digits.length - 1, digit = 0;
        do {
            if (i == -1) 
                break;
            carry = 0;
            digits[i] += 1;
            if (digits[i] == 10) {
                carry = 1;
                digits[i] = 0;
            }
            --i;
        } while (carry == 1);
        if (carry == 1) {
            int[] output = new int[digits.length + 1];
            output[0] = 1;
            return output;
        } else {
            return digits;
        }
    }

    public void printArray(int[] a) {
        for (int o: a) {
            System.out.print(o);
        }
        System.out.println();
    }

    public static void main(String[] args) {
        Solution obj = new Solution();

        // int[] digits;{1, 2, 3};
        obj.printArray(obj.plusOne(new int[]{1, 2, 3}));
        // digits = {1};
        obj.printArray(obj.plusOne(new int[]{1}));
        // digits = {9, 9, 9, 9};
        obj.printArray(obj.plusOne(new int[]{9, 9, 9, 9}));
        obj.printArray(obj.plusOne(new int[]{9}));
    }
}
