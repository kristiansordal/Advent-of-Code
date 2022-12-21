infile = open('input/day21.in', 'r', newline='')
lines = [line.rstrip('\n') for line in infile] 
while 'root' not in locals():
    for line in lines: 
        variable, operation = line.split(':') 
        try: 
            locals()[variable] = eval(operation) 
        except NameError: 
            pass; #variable is not defined yet 
print(f'root is: {root}')
# def main():
#     with open('input/day21.in') as f:
#         monke = [l.strip() for l in f]
#     while 'root' not in locals():
#         for m in monke:
#             var, op = m.split(':')
#             try:
#                 locals()[var] = eval(op)
#             except NameError:
#               print('An exception occurred')    
#         print(f'root is : {locals()[root]}')
#         # monke = [(l.strip().split(':')[0], l.strip().split(':')[1][1:]) for l in f.readlines()]
# #     monkeMap = {}
# #     for m in monke:
# #         try: 
# #             monkeMap[m[0]] = int(m[1])
# #         except:
# #             monkeMap[m[0]] = m[1]
# #     part1(monkeMap)
    
# #     # print(int('asef'))
# #     # try

# if __name__ == '__main__':
#     main()