#include <iostream>
#include <math.h>
#include <fstream>
#include <vector>
#include <sstream>
#include <algorithm>

using namespace std;

class Part1
{
    public:
        void getOverlap(vector<int> x1, vector<int> y1, vector<int> x2, vector<int> y2);
};

class Part2
{
    public:
        void getOverlapDiagonal(vector<int> x1, vector<int> y1, vector<int> x2, vector<int> y2);
        void printArr(int **arr, int row, int col);
};
int main()
{
    ifstream file("inputDay5.txt");

    string xyCoord;
    string num;
    string xCoords;
    string yCoords;
    vector<int> x1;
    vector<int> x2;
    vector<int> y1;
    vector<int> y2;

    int i = 1;
    while(file >> xyCoord)
    {
        stringstream ss(xyCoord);
        getline(ss, num, '-');
        if (!num.empty())
        {
            stringstream x1x2(num);
            getline(x1x2, xCoords, ',');
            getline(x1x2, yCoords, ' ');
            i++;

            if(i % 2 == 0)
            {
                x1.push_back(stoi(xCoords));
                y1.push_back(stoi(yCoords));
            }
            else
            {
                x2.push_back(stoi(xCoords));
                y2.push_back(stoi(yCoords));
            }
        }
    }

    Part1 solution;

    solution.getOverlap(x1, y1, x2, y2);

    Part2 solution2;

    solution2.getOverlapDiagonal(x1, y1, x2, y2);

    return 0;
}

void Part1::getOverlap(vector<int> x1, vector<int> y1, vector<int> x2, vector<int> y2)
{
    int i, j;
    int size = x1.size();

    // get max element in each vector
    int maxX = 0, maxY = 0;
    int maxX1 = *max_element(begin(x1), end(x1));
    int maxX2 = *max_element(begin(x2), end(x2));
    int maxY1 = *max_element(begin(y1), end(y1));
    int maxY2 = *max_element(begin(y2), end(y2));

    if (maxX1 >= maxX2)
    {
        maxX = maxX1;
    }
    else
    {
        maxX = maxX2;
    }

    if (maxY1 >= maxY2)
    {
        maxY = maxY1;
    }
    else
    {
        maxY = maxY2;
    }

    // create array filled with 0 with the size of the inputs
    int **overlapArr = new int*[maxY];

    for (i = 0; i <=maxY; i++)
    {
        overlapArr[i] = new int[maxX];
    }

    for ( i = 0; i <= maxY; i++)
    {
        for ( j = 0; j <= maxX; j++)
        {
            overlapArr[i][j] = 0;
        }
    }
    
    // add 1 to overlappoints
    int pos;
    for (i = 0; i < size +1; i++)
    {
        if (x1[i] == x2[i])
        {
            pos = x1[i];
            if (y1[i] < y2[i])
            {
                for (j = y1[i]; j <= y2[i]; j++)
                {
                    overlapArr[j][pos]++;
                }
            }
            if (y2[i] < y1[i])
            {
                for (j = y2[i]; j <= y1[i]; j++)
                {
                    overlapArr[j][pos]++;
                }
            }
        }
        else if (y1[i] == y2[i])
        {
            pos = y1[i];
            if (x1[i] < x2[i])
            {
                for (j = x1[i]; j <= x2[i]; j++)
                {
                    ++overlapArr[pos][j];
                }
            }
            if (x2[i] < x1[i])
            {
                for (j = x2[i]; j <= x1[i]; j++)
                {
                    ++overlapArr[pos][j];
                }
            }
        }
    }

    // count points where the value is over 2
    int counter = 0;

    for (i = 0; i <= maxY; i++)
    {
        for (j = 0; j <= maxX; j++)
        {
            if (overlapArr[i][j] >= 2)
            {
                counter++;
            }
        }
    }

    cout << "Points with values higher than 2: " << counter;
}


