#include <iostream>
#include <math.h>
#include <string>
#include <vector>
#include <fstream>

class Part1
{
    public:
        void flashes(std::vector<std::vector<int> > energyLevel, std::vector<std::vector<bool> > hasFlashed);
};

class Part2
{
    public:
        void allFlashedAtOnce(std::vector<std::vector<int> > energyLevel, std::vector<std::vector<bool> > hasFlashed);
};

void increaseEnergy(std::vector<std::vector<int> >&, std::vector<std::pair<int, int> >);
void checkFlashes(std::vector<std::vector<int> >&, std::vector<std::vector<bool> >&, int&, std::vector<std::pair<int, int> >);
void increaseAdjacent(std::vector<std::vector<int> >&, std::vector<std::pair<int, int> >, int, int);
void printFlashes(std::vector<std::vector<bool> >);
void resetFlashes(std::vector<std::vector<bool> >&, std::vector<std::vector<int> >&);
bool checkFor10s(std::vector<std::vector<int> >, std::vector<std::vector<bool> > hasFlashed);
int checkForAllFlashes(std::vector<std::vector<int> >&, std::vector<std::vector<bool> >&, int&, std::vector<std::pair<int, int> >);
int main()
{
    // open file
    std::ifstream file("inputDay11.txt");
    std::ifstream fileSize("inputDay11.txt");

    std::string line;
    std::string num;
    std::vector<int> numLine;
    std::vector<bool> flashLine;
    std::vector<std::vector<int> > energyLevel;
    std::vector<std::vector<bool> > hasFlashed;

    getline(fileSize, line);

    for (int i = 0; i < line.size()+2; i++)
    {
        numLine.push_back(9);
        flashLine.push_back(false);
    }
    energyLevel.push_back(numLine);
    hasFlashed.push_back(flashLine);
    numLine.clear();
    flashLine.clear();

    while(getline(file, line))
    {
        numLine.push_back(9);
        flashLine.push_back(false);
        for (int i = 0; i < line.size(); i++)
        {
            numLine.push_back(line[i] - '0');
            flashLine.push_back(false);
        }
        numLine.push_back(9);
        flashLine.push_back(false);
        energyLevel.push_back(numLine);
        hasFlashed.push_back(flashLine);
        numLine.clear();
        flashLine.clear();
    }

    for (int i = 0; i < line.size()+2; i++)
    {
        numLine.push_back(9);
        flashLine.push_back(false);
    }
    energyLevel.push_back(numLine);
    hasFlashed.push_back(flashLine);
    numLine.clear();
    flashLine.clear();
    file.close();

    for(int i = 1; i < energyLevel.size()-1; i++)
    {
        for(int j = 1; j < energyLevel[0].size()-1; j++)
        {
            std::cout << energyLevel[i][j]; 
        }
        std::cout << std::endl;
    }

    Part1 solution1;
    Part2 solution2;
    // solution1.flashes(energyLevel, hasFlashed);
    solution2.allFlashedAtOnce(energyLevel, hasFlashed);

    return 0;
}

void Part1::flashes(std::vector<std::vector<int> > energyLevel, std::vector<std::vector<bool> > hasFlashed)
{
    int i, j, k;
    int totalFlashes = 0;
    int steps = 100;

    // directions
    auto dir = std::vector<std::pair<int, int> >
    {
        {1, 0},
        {0, 1},
        {1, 1},
        {0, -1},
        {-1, 0},
        {-1, -1},
        {-1, 1},
        {1, -1}
    };

    // increase energy for each step
    for (k = 1; k <= steps; k++)
    {
        std::cout << "Step: " << k << std::endl;
        std::cout << std::endl;

        // increase energy
        increaseEnergy(energyLevel, dir);

        // check for flashes
        while(checkFor10s(energyLevel, hasFlashed))
            checkFlashes(energyLevel, hasFlashed, totalFlashes, dir);
    
        //reset flashes and set values that have flashed to zero
        resetFlashes(hasFlashed, energyLevel);
    }
    std::cout << "Total flashes: " << totalFlashes;
}
void Part2::allFlashedAtOnce(std::vector<std::vector<int> > energyLevel, std::vector<std::vector<bool> > hasFlashed)
{
    int i, j, k;
    int totalFlashes = 0;
    int steps = 10000;
    int allFlashes;
    int area = (energyLevel.size() - 2) * (energyLevel[0].size() - 2);

    // directions
    auto dir = std::vector<std::pair<int, int> >
    {
        {1, 0},
        {0, 1},
        {1, 1},
        {0, -1},
        {-1, 0},
        {-1, -1},
        {-1, 1},
        {1, -1}
    };

    // increase energy for each step
    for (k = 1; k <= steps; k++)
    {
        std::cout << "Step: " << k << std::endl;
        std::cout << std::endl;

        // increase energy
        increaseEnergy(energyLevel, dir);

        // check for flashes
        while(checkFor10s(energyLevel, hasFlashed))
        {
            allFlashes = checkForAllFlashes(energyLevel, hasFlashed, totalFlashes, dir);
            if (allFlashes == area-2)
                break;
        } 
        if (allFlashes == area-2)
            break;
    
        //reset flashes and set values that have flashed to zero
        resetFlashes(hasFlashed, energyLevel);
    }
    std::cout << "All flashes happened at step: " << k;
}

