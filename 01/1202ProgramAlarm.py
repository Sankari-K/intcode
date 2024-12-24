import copy

BEHAVIOUR = {
    1: lambda x: x[0] + x[1],
    2: lambda x: x[0] * x[1]
}

def get_program(directory):
    with open(directory) as file:
        return list(map(int, file.read().split(",")))

def get_program_copy(PROGRAM):
    return copy.deepcopy(PROGRAM)

def modify_program(program, noun, verb):
    program[1] = noun
    program[2] = verb
    return program

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
            program_copy = get_program_copy(PROGRAM)
            ans = run_program(modify_program(program_copy, noun, verb))
            if ans == REQD_OUTPUT:
                return 100 * noun + verb

PROGRAM = get_program("input.txt")

# part a
modified_program = modify_program(get_program_copy(PROGRAM), 12, 2)
print(run_program(modified_program))

# part b
print(complete_gravity_assist(PROGRAM, 19690720))
