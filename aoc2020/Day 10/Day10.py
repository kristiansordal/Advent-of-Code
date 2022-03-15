def part1(jolt):
    rating = 0
    oneDiff = 0
    threeDiff = 1
    for i, num in enumerate(jolt):
        for j in range(i, i+3):
            if j <= len(jolt)-1:
                if jolt[i+(i-j)] - rating == 1:
                    rating = num 
                    oneDiff += 1
                    break
                elif jolt[i+(i-j)] - rating == 2:
                    rating = num
                    break
                elif jolt[i+(i-j)] - rating == 3:
                    rating = num
                    threeDiff += 1
                    break

    print(oneDiff * threeDiff)

def part2(jolt):
    visited = {}
    node = 0
    print(dfs(jolt, node, visited))

def dfs(jolt, node, visited):
    if node == len(jolt) - 1: return 1
    if node in visited: return visited[node]

    combinations = 0
    for i in range(node + 1, len(jolt)):
        if jolt[i] - jolt[node] <= 3:
            combinations += dfs(jolt, i, visited)

    visited[node] = combinations
    return combinations



    

        
def main():
    with open('C:\dev\Advent of Code\Advent of Code 2020\Day 10\inputDay10.txt') as file:
        jolt = [int(line.strip()) for line in file]
    
    jolt.sort()
    jolt = [0] + jolt
    jolt.append(max(jolt)+3)

    part1(jolt)
    part2(jolt)

if __name__ == '__main__':
    main()