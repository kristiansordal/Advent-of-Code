# class OpCode:
#     def __init__(self, op, x, y, out):
#         self.op = op
#         self.x = x
#         self.y = y
#         self.out = out


class IntCode:
    def __init__(self, S):
        self.program = S
        self.size = len(S)
        self.ptr = 0
        self.op = -1

    def execute(self, noun, verb):
        self.program[0] = noun
        self.program[1] = verb
        while self.ptr < self.size:
            self.op = self.program[self.ptr]

            if self.op == 99:
                return self.program[0]

            param1 = self.program[self.ptr + 1]
            param2 = self.program[self.ptr + 2]
            mem_out = self.program[self.ptr + 3]

            if self.op == 1:
                self.add(param1, param2, mem_out)
            elif self.op == 2:
                self.mult(param1, param2, mem_out)
            self.ptr += 4

    def add(self, param1, param2, mem_out):
        x = self.program[param1]
        y = self.program[param2]
        self.program[mem_out] = x + y

    def mult(self, param1, param2, mem_out):
        x = self.program[param1]
        y = self.program[param2]
        self.program[mem_out] = x * y
