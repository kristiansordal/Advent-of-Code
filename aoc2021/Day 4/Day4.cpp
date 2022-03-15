#include <iostream>
#include <math.h>
#include <fstream>
#include <vector>
#include <sstream>

using namespace std;

void part1(vector<int> bingoNum, vector<vector<vector<int>>> boards)
{
    // compare first entry of bingonum to all boards and check for matches

    int amountOfRandNums = bingoNum.size();
    int boardsAmount = boards.size();
    int row = 5;
    int col = 5;
    int guess;
    int winnerBoard;

    int i, j, k, l;
    int winnerRow = 0;
    for (i = 0; i < bingoNum.size(); i++)
    {
        guess = bingoNum[i];
        cout << "Guess is: " << guess << '\n';

        for (j = 0; j < boardsAmount; j++)
        {
            for (int k = 0; k < row; k++)
            {
                for (l = 0; l < col; l++)
                {
                    if (guess == boards[j][k][l]) 
                    {
                        boards[j][k][l] = -1;
                    }
                }
            }
        }
        if (i > 4)
        {
            for (j = 0; j < boardsAmount; j++)
            {
                for (int k = 0; k < row; k++)
                {
                    for (l = 0; l < col; l++)
                    {
                        if (boards[j][k][l] == -1) 
                        {
                            winnerRow++;
                        }
                        if(winnerRow == 5)
                        {
                            cout << "We have a winner at " << j;
                            winnerBoard = j;
                            break;
                        }
                    }
                    if (winnerRow == 5)
                    {
                        break;
                    }
                    else
                    {
                        winnerRow = 0;
                    }
                }
                if (winnerRow == 5)
                {
                    break;
                }
            }
            if (winnerRow == 5)
            {
                break;
            }
            for (j = 0; j < boardsAmount; j++)
            {
                for (int l = 0; l < col; l++)
                {
                    for (k = 0; k < row; k++)
                    {
                        if (boards[j][k][l] == -1) 
                        {
                            winnerRow++;
                        }
                        if(winnerRow == 5)
                        {
                            cout << "We have a winner at " << j;
                            winnerBoard = j;
                            break;
                        }
                    }
                    if (winnerRow == 5)
                    {
                        break;
                    }
                    else
                    {
                        winnerRow = 0;
                    }
                }
                if (winnerRow == 5)
                {
                    break;
                }
            }
            if (winnerRow == 5)
            {
                break;
            }
        }
    }

    int sum = 0;
    int finalScore;
    for (int k = 0; k < row; k++)
    {
        for (l = 0; l < col; l++)
        {
            if (boards[winnerBoard][k][l] != -1)
            {
                sum += boards[winnerBoard][k][l];
            }
        }
    }

    finalScore = guess * sum;

    cout << "Final score is: " << finalScore;
}

