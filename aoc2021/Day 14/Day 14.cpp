#include <iostream>
#include <math.h>
#include <cstring>
#include <vector>
#include <fstream>

class Part1
{
    public:
        void polymerization(std::vector<char> &polyTemplate, std::vector<std::string> rules);
};

void addElements(std::vector<char> &polyTemplate, std::vector<char> &element, std::vector<int>& position);
void countElements(std::vector<char> polyTemplate);

int main()
{
    std::ifstream file("inputDay14.txt");
    std::string line;

    std::vector<char> polyTemplate;
    std::vector<std::string> rules;

    getline(file, line);

    for (int i = 0; i < line.size(); i++)
    {
        polyTemplate.push_back(line[i]);
    }

    getline(file, line);

    while (getline(file, line))
    {
        rules.push_back(line);
    }
    file.close();

    Part1 solution1;

    solution1.polymerization(polyTemplate, rules);

    return 0;
}

void Part1::polymerization(std::vector<char> &polyTemplate, std::vector<std::string> rules)
{
    std::vector<int> position;
    std::vector<char> element;
    int i, j, k;
    int steps = 40;

    for (int k = 0; k < steps; k++)
    {
        for(i = 0; i < polyTemplate.size(); i++)
        {
            for (j = 0; j < rules.size(); j++)
            {
                if(polyTemplate[i] == rules[j][0] && polyTemplate[i+1] == rules[j][1])
                {
                    element.push_back(rules[j][rules[j].size()-1]);
                    position.push_back(i + 1);
                    // break;
                }
            }
        }
        addElements(polyTemplate, element, position);
    }
    countElements(polyTemplate);
}

void addElements(std::vector<char> &polyTemplate, std::vector<char> &element, std::vector<int>& position)
{
    int i, j;
    for (i = polyTemplate.size(); i >= 0; i--)
    {
        for (j = 0; j < position.size(); j++)
        {
            if (i == position[j])
            {
                // polyTemplate.push_back(element[j]);
                polyTemplate.insert(polyTemplate.begin() + i, element[j]);
            }
        }
    }
    position.clear();
    element.clear();
}


void countElements(std::vector<char> polyTemplate)
{
    bool isUnique;
    std::vector<char> uniqueElements;
    std::vector<int> elementAmount = {0,0,0,0,0,0,0,0,0,0};
    int i, j;

    uniqueElements.push_back(polyTemplate[0]);
    for(i = 1; i < polyTemplate.size(); i++)
    {
        isUnique = true;
        for(j = 0; j < uniqueElements.size(); j++)
        {
            if (polyTemplate[i] == uniqueElements[j] && i != j)
            {
                isUnique = false;
                break;
            }
        }
        if (isUnique == true)
        {
            uniqueElements.push_back(polyTemplate[i]);
        }
    }

    for ( i = 0; i < uniqueElements.size(); i++)
    {
        std::cout << uniqueElements[i] << " ";
    }

    for (i = 0; i < polyTemplate.size(); i++)
    {
        if (polyTemplate[i] == uniqueElements[0])
            elementAmount[0]++;
        
        else if(polyTemplate[i] == uniqueElements[1])
            elementAmount[1]++;

        else if(polyTemplate[i] == uniqueElements[2])
            elementAmount[2]++;

        else if(polyTemplate[i] == uniqueElements[3])
            elementAmount[3]++;

        else if(polyTemplate[i] == uniqueElements[4])
            elementAmount[4]++;

        else if(polyTemplate[i] == uniqueElements[5])
            elementAmount[5]++;

        else if(polyTemplate[i] == uniqueElements[6])
            elementAmount[6]++;

        else if(polyTemplate[i] == uniqueElements[7])
            elementAmount[7]++;

        else if(polyTemplate[i] == uniqueElements[8])
            elementAmount[8]++;

        else if(polyTemplate[i] == uniqueElements[9])
            elementAmount[9]++;
    }

    int min = elementAmount[0];
    int max = elementAmount[0];

    for (i = 0; i < elementAmount.size(); i++)
    {
        if (min > elementAmount[i])
        {
            min = elementAmount[i];
        }
        if (max < elementAmount[i])
        {
            max = elementAmount[i];
        }
    }

    int diff = max - min;

    std::cout<< "Difference between largest and smallest element amount: " << diff;

