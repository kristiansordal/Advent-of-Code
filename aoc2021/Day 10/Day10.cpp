#include <iostream>
#include <math.h>
#include <string>
#include <vector>
#include <fstream>

class Part1
{
    public:
        void calculateSyntaxScore(std::vector<std::string> corruptedLines);
};

class Part2
{
    public:
        void discardcorruptedLines(std::vector<std::string> &navSys, std::vector<std::vector<char>> &missingCharacters);
        void findMissingCharacters(std::vector<std::string> navSys, std::vector<std::vector<char>> &missingCharacters);
        void computeAutoCompleteScore(std::vector<std::vector<char>> missingCharacters);
};

int main()
{
    // get input from file
    std::ifstream file("inputDay10.txt");
    std::string input;
    std::vector<std::string> navSys;
    std::vector<std::string> incompleteLines;
    std::vector<std::vector<char>> missingCharacters;

    while(getline(file, input))
    {
        navSys.push_back(input);
    }

    Part1 solution1;
    Part2 solution2;

    solution1.calculateSyntaxScore(navSys);
    solution2.findMissingCharacters(navSys, missingCharacters);
    solution2.computeAutoCompleteScore(missingCharacters);
    return 0;
}

void Part1::calculateSyntaxScore(std::vector<std::string> corruptedLInes)
{
    // score for different characters
    int score = 0;
    int finalScore = 0;
    int parScore = 3;
    int braScore = 57;
    int curlScore = 1197;
    int mouthScore = 25137;

    int inputSize = corruptedLInes.size();

    int i, j;
    bool exit = false;
    char c, end;
    std::vector<char> queue;

    for (i = 0; i < inputSize; i++)
    {
        exit = false;
        queue.clear();
        for (j = 0; j < corruptedLInes[i].size(); j++)
        {
            c = corruptedLInes[i][j];

            switch (c)
            {
                case '(':
                case '[':
                case '{':
                case '<':
                    queue.push_back(c);
                    break;
                case ')':
                    end = queue[queue.size()-1];

                    if (end != '(')
                    {
                        score += parScore;
                        exit = true;
                    }
                    else
                    {
                        queue.erase(queue.end() - 1, queue.end());
                    }
                    
                    break;
                case ']':
                    end = queue[queue.size()-1];

                    if (end != '[')
                    {
                        score += braScore;
                        queue.erase(queue.end() - 1, queue.end());
                        exit = true;
                    }
                    else
                    {
                        queue.erase(queue.end() - 1, queue.end());
                    }
                    break;
                case '}':
                    end = queue[queue.size() - 1];

                    if (end != '{')
                    {
                        score += curlScore;
                        queue.erase(queue.end() - 1, queue.end());
                        exit = true;
                    }
                    else
                    {
                        queue.erase(queue.end() - 1, queue.end());
                    }
                    break;
                case '>':
                    end = queue[queue.size()-1];

                    if (end != '<')
                    {
                        score += mouthScore;
                        queue.erase(queue.end() - 1, queue.end());
                        exit = true;
                    }
                    else
                    {
                        queue.erase(queue.end() - 1, queue.end());
                    }
                    break;
            }
            finalScore += score;
            score = 0;
            if (exit == true)
            {
                break;
            }
        }
    }


    std::cout << "Score is: " << finalScore << std::endl;
}

void Part2::findMissingCharacters(std::vector<std::string> navSys, std::vector<std::vector<char>> &missingCharacters)
{
    // score for different characters
    int inputSize = navSys.size();
    std::vector<char> queue;

    int i, j, k;
    bool exit = false;
    char c, end;

    for (i = navSys.size()-1; i >= 0; i--)
    {
        exit = false;
        if (!queue.empty())
        {
            missingCharacters.push_back(queue);
        }
        
        queue.clear();
        for (j = 0; j < navSys[i].size(); j++)
        {
            c = navSys[i][j];

            switch (c)
            {
                case '(':
                case '[':
                case '{':
                case '<':
                    queue.push_back(c);
                    break;
                case ')':
                    end = queue[queue.size()-1];

                    if (end != '(')
                    {
                        navSys[i].clear();
                        queue.erase(queue.end() - 1, queue.end());
                        exit = true;
                    }
                    else
                    {
                        queue.erase(queue.end() - 1, queue.end());
                    }
                    
                    break;
                case ']':
                    end = queue[queue.size()-1];

                    if (end != '[')
                    {
                        navSys[i].clear();
                        queue.erase(queue.end() - 1, queue.end());
                        exit = true;
                    }
                    else
                    {
                        queue.erase(queue.end() - 1, queue.end());
                    }
                    break;
                case '}':
                    end = queue[queue.size() - 1];

                    if (end != '{')
                    {
                        navSys[i].clear();
                        queue.erase(queue.end() - 1, queue.end());
                        exit = true;
                    }
                    else
                    {
                        queue.erase(queue.end() - 1, queue.end());
                    }
                    break;
                case '>':
                    end = queue[queue.size()-1];

                    if (end != '<')
                    {
                        navSys[i].clear();
                        queue.erase(queue.end() - 1, queue.end());
                        exit = true;
                    }
                    else
                    {
                        queue.erase(queue.end() - 1, queue.end());
                    }
                    break;
            }
            if (exit == true)
            {
                queue.clear();
                break;
            }
        }
    }
    if (!queue.empty())
    {
        missingCharacters.push_back(queue);
    }
}

void Part2::computeAutoCompleteScore(std::vector<std::vector<char>> missingCharacters)
{
    // compute score by looping through missing characters
    int i, j;
    uint64_t score = 0;
    std::vector<uint64_t> scoreList;
    for(i = 0; i < missingCharacters.size(); i++)
    {
        score = 0;
        for(j = missingCharacters[i].size()-1; j >= 0; j--)
        {
            score *= 5;
            switch(missingCharacters[i][j]) 
            {
                case '(':
                    score += 1;
                    break;
                case '[':
                    score += 2;
                    break;
                case '{':
                    score += 3;
                    break;
                case '<':
                    score += 4;
                    break;
            }
        }
        scoreList.push_back(score);
    }

    // sort score in ascending order
    for(i = 0; i < scoreList.size(); i++)
    {
        for(j = 1; j < scoreList.size(); j++)
        {
            uint64_t temp;
            if(scoreList[j] < scoreList[j-1])
            {
                temp = scoreList[j];
                scoreList[j] = scoreList[j - 1];
                scoreList[j - 1] = temp;
            }
        }
    }
    
    // print final middle score
    int middle = scoreList.size() - scoreList.size() / 2-1;
    std::cout << "Middle score is: " << scoreList[middle];
}
