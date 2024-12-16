#include <vector>
#include <iostream>
using namespace std;
class Solution
{
public:
    vector<string> result;
    vector<string> letterCombinations(string digits)
    {
        result.clear();
        if (digits.size() == 0)
        {
            return result;
        }
        getCombinations(digits, 0, "");
        return result;
    }

private:
    const string letterMap[10] = {
        "",     // 0
        "",     // 1
        "abc",  // 2
        "def",  // 3
        "ghi",  // 4
        "jkl",  // 5
        "mno",  // 6
        "pqrs", // 7
        "tuv",  // 8
        "wxyz", // 9
    };

    void getCombinations(string digits, int index, string s)
    {
        if (index==digits.size())
        {
            result.push_back(s);
            return;
        }

        int digit=digits[index]-'0';
        string letters=letterMap[digit];
        for(int i=0;i<letters.size();i++)
        {
            getCombinations(digits,index+1,s+letters[i]);
        }

    }
};

int main()
{
    string digits = "23"; // 示例输入
    Solution solution;
    solution.letterCombinations(digits);
}