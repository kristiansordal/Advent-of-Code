#include <iostream>
#include <vector>
#include <fstream>
//#include "../Advent of Code 2021/inputDay1.txt"

using namespace std;

class Solution {
    public:

    int isDepthIncreased(vector<int> vec)
    {
        int counter = 0;
        vector<int> subVec;

        for (int i = 2; i < vec.size(); i++)
        {
            subVec.push_back(vec[i - 2] + vec[i - 1] + vec[i]);
        }
        cout << subVec.size() << endl;  
        for (int i = 0; i < subVec.size(); i++)
        {
            if (subVec[i] > subVec[i-1])
            {
                ++counter;
            }
        }
        return counter;
    }
};


int main()
{
    ifstream file("inputDay1.txt");

    vector<int> sweep;

    while (file.eof() == false)
    {
        int next;
        file >> next;
        sweep.push_back(next);
    }
    file.close();

    Solution solution;

    int sum = solution.isDepthIncreased(sweep);
    cout << sum;
    return 0;
}