void part2(vector<int> bingoNum, vector<vector<vector<int>>> boards)
{
    // compare first entry of bingonum to all boards and check for matches

    int amountOfRandNums = bingoNum.size();
    int boardsAmount = boards.size();
    int row = 5;
    int col = 5;
    int guess;
    int winnerBoard;
    bool isDuplicate;
    int guessAtInsert;

    int i, j, k, l;
    int winnerRow = 0;
    vector<int> hasBoardWon;

    for (i = 0; i < amountOfRandNums; i++)
    {
        guess = bingoNum[i];
        cout << "Guess is: " << guess << '\n';

        for (j = 0; j < boardsAmount; j++)
        {
            for (int k = 0; k < row; k++)
            {
                for (l = 0; l < col; l++)
                {
                    if (guess == boards[j][k][l]) 
                    {
                        boards[j][k][l] = -1;
                    }
                }
            }
        }
        if (i > 4)
        {
            for (j = 0; j < boardsAmount; j++)
            {
                for (int k = 0; k < row; k++)
                {
                    for (l = 0; l < col; l++)
                    {
                        if (boards[j][k][l] == -1) 
                        {
                            winnerRow++;
                        }
                        if(winnerRow == 5)
                        {
                            if(hasBoardWon.size() != 0)
                            {
                                isDuplicate = false;
                                for (int a = 0; a < hasBoardWon.size(); a++)
                                {
                                    if (j == hasBoardWon[a])
                                    {
                                        cout << "Boards size: " << boards.size() << endl;
                                        cout << "Has board won size: " << hasBoardWon.size() << endl;
                                        isDuplicate = true;
                                        break;
                                    }
                                }
                            }
                            else if (hasBoardWon.size() == 0)
                            {
                                cout << "inserting " << j << endl;
                                hasBoardWon.push_back(j);
                                guessAtInsert = guess;
                                isDuplicate = true;
                            }
                            if(isDuplicate == false)
                            {
                                cout << "inserting " << j << endl;
                                hasBoardWon.push_back(j);
                                guessAtInsert = guess;
                            }
                            if (hasBoardWon.size() == boards.size())
                            {
                                break;
                            }
                        }
                        if (hasBoardWon.size() == boards.size())
                        {
                            break;
                        }
                    }
                    if (hasBoardWon.size() == boards.size())
                    {
                        break;
                    }
                    else
                    {
                        winnerRow = 0;
                    }
                }
                if (hasBoardWon.size() == boards.size())
                {
                    break;
                }
            }
            if (hasBoardWon.size() == boards.size())
            {
                break;
            }
            for (j = 0; j < boardsAmount; j++)
            {
                for (int l = 0; l < col; l++)
                {
                    for (k = 0; k < row; k++)
                    {
                        if (boards[j][k][l] == -1) 
                        {
                            winnerRow++;
                        }
                        if(winnerRow == 5)
                        {
                            if(hasBoardWon.size() != 0)
                            {
                                isDuplicate = false;
                                for (int a = 0; a < hasBoardWon.size(); a++)
                                {
                                    if (j == hasBoardWon[a])
                                    {
                                        isDuplicate = true;
                                        break;
                                    }
                                }
                            }
                            else if (hasBoardWon.size() == 0)
                            {
                                cout << "inserting " << j << endl;
                                hasBoardWon.push_back(j);
                                guessAtInsert = guess;
                                isDuplicate = true;
                            }
                            if(isDuplicate == false)
                            {
                                cout << "inserting " << j << endl;
                                hasBoardWon.push_back(j);
                                guessAtInsert = guess;
                            }
                            if (hasBoardWon.size() == boards.size())
                            {
                                break;
                            }
                        }
                        if (hasBoardWon.size() == boards.size())
                        {
                            break;
                        }
                    }
                    if (hasBoardWon.size() == boards.size())
                    {
                        break;
                    }
                    else
                    {
                        winnerRow = 0;
                    }
                }
                if (hasBoardWon.size() == boards.size())
                {
                    break;
                }
            }
            if (hasBoardWon.size() == boards.size())
            {
                break;
            }
        }
    }

    int sum = 0;
    int finalScore;
    winnerBoard = hasBoardWon[hasBoardWon.size()-1];
    cout << endl;
    for (int k = 0; k < row; k++)
    {
        for (l = 0; l < col; l++)
        {
            if (boards[winnerBoard][k][l] != -1)
            {
                sum += boards[winnerBoard][k][l];
            }
        }
    }

    finalScore = guessAtInsert * sum;
    cout << guessAtInsert;
    cout << "Final score is: " << finalScore;
}


int main()
{
    // open file
    ifstream file("inputDay4.txt");

    // bingo numbers and bingoboard
    vector<int> bingoNum;
    vector<vector<int>> bingoBoard;
    vector<vector<vector<int>>> boards;
    string line;
    int fileSize = 0;

    // insert random numbers into bingoNum
    while (file >> line)
    {
        ++fileSize;
        if (fileSize == 1)
        {
            string buffer;
            stringstream ss(line);
            
            while(getline(ss, buffer, ','))
            {
                bingoNum.push_back(stoi(buffer));
            }
            break;
        }
    }

    int lineNumber = 0;
    // make bingo boards
    while(getline(file, line))
    {
        ++lineNumber;
        int boardNum;
        stringstream ss(line);
        vector<int> boardLine;

        while(ss >> boardNum)
        {
            boardLine.push_back(boardNum);
        }
        if (!line.empty())
        {
            bingoBoard.push_back(boardLine);
            boardLine.clear();
        }
        else if(lineNumber > 2 && (line.empty() || file.eof()))
        {
            boards.push_back(bingoBoard);
            bingoBoard.clear();
        }
    }
    // push final bingoBoards into boards
    boards.push_back(bingoBoard);
    file.close();

    // part1(bingoNum, boards);
    part2(bingoNum, boards);
    return 0;
}