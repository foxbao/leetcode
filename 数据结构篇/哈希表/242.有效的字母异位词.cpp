#include <vector>
#include <iostream>
#include <unordered_map>
using namespace std;
class Solution
{
public:
    bool isAnagram(string s, string t)
    {
        if (s.size() != t.size())
        {
            return false;
        }
        unordered_map<char,int>charCount;
        for(char c:s)
        {
            charCount[c]++;
        }
        for(char c:t)
        {
            if(charCount.find(c) == charCount.end() || charCount[c] == 0)
            {
                return false;
            }
            charCount[c]--;

        }
        return true;
    }

private:
};

int main()
{

    string s = "anagram"; // 示例输入 1
    string t = "nagaram";
    Solution solution;
    if (solution.isAnagram(s, t))
    {
        cout << "\"" << t << "\" is an anagram of \"" << s << "\"." << endl;
    }
    else
    {
        cout << "\"" << t << "\" is NOT an anagram of \"" << s << "\"." << endl;
    }

    return 0;
}