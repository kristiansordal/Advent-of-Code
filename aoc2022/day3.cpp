#include <bits/stdc++.h>

#include <fstream>
#include <string>

auto commonHalf(std::vector<std::string> s) {
    std::vector<int> prio;
    for (auto str : s) {
        std::string fst = str.substr(0, str.length() / 2);
        std::string snd = str.substr(str.length() / 2, str.length());
        std::set<char> fstSet(fst.begin(), fst.end());
        std::set<char> sndSet(snd.begin(), snd.end());
        std::set<char> i;
        std::set_intersection(fstSet.begin(), fstSet.end(), sndSet.begin(),
                              sndSet.end(), std::inserter(i, i.begin()));

        auto it = std::find_if(i.begin(), i.end(), [](char c) {
            return (c >= 'A' && c <= 'Z') || (c >= 'a' && c <= 'z');
        });

        if (std::islower(*it)) {
            prio.push_back(*it - 'a' + 1);
        } else if (std::isupper(*it)) {
            prio.push_back(*it - 'A' + 27);
        }
    }
    return std::accumulate(prio.begin(), prio.end(), 0);
}

auto chunksOf(std::vector<std::string> l, int n) {
    std::vector<std::vector<std::string>> chunks;
    std::vector<std::string> chunk;
    int c = 0;

    for (auto s : l) {
        if (c == n - 1) {
            chunk.push_back(s);
            chunks.push_back(chunk);
            chunk.clear();
            c = 0;
        } else {
            chunk.push_back(s);
            c++;
        }
    }
    return chunks;
}

auto commonThree(std::vector<std::string> s) {
    std::vector<std::vector<std::string>> chunks = chunksOf(s, 3);
    std::vector<int> prio;

    for (auto chunk : chunks) {
        std::set<char> s1(chunk[0].begin(), chunk[0].end());
        std::set<char> s2(chunk[1].begin(), chunk[1].end());
        std::set<char> s3(chunk[2].begin(), chunk[2].end());
        std::set<char> i1;
        std::set_intersection(s1.begin(), s1.end(), s2.begin(), s2.end(),
                              std::inserter(i1, i1.begin()));
        std::set<char> i2;
        std::set_intersection(i1.begin(), i1.end(), s3.begin(), s3.end(),
                              std::inserter(i2, i2.begin()));

        auto it = std::find_if(i2.begin(), i2.end(), [](char c) {
            return (c >= 'A' && c <= 'Z') || (c >= 'a' && c <= 'z');
        });

        if (std::islower(*it)) {
            prio.push_back(*it - 'a' + 1);
        } else if (std::isupper(*it)) {
            prio.push_back(*it - 'A' + 27);
        }
    }
    return std::accumulate(prio.begin(), prio.end(), 0);
}

int main() {
    std::fstream f("input/day3.in");
    std::string l;
    std::vector<int> prio;
    std::vector<std::string> s;
    while (getline(f, l)) {
        s.push_back(l);
    }

    int sum1 = commonHalf(s);
    int sum2 = commonThree(s);
    std::cout << "Part 1: " << sum1 << std::endl;
    std::cout << "Part 2: " << sum2 << std::endl;

    return 0;
}
