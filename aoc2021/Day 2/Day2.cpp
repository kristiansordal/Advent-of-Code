#include <iostream>
#include <vector>
#include <fstream>
#include <string>
using namespace std;

class Solution {
    public:

    void finalPosition(vector<string> position, vector<int> amount) 
    {
        int horizontal = 0;
        int vertical = 0;
        int aim = 0;

        for (int i = 0; i < position.size(); i++)
        {
            if (position[i] == "forward")
            {
                horizontal += amount[i];
                vertical += aim * amount[i];
            }
            else if (position[i] == "down")
            {
                aim += amount[i];
            }
            else if (position[i] == "up")
            {
                aim -= amount[i];
            }
        }
        int sum = horizontal * vertical;
        cout << "The sum when you multiply is : " << sum;
    }
};
int main()
{
    ifstream file("inputDay2.txt");

    vector<string> positions;
    vector<int> amounts;

    while (file.eof() == false)
    {
        string position;
        int amount;

        file >> position;
        file >> amount;

        positions.push_back(position);
        amounts.push_back(amount);
        }
    file.close();

    
    Solution solution;

    solution.finalPosition(positions, amounts);
    return 0;
}