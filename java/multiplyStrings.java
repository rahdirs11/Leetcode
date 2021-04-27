/*
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

 

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"


*/


class Solution {
	public int charToInt(char c) {
		switch (c) {
			case '1':
				return 1;
			case '2':
				return 2;
			case '3':
				return 3;
			case '4':
				return 4;
			case '5':
				return 5;
			case '6':
				return 6;
			case '7':
				return 7;
			case '8':
				return 8;
			case '9':
				return 9;
			case '0':
				return 0;
		}
		return -1;
	}

	public String multiply(String num1, String num2) {
		String result = "";
		String term1, term2;
		if (num1.length() >= num2.length()) {
			term1 = num2;
			term2 = num1;
		} else {
			term2 = num2;
			term1 = num1;
		}
		int res = 0, finalRes = 0, carry = 0;
		int t1, t2;
		// System.out.println("term1: " + term1 + ", term2: " + term2);
		for (int i = term1.length() - 1; i >= 0; --i) {
			res = 0;
			carry = 0;
			t1 = charToInt(term1.charAt(i));
			for (int j = term2.length() - 1; j >= 0; --j) {
				t2 = charToInt(term2.charAt(j));
				int prod = (t2 * t1);
				if (carry != 0) {
					prod += carry;
					carry = 0;
				}
				System.out.print("t1: " + t1 + ", t2: " + t2 + ", prod: " + prod + ", carry(before): " + carry);
				res = (int)(Math.pow(10, term2.length() - j - 1)) * (prod % 10) + res;
				carry = prod / 10;
				System.out.println(", carry(after): " + carry + '\n');
			}
			if (carry != 0) {
				res = (int)Math.pow(10, term2.length()) * carry + res;
			}
			finalRes = (int)(Math.pow(10, term1.length() - i - 1)) * res + finalRes;
			System.out.println("res:\t" + res + ", finalRes:\t" + finalRes);
		}
		result = Integer.toString(finalRes);
		return result;
	}

	public static void main(String[] args) {
		Solution obj = new Solution();
		// System.out.println(obj.multiply("2", "3"));	
		// System.out.println(obj.multiply("123", "456"));	
		// System.out.println(obj.multiply("123", "6"));
		// System.out.println(obj.multiply("123", "5"));
		// System.out.println(obj.multiply("123", "4"));
		// 12345 * 123 = 1518435  
		// System.out.println(obj.multiply("999", "999"));
		System.out.println(obj.multiply("9", "9"));


	}
}