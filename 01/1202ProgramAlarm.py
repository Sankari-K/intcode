import copy

BEHAVIOUR = {
    1: lambda x: x[0] + x[1],
    2: lambda x: x[0] * x[1]
}

def get_program(directory):
    with open(directory) as file:
        return list(map(int, file.read().split(",")))

def modify_program(PROGRAM, noun, verb):
    MODIFIED_PROGRAM = copy.deepcopy(PROGRAM)
    MODIFIED_PROGRAM[1] = noun
    MODIFIED_PROGRAM[2] = verb
    return MODIFIED_PROGRAM

def run_program(PROGRAM):
    for index, opcode in enumerate(PROGRAM[::4]):
        if opcode == 99:
            return PROGRAM[0]
        a_address, b_address, c_address = PROGRAM[4 * index + 1], PROGRAM[4 * index + 2], PROGRAM[4 * index + 3]
        PROGRAM[c_address] = BEHAVIOUR[opcode]((PROGRAM[a_address], PROGRAM[b_address]))
    return PROGRAM[0]

def complete_gravity_assist(PROGRAM, REQD_OUTPUT):
    for noun in range(100):
        for verb in range(100):
            ans = run_program(modify_program(PROGRAM, noun, verb))
            if ans == REQD_OUTPUT:
                return 100 * noun + verb

PROGRAM = get_program("input.txt")

# part a
modified_program = modify_program(copy.deepcopy(PROGRAM), 12, 2)
print(run_program(modified_program))

# part b
print(complete_gravity_assist(PROGRAM, 19690720))
