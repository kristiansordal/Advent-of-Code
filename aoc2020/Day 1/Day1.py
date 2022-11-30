from re import A


def main():
    with open('C:\dev\Advent of Code\Advent of Code 2020\Day 1\inputDay1.txt') as file:
        # input = file.read().splitlines()
        input = [int(line.strip()) for line in file]

    # flag = False
    # for i in input:
    #     for j in input:
    #         for k in input:
    #             if int(i)+int(j)+int(k) == 2020:
    #                 ans = int(i)*int(j)*int(k)
    #                 flag = True 
    #                 break
    #     if flag:
    #         break

    ans = [[[k for k in input if k + j + i == 2020] for j in input] for i in input]

    print(ans)
    
    
    print("Answer is: ", ans)
if __name__ == "__main__":
    main()