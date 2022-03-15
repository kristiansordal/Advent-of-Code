#include <iostream>
#include <math.h>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

class Part1{
    public:
    void gammaNum(vector<string> binaryInput)
    {
        int i = 0, j = 0;
        int ones, zeros;

        int row = binaryInput.size();
        int col = binaryInput[0].size();

        int *gammaNum = new int[col]; // 5
        int *epsilonNum = new int[col]; // 5

        for (i = 0; i < col; i++)
        {
            ones = 0;
            zeros = 0;
            for (j = 0; j < row; j++)
            {
                if (binaryInput[j][i] == '1')
                {
                    ones++;
                }
                else if (binaryInput[j][i] == '0')
                {
                    zeros++;
                }
            }
            if (ones > zeros)
            {
                gammaNum[i] = 1;
            }
            else if (zeros > ones)
            {
                gammaNum[i] = 0;
            }
        }

        computeEpsilonNum(gammaNum, epsilonNum, col);

        int gamma = binaryToInteger(gammaNum, col);
        int epsilon = binaryToInteger(epsilonNum, col);
        cout << "Power consumption is: " << gamma * epsilon;
    }

    void computeEpsilonNum(int gammaNum[], int epsilonNum[], int arrSize)
    {
        for (int i = 0; i < arrSize; i++)
        {
            if (gammaNum[i] == 1)
            {
                epsilonNum[i] = 0;
            }
            else
            {
                epsilonNum[i] = 1;
            }
        }
    }

    int binaryToInteger(int num[], int arrSize)
    {
        int sum = 0;

        for (int i = 0; i < arrSize; i++)
        {
            if (num[i] == 1)
            {
                sum += pow(2, arrSize-1-i);
            }
        }
        return sum;
    }
    
};

class Part2{
    public:

    void lifeSupportRating(vector<string> binaryInput)
    {
        int i = 0, j = 0;
        int ones, zeros;
        int deletedRows;
        int co2num, o2num;

        int col = 0;
        int row = binaryInput.size();

        vector<string> binaryInput1(binaryInput.size());
        vector<string> binaryInput2(binaryInput.size());

        for (int k = 0; k < row; k++)
        {
            binaryInput1[k] = binaryInput[k];
            binaryInput2[k] = binaryInput[k];
        }
        

        int inputRow = row;
        while (inputRow != 1)
        {
            ones = 0;
            zeros = 0;

            for (i = 0; i < inputRow; i++)
            {
                if (binaryInput1[i][col] == '1')
                {
                    ones++;
                }
                else if (binaryInput1[i][col] == '0')
                {
                    zeros++;
                }
            }
            O2ScrubberRating(ones, zeros, inputRow, col, binaryInput1, deletedRows);
            inputRow -= deletedRows;
        }
        if (inputRow == 1)
        {
            o2num = stoi(binaryInput1[0], 0, 2);
            cout << o2num;
            cout << endl;
        }

        inputRow = row;
        col = 0;
        i = 0, j = 0;
        while (inputRow != 1)
        {
            ones = 0;
            zeros = 0;

            for (i = 0; i < inputRow; i++)
            {
                if (binaryInput2[i][col] == '1')
                {
                    ones++;
                }
                else if (binaryInput2[i][col] == '0')
                {
                    zeros++;
                }
            }
            C02ScrubberRating(ones, zeros, inputRow, col, binaryInput2, deletedRows);
            inputRow -= deletedRows;
        }
        if (inputRow == 1)
        {
            co2num = stoi(binaryInput2[0], 0, 2);
            cout << co2num;
            cout << endl;
        }

        int lifeSupportNumber = co2num * o2num;
        cout << endl;
        cout << "Life support number: " << lifeSupportNumber;
    }

    void O2ScrubberRating(int ones, int zeros, int row, int& col, vector<string>& binaryInput, int& deletedRows)
    {
        deletedRows = 0;

        if (ones >= zeros)
        {
            for (int i = row-1; i >= 0; i--)
            {
                if (binaryInput[i][col] == '0')
                {
                    binaryInput.erase(binaryInput.begin() + i);
                    deletedRows++;
                }
            }
        }
        if (ones < zeros)
        {
            for (int i = row-1; i >= 0; i--)
            {
                if (binaryInput[i][col] == '1')
                {
                    binaryInput.erase(binaryInput.begin() + i);
                    deletedRows++;
                }
            }
        }
        col++;
    }
    void C02ScrubberRating(int ones, int zeros, int row, int& col, vector<string>& binaryInput, int& deletedRows)
    {
        deletedRows = 0;

        if (ones >= zeros)
        {
            for (int i = row-1; i >= 0; i--)
            {
                if (binaryInput[i][col] == '1')
                {
                    binaryInput.erase(binaryInput.begin() + i);
                    deletedRows++;
                }
            }
        }
        if (ones < zeros)
        {
            for (int i = row-1; i >= 0; i--)
            {
                if (binaryInput[i][col] == '0')
                {
                    binaryInput.erase(binaryInput.begin() + i);
                    deletedRows++;
                }
            }
        }
        col++;
    }
};

int main()
{
    ifstream file("inputDay3.txt");

    vector<string> binaryInput;

    while (file.eof() == false)
    {
        string num;
        file >> num;
        binaryInput.push_back(num);
    }
    file.close();
    
    Part1 solution;
    Part2 solution2;

    solution2.lifeSupportRating(binaryInput);
    return 0;

}