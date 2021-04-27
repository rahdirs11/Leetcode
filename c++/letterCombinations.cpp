#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Solution {
private:
    string getLetters(char number) {
        switch(number) {
            case '2':
                return  "abc";
            case '3':
                return "def";
            case '4':
                return "ghi";
            case '5':
                return "jkl";
            case '6':
                return "mno";
            case '7':
                return "pqrs";
            case '8':
                return "tuv";
            case '9':
                return "wxyz";
        }
        return "";
    }
public:
    vector<string> letterCombinations(string digits) {
        if (digits.length() > 4 || digits.length() < 0) {
            return vector<string>();
        }
        if (digits.size() == 0) {
            vector<string> returnValue{""};
            return returnValue;
        }
        
        string remainingDigits = digits.substr(1);
        vector<string> nextResult = letterCombinations(remainingDigits);        

        char currentValue = digits[0];
        string letters = getLetters(currentValue);
        cout << "Letters:\t" << letters << endl;
        vector<string> currentResult;
        for (unsigned int i{}; i < letters.size(); ++i) {
            for (auto r: nextResult) {
                currentResult.push_back(letters[i] + r);
            }
        }
        return currentResult;
    }
};

int main() {
    string digits{""};
    cin >> digits;
    for (auto combination: Solution().letterCombinations(digits)) {
        cout << combination << " ";
    }
    cout << endl;
    return 0;
}