void increaseEnergy(std::vector<std::vector<int> >& energyLevel, std::vector<std::pair<int, int> > dir)
{
    int i, j;
    for(i = 1; i < energyLevel.size()-1; i++)
    {
        for(j = 1; j < energyLevel[0].size()-1; j++)
        {
            ++energyLevel[i][j];
        }
    }
}
void checkFlashes(std::vector<std::vector<int> >& energyLevel, std::vector<std::vector<bool> >& hasFlashed, int& totalFlashes, std::vector<std::pair<int, int> > dir)
{
    int i, j;
    int flashes = 0;
    for(i = 1; i < energyLevel.size()-1; i++)
    {
        for(j = 1; j < energyLevel[0].size()-1; j++)
        {
            if (energyLevel[i][j] > 9 && hasFlashed[i][j] == false)
            {
                hasFlashed[i][j] = true;
                increaseAdjacent(energyLevel, dir, i, j);
            }
            if (hasFlashed[i][j] == true)
            {
                flashes++;
            }
        }
    }
    // printFlashes(hasFlashed);
    totalFlashes += flashes;
}
int checkForAllFlashes(std::vector<std::vector<int> >& energyLevel, std::vector<std::vector<bool> >& hasFlashed, int& totalFlashes, std::vector<std::pair<int, int> > dir)
{
    int i, j;
    int flashes = 0;
    for(i = 1; i < energyLevel.size()-1; i++)
    {
        for(j = 1; j < energyLevel[0].size()-1; j++)
        {
            if (energyLevel[i][j] > 9 && hasFlashed[i][j] == false)
            {
                hasFlashed[i][j] = true;
                increaseAdjacent(energyLevel, dir, i, j);
                if (hasFlashed[i][j] == true)
                {
                    ++flashes;
                }
            }
        }
    }
    return flashes;
}

void increaseAdjacent(std::vector<std::vector<int> >& energyLevel, std::vector<std::pair<int, int> > dir, int i, int j)
{
    int k;
    for (k = 0; k < dir.size(); k++)
    {
        energyLevel[i + dir[k].first][j + dir[k].second]++;
    }
}

void printFlashes(std::vector<std::vector<bool> > hasFlashed)
{
    for (int i = 1; i < hasFlashed.size()-1; i++)
    {
        for (int j = 1; j < hasFlashed[0].size()-1; j++)
        {
            if (hasFlashed[i][j] == true)
            {
                std::cout << 1;
            }
            else
            {
                std::cout << '.';
            }
        }
        std::cout << std::endl;
    }
}

void resetFlashes(std::vector<std::vector<bool> >& hasFlashed, std::vector<std::vector<int> >& energyLevel)
{
    int i, j;
    for(i = 1; i < hasFlashed.size()-1; i++)
    {
        for(j = 1; j < hasFlashed[0].size()-1; j++)
        {
            if (hasFlashed[i][j] == true)
            {
                energyLevel[i][j] = 0;
                hasFlashed[i][j] = false;
            }
        }
    }
}
bool checkFor10s(std::vector<std::vector<int> > energyLevel, std::vector<std::vector<bool> > hasFlashed)
{
    int i, j;
    bool flag = false;

    for(i = 1; i < energyLevel.size()-1; i++)
    {
        for(j = 1; j < energyLevel[0].size()-1 ; j++)
        {
            if (energyLevel[i][j] > 9 && hasFlashed[i][j] == false)
                flag = true;
        }
    }
    return flag;
}