void Part2::getOverlapDiagonal(vector<int> x1, vector<int> y1, vector<int> x2, vector<int> y2)
{
    int i, j, k;
    int size = x1.size();

    // get max element in each vector
    int maxX = 0, maxY = 0;
    int maxX1 = *max_element(begin(x1), end(x1));
    int maxX2 = *max_element(begin(x2), end(x2));
    int maxY1 = *max_element(begin(y1), end(y1));
    int maxY2 = *max_element(begin(y2), end(y2));

    if (maxX1 >= maxX2)
    {
        maxX = maxX1;
    }
    else
    {
        maxX = maxX2;
    }

    if (maxY1 >= maxY2)
    {
        maxY = maxY1;
    }
    else
    {
        maxY = maxY2;
    }

    // create array filled with 0 with the size of the inputs
    int **overlapArr = new int*[maxY];

    for (i = 0; i <=maxY; i++)
    {
        overlapArr[i] = new int[maxX];
    }

    for ( i = 0; i <= maxY; i++)
    {
        for ( j = 0; j <= maxX; j++)
        {
            overlapArr[i][j] = 0;
        }
    }
    
    // add 1 to overlappoints
    int pos;
    for (i = 0; i < size +1; i++)
    {
        if (x1[i] == x2[i])
        {
            pos = x1[i];
            if (y1[i] < y2[i])
            {
                for (j = y1[i]; j <= y2[i]; j++)
                {
                    overlapArr[j][pos]++;
                }
            }
            if (y2[i] < y1[i])
            {
                for (j = y2[i]; j <= y1[i]; j++)
                {
                    overlapArr[j][pos]++;
                }
            }
        }
        else if (y1[i] == y2[i])
        {
            pos = y1[i];
            if (x1[i] < x2[i])
            {
                for (j = x1[i]; j <= x2[i]; j++)
                {
                    ++overlapArr[pos][j];
                }
            }
            if (x2[i] < x1[i])
            {
                for (j = x2[i]; j <= x1[i]; j++)
                {
                    ++overlapArr[pos][j];
                }
            }
        }
        // else if(x1[i] == y1[i] && x2[i] == y2[i])
        else if(abs((x1[i] - x2[i])) == abs((y1[i] - y2[i])))
        {
            if (y1[i] >= y2[i] && x1[i] >= x2[i])
            {
                k = x2[i];
                j = y2[i];

                while (k <= x1[i] && j <= y1[i])
                {
                    overlapArr[j][k]++;
                    k++;
                    j++;
                }
                
            }
            else if (y2[i] >= y1[i] && x2[i] >= x1[i])
            {
                k = x1[i];
                j = y1[i];

                while(k <= x2[i] && j <= y2[i])
                {
                    overlapArr[j][k]++;
                    k++;
                    j++;
                }
            }
            else if (y2[i] >= y1[i] && x2[i] <= x1[i])
            {
                k = x1[i];
                j = y1[i];

                while(k >= x2[i] && j <= y2[i])
                {
                    overlapArr[j][k]++;
                    k--;
                    j++;
                }
            }
            else if (y2[i] <= y1[i] && x2[i] >= x1[i])
            {
                k = x1[i];
                j = y1[i];

                while(k <= x2[i] && j >= y2[i])
                {
                    overlapArr[j][k]++;
                    k++;
                    j--;
                }
            }
        }
        // else if(y1[i] != y2[i])
        // {

        // }
    }

    // count points where the value is over 2
    int counter = 0;

    for (i = 0; i <= maxY; i++)
    {
        for (j = 0; j <= maxX; j++)
        {
            if (overlapArr[i][j] >= 2)
            {
                counter++;
            }
        }
    }
    printArr(overlapArr, maxY, maxX);
    cout << "Points with values higher than 2: " << counter;
}

void Part2::printArr(int **arr, int row, int col)
{
    for (int i = 0; i <= row; i++)
    {
        for (int j = 0; j <=col; j++)
        {
            if (arr[i][j] == 0)
            {
                cout << '.';
            }
            else
            {
                cout << arr[i][j];
            }
        }
        cout << endl;
    }
    cout << endl;
}