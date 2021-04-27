import java.util.Scanner;

class Solution {
    private boolean checkAllLower(String word) {
        int i = 0;
        while (i < word.length() && Character.isLowerCase(word.charAt(i))) {
            ++i;
        }
        return i == word.length();
    }

    private boolean checkAllUpper(String word) {
        int i = 0;
        while (i < word.length() && Character.isUpperCase(word.charAt(i))) {
            ++i;
        }
        return i == word.length();
    }

    public boolean detectCapitalUse(String word) {
        if (word.length() == 1) {
            return true;
        }
        if (Character.isLowerCase(word.charAt(0))) {
            return checkAllLower(word.substring(1));
        } else {
            if (Character.isLowerCase(word.charAt(1))) {
                return checkAllLower(word.substring(2));
            } else {
                return checkAllUpper(word.substring(2));
            }
        }
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        Solution obj = new Solution();
        System.out.println(obj.detectCapitalUse(scan.nextLine())? "True": "False");
    }
}