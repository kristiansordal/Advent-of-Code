#include <iostream>
#include <math.h>
#include <string>
#include <vector>
#include <fstream>
#include <sstream> 

class Part1
{
    public:
        void getPaths(std::vector<std::string> caveMap, std::vector<std::string> caves);
};


int main()
{
    std::ifstream file1("inputDay12.txt");
    std::ifstream file2("inputDay12.txt");
    std::string line;
    std::string stream;
    std::vector<std::string> caveMap;
    std::vector<std::string> caves;

    // get cavemap
    while(getline(file1, line))
    {
        caveMap.push_back(line);
    }
    file1.close();

    // get all unique caves
    while(getline(file2, line, '-'))
    {
        bool isUnique = true;

        std::stringstream ss(line);
        getline(ss, stream, '\n');

        for (int i = 0; i < caves.size(); i++)
        {
            if (stream == caves[i])
            {
                isUnique = false;
            }
        }
        if (isUnique)
        {
            caves.push_back(stream);
        }
    }
    file2.close();


    // for (int i = 0; i < caves.size(); i++)
    // {
    //     std::cout << caves[i] << std::endl;
    // }
    // for (int i = 0; i < caveMap.size(); i++)
    // {
    //     std::cout << caveMap[i] << std::endl;
    // }
    
    return 0;
}

void Part1::getPaths(std::vector<std::string> caveMap, std::vector<std::string> caves)
{

}

