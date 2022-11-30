# import numpy as np


# def part1(image, algo, iterations):
#     dir = {
#         (-1, 1),
#         (0, 1),
#         (1, 1),
#         (0, -1),
#         (0, 0),
#         (1, 0),
#         (-1, -1),
#         (-1, 0),
#         (1, -1),
#     }

#     newImage = []
#     border = ['.' for i in range(len(image[0]))]
#     newImage.append(border)

#     for i in range(1, len(image) - 1):
#         line = ['.']
#         for j in range(1, len(image[0]) - 1):
#             x = []
#             for d in dir:
#                 if image[j + d[1]][i + d[0]] == '.':
#                     x.append(0)
#                 else:
#                     x.append(1)
            
#             res = int("".join(str(x) for x in x), 2)
#             line.append(algo[res])

#         line.append('.')
#         newImage.append(line)
    
#     newImage.append(border)
    
#     if iterations == 0:
#         counter = 0
#         for line in newImage:
#             for num in line:
#                 if num == '#':
#                     counter += 1
        
#         return counter
    
#     return part1(newImage, algo, iterations - 1)

# def main():
#     image = []
#     with open('inputday20.txt') as file:
#         algo = file.readline().strip()
#         b = file.readline()

#         image = []
#         for line in file.readlines():
#             row = ['.']
#             for x in line.strip():
#                 row.append(x)
#             row.append('.')
#             image.append(row)
        
        
#         border = ['.' for i in range(len(image[0]))]
#         image.insert(0, border)
#         image.append(border)

#     print(part1(image, algo, 2))

# if __name__ == "__main__":
#     main()
def build_map(map, filler):
    w = len(map[0]) + 2
    new_map = []
    new_map.append([filler] * w)
    for line in map:
        new_map.append([filler] + line + [filler])
    new_map.append([filler] * w)
    return new_map


def get_neighbors(r, c, map, filler):
    bs = ""
    for rm in range(-1, 2):
        for cm in range(-1, 2):
            if r + rm < 0 or r + rm >= len(map) or c + cm < 0 or c + cm >= len(map[0]):
                bs += str(filler)
            else:
                bs += str(map[r + rm][c + cm])
    return 1 if alg[int(bs, 2)] == "#" else 0


data = open("inputday20.txt").read().strip().split("\n\n")
alg = data.pop(0)
map = [[0 if j == "." else 1 for j in i] for i in data[0].split("\n")]

for i in range(1, 50 + 1):
    # determine state of infinite pixels
    filler = 1 if alg[0] == "#" and alg[-1] == "." and not i % 2 else 0
    map = build_map(map, filler)
    # iterate over map and find updates
    changes = {}
    for r in range(len(map)):
        for c in range(len(map[0])):
            changes[(r, c)] = get_neighbors(r, c, map, filler)
    # apply updates to map
    for r, c in changes:
        map[r][c] = changes[(r, c)]
    if i == 2:
        print(f"Part 1: {sum([val for sublist in map for val in sublist])}")
print(f"Part 2: {sum([val for sublist in map for val in sublist])}")