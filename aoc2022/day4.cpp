#include <bits/stdc++.h>

#include <fstream>
#include <regex>

int main() {
    std::ifstream f("input/day4.in");
    std::vector<std::vector<int>> v;
    std::regex p("\\d+");
    std::string l;

    while (getline(f, l)) {
        std::sregex_iterator iter(l.begin(), l.end(), p);
        std::sregex_iterator end;
        std::vector<int> line;

        while (iter != end) {
            line.push_back(std::stoi(iter->str()));
            ++iter;
        }
        v.push_back(line);
    }

    int p1 = std::count_if(v.begin(), v.end(), [](const auto& n) {
        return ((n[0] <= n[2] && n[1] >= n[3]) ||
                (n[0] >= n[2] && n[1] <= n[3]));
    });

    int p2 = std::count_if(v.begin(), v.end(), [](const auto& n) {
        return ((n[1] >= n[2]) && (n[3] >= n[0]));
    });

    std::cout << "Part 1: " << p1 << std::endl;
    std::cout << "Part 2: " << p2 << std::endl;

    return 0;
}
