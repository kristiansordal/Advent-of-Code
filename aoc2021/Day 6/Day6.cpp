#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <math.h>
using namespace std;

class Part1
{
    public:
        // function declaration
        void populationGrowth(vector<int> lanternFish);
};

class Part2
{
    public:
        void populationGrowthV2(vector<int> lanternFish);
};
int main()
{
    //get input from textfile   
    ifstream file("inputDay6.txt");
    string num;

    vector<int> lanternFish;

    while (getline(file, num, ','))
    {
        lanternFish.push_back(stoi(num));
    }

    Part1 solution1;
    Part2 solution2;

    // solution1.populationGrowth(lanternFish);
    solution2.populationGrowthV2(lanternFish);
    return 0;
}

// function definition

void Part1::populationGrowth(vector<int> lanternFish)
{
    int days = 256;
    uint64_t size = lanternFish.size();
    int i, j, populationCounter = 0;

    // reduce timer by 1 for each iteration of loop
    for (i = 0; i < days; i++)
    {
        for (j = 0; j < size; j++)
        {
            // if timer reaches 0, add new 8 at the back of vector, reset 0 to 6
            if(lanternFish[j] == 0)
            {
                lanternFish.push_back(8);
                lanternFish[j] = 6;
                continue;
            }
            lanternFish[j]--;

        }
        // new lanternfish does not start counting down until next day
        size = lanternFish.size();
    }

    cout << "Size of population after 80 days: " << size;
}

void Part2::populationGrowthV2(vector<int>lanternFish)
{
    uint64_t arr[] = {0, 0, 0, 0, 0, 0, 0, 0, 0};
    int days = 256;

    for (int i = 0; i < lanternFish.size(); i++)
    {
        if(lanternFish[i] == 0) 
            arr[0] += 1;
        else if(lanternFish[i] == 1)
            arr[1] += 1;
        else if(lanternFish[i] == 2)
            arr[2] += 1;
        else if(lanternFish[i] == 3)
            arr[3] += 1;
        else if(lanternFish[i] == 4)
            arr[4] += 1;
        else if(lanternFish[i] == 5)
            arr[5] += 1;
        else if(lanternFish[i] == 6)
            arr[6] += 1;
        else if(lanternFish[i] == 7)
            arr[7] += 1;
        else if(lanternFish[i] == 8)
            arr[8] += 1;
    }

    uint64_t resetFish;
    uint64_t newFish;

    for (int i = 0; i < days; i++)
    {
        for (int j = 0; j < 9; j++)
        {
            if(j == 0)
            {
                newFish = arr[j];
                resetFish = arr[j];
                arr[j] = arr[j + 1];
            }
            else if(j < 8 && j != 0)
                arr[j] = arr[j + 1];

        }
        arr[6] += resetFish;
        arr[8] = newFish;
    }

    uint64_t sum = 0;
    for (int i = 0; i < 9; i++)
    {
        sum += arr[i];
    }

    cout << sum;
}