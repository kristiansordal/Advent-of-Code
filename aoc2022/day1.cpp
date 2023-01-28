#include <bits/stdc++.h>

#include <fstream>

auto sortSums(std::vector<std::vector<int>> v, std::vector<int>& sums) {
    sums.resize(v.size());
    std::transform(v.begin(), v.end(), sums.begin(),
                   [](const std::vector<int>& i) {
                       return std::accumulate(i.begin(), i.end(), 0);
                   });
    return std::sort(sums.begin(), sums.end(), std::greater<int>());
}

int main() {
    std::ifstream f("input/day1.in");
    std::vector<std::vector<int>> v;
    std::vector<int> line;
    std::string l;

    while (getline(f, l)) {
        if (l.empty()) {
            v.push_back(line);
            line.clear();
        } else {
            line.push_back(std::stoi(l));
        }
    }

    std::vector<int> sums;
    sortSums(v, sums);
    auto max = sums[0];
    auto max3 = std::accumulate(sums.begin(), sums.begin() + 3, 0);
    std::cout << "Part 1: " << max << std::endl;
    std::cout << "Part 2: " << max3 << std::endl;
}
