#include <iostream>
#include <math.h>
#include <string>
#include <vector>
#include <fstream>
#include <sstream>
#include <bits/stdc++.h>

class Part1 {
public:
    void dijkstra(std::vector<std::vector<int>> riskMap, std::vector<std::vector<bool>>& isVisited, std::vector<std::vector<int>>& minDist);
};

int main() {
    std::ifstream file("inputDay15.txt");

    std::string line;
    std::string num;
    std::vector<std::vector<int>> riskMap;
    std::vector<std::vector<bool>> isVisited;
    std::vector<std::vector<int>> minDist;

    while (getline(file, line)) {
        std::stringstream ss(line);
        std::vector<int> riskLine;
        std::vector<int> costLine;
        std::vector<bool> isVisitedLine;
        getline(ss, num);
        for (int i = 0; i < num.size(); i++) {
            riskLine.push_back(num[i] - '0');
            isVisitedLine.push_back(false);
            costLine.push_back(1000000);
        }

        riskMap.push_back(riskLine);
        isVisited.push_back(isVisitedLine);
        minDist.push_back(costLine);
    }
    file.close();
    minDist[0][0] = 0;

    // for (auto&& line : riskMap) {
    //     for (auto&& i : line) {
    //         std::cout << i;
    //     }
    // }

    Part1 solutiuon;

    solutiuon.dijkstra(riskMap, isVisited, minDist);

    return 0;
}

void Part1::dijkstra(std::vector<std::vector<int>> riskMap, std::vector<std::vector<bool>>& isVisited, std::vector<std::vector<int>>& minDist) {
    int h = riskMap.size();
    int w = riskMap[0].size();

    std::pair<int, int> start(0, 0);
    // std::vector<std::pair<int, std::pair<int, int>>> queue;
    // std::priority_queue<int, std::pair<int, int>> queue;
    // queue.push(0, (start));
    std::priority_queue<int, int> queue;
    queue.push(0, 0);


    // while (queue) {
    //     distance = queue.pop
    // }




}
