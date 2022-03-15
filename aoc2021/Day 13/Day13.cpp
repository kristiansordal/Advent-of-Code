#include <iostream>
#include <math.h>
#include <string>
#include <vector>
#include <fstream>
#include <sstream>
#include <algorithm>

class Part1
{
    public:
        void foldPaper(std::vector<std::vector<int>>& dots, std::vector<int> foldLine, std::vector<char> foldDir, int& sizeX, int& sizeY);
};

int getSizeRow(std::vector<std::vector<int>>);
int getSizeX(std::vector<std::vector<int>>);
int getSizeY(std::vector<std::vector<int>>);
void printDots(std::vector<std::vector<int>>, int, int);
void sortAscending(std::vector<std::vector<int>> &dots);

int main()
{
    std::ifstream file("inputDay13.txt");
    std::vector<int> dotLine;
    std::vector<std::vector<int>> dots;
    std::vector<int> foldLine;
    std::vector<char> foldDir;
    std::string line;
    std::string num;
    std::string foldNum;
    bool fold = false;

    while(getline(file, line, '\n'))
    {
        if (line.empty())
        {
            fold = true;
        }

        if (!fold) 
        {
            std::stringstream ss(line);
            while (getline(ss, num, ','))
            {
                dotLine.push_back(stoi(num));
            }
            dots.push_back(dotLine);
            dotLine.clear();
        }

        else if (fold)
        {
            if (!line.empty())
                foldLine.push_back((line[line.size() - 1] - '0'));

            std::stringstream ss1(line);
            while(getline(ss1, num))
            {
                for (int i = 0; i < num.size(); i++)
                {
                    if (num[i] == 'x' || num[i] == 'y')
                    {
                        foldDir.push_back(num[i]);
                    }
                    
                }
                
            }
        }
    }

    Part1 solution1;

    int sizeX = getSizeX(dots);
    int sizeY = getSizeY(dots);

    solution1.foldPaper(dots, foldLine, foldDir, sizeX, sizeY);
    printDots(dots, sizeX, sizeY);
    return 0;
}


int getSizeX(std::vector<std::vector<int>> dots)
{
    int max = dots[0][0];
    for (int i = 1; i < dots.size(); i++)
    {
        if (dots[i][0] > max)
        {
            max = dots[i][0];
        }
    }
    return max+1;
}

int getSizeY(std::vector<std::vector<int>> dots)
{
    int max = dots[0][0];
    for (int i = 1; i < dots.size(); i++)
    {
        if (dots[i][1] > max)
        {
            max = dots[i][1];
        }
    }
    return max+1;
}

void Part1::foldPaper(std::vector<std::vector<int>>& dots, std::vector<int> foldLine, std::vector<char> foldDir, int& sizeX, int& sizeY)
{
    for (int i = 0; i < foldLine.size(); i++)
    {
        sortAscending(dots);
        printDots(dots, sizeX, sizeY);
        if (foldDir[i] == 'x') 
        {
            for (int j = dots.size()-1; j >= 0; j--)
            {
                if (dots[j][0] > foldLine[i])
                {
                    dots[j][0] = sizeX - dots[j][0]-1;
                    for (int k = dots.size()-1; k >= 0; k--)
                    {
                        if (dots[j][1] == dots[k][1] && dots[j][0] == dots[k][0] && k != j)
                        {
                            // dots[j].clear();
                            dots.erase(dots.begin() + j);
                        }
                        
                    }
                    
                }
            }
            sizeX = sizeX - foldLine[i]-1;
        }
        if (foldDir[i] == 'y') 
        {
            for (int j = dots.size()-1; j >= 0; j--)
            {
                if (dots[j][1] > foldLine[i])
                {
                    dots[j][1] = sizeY - dots[j][1]-1;
                    for (int k = dots.size()-1; k >= 0; k--)
                    {
                        if (dots[j][1] == dots[k][1] && dots[j][0] == dots[k][0] && k != j)
                        {
                            // dots[j].clear();
                            dots.erase(dots.begin() + j);
                        }
                        
                    }
                }
            }
            sizeY = sizeY - foldLine[i]-1;
        }
    }
    printDots(dots, sizeX, sizeY);
    
}
void printDots(std::vector<std::vector<int>> dots, int x, int y)
{
    int i, j, k, l;
    int count = 0;
    for(i = 0; i < y; i++)
    {
        for(j = 0; j < x; j++)
        {
            for (k = 0; k < dots.size(); k++)
            {
                if (dots[k][0] == j && dots[k][1] == i)
                {
                    // std::cout << "#";
                    count++;
                    j++;
                    for (l = 0; l < dots.size(); l++)
                    {
                        if (dots[l][0] == dots [k][0] +1 && dots[l][1] == dots[k][1])
                        {
                            // std::cout << "#";
                            count++;
                            // j++;
                            break;
                        }
                        
                    }
                    break;
                }
            }
            if (j == x)
                break;
            // else
                // std::cout << ".";

        }
        // std::cout << std::endl;
    }
    std::cout << "There are " << count << " visible dots." << std::endl;
}

void sortAscending(std::vector<std::vector<int>>& dots)
{
    // sort in ascending order of Y
    int tempY, tempX;
    for (int j = 0; j < dots.size(); j++)
    {
        for (int i = 1; i < dots.size(); i++)
        {
            if (dots[i][1] < dots[i-1][1])
            {
                tempY = dots[i][1];
                tempX = dots[i][0];
                dots[i][1] = dots[i - 1][1];
                dots[i][0] = dots[i - 1][0];
                dots[i - 1][1] = tempY;
                dots[i - 1][0] = tempX;
            }
        }
    }
    for (int j = 0; j < dots.size(); j++)
    {
        for (int i = 1; i < dots.size(); i++)
        {
            if (dots[i][0] < dots[i-1][0] && dots[i][1] == dots[i-1][1])
            {
                    tempX = dots[i][0];
                    dots[i][0] = dots[i - 1][0];
                    dots[i - 1][0] = tempX;
            }
        }
    }
}