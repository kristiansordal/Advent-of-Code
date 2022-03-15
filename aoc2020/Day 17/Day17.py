import numpy as np
def main():
    # with open('C:\dev\Advent of Code\Advent of Code 2020\Day 17\inputDay17.txt') as file:

    arr1 = np.full((3,2), 2)
    arr2 = np.ones((2,3))

    arr3 = np.matmul(arr1, arr2)

    print(arr3)
if __name__ == '__main__':
    main()