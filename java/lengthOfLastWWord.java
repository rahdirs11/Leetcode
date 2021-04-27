class Solution {
	public int lengthOfLastWord(String str) {
		str = str.trim();
		int wordLength = 0, i = str.length() - 1;
		while (i >= 0 && str.charAt(i) != ' ') {
			++wordLength;
			--i;
		}
		return wordLength;
	}

	public static void main(String[] args) {
		Solution obj = new Solution();
		System.out.println(obj.lengthOfLastWord(" "));
		System.out.println(obj.lengthOfLastWord("hello world"));
		System.out.println(obj.lengthOfLastWord("a "));
	}
}