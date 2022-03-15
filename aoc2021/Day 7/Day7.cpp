#include <iostream>
#include <math.h>
#include <vector>
#include <string>
#include <fstream>
#include <algorithm>
using namespace std;

class Part1
{
    public:
        void leastFuelSpent(vector<int> crabPos);
};

class Part2
{
    public:
        void leastFuelSpentV2(vector<int> crabPos);
};

int main()
{
    //get input from textfile   
    ifstream file("inputDay7.txt");
    string num;

    vector<int> crabPos;

    while (getline(file, num, ','))
    {
        crabPos.push_back(stoi(num));
    }


    Part1 solution1;
    Part2 solution2;
    solution1.leastFuelSpent(crabPos);
    solution2.leastFuelSpentV2(crabPos);
    return 0;
}

void Part1::leastFuelSpent(vector<int> crabPos)
{
    vector<int> fuelSpent;
    int fuel;
    int size = crabPos.size();
    int i, j;

    int maxPos = *max_element(begin(crabPos), end(crabPos));

    for (i = 1; i <= maxPos; i++)
    {
        fuel = 0;
        for (j = 0; j < size; j++)
        {
            fuel += abs(crabPos[j] - i);
        }
        fuelSpent.push_back(fuel);
    }

    int minFuel = *min_element(begin(fuelSpent), end(fuelSpent));

    cout << "Minimum fuel: " << minFuel;
}

void Part2::leastFuelSpentV2(vector<int> crabPos)
{
    vector<int> fuelSpent;
    int fuel, steps;
    int size = crabPos.size();
    int i, j, k;

    int maxPos = *max_element(begin(crabPos), end(crabPos));

    for (i = 1; i <= maxPos; i++)
    {
        fuel = 0;
        for (j = 0; j < size; j++)
        {
            steps = abs(crabPos[j] - i);
            for (k = 1; k <= steps; k++)
            {
                fuel += k;
            }
            
        }
        fuelSpent.push_back(fuel);
    }

    int minFuel = *min_element(begin(fuelSpent), end(fuelSpent));

    cout << "Minimum fuel: " << minFuel;
}
