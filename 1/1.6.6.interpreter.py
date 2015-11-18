import fileinput
import itertools


def operate(program_counter, registers, memory):
    instruction = '{:03d}'.format(memory[program_counter])
    operation, left, right = map(int, instruction)

    if operation == 1:
        raise StopIteration

    elif operation == 2:
        registers[left] = right

    elif operation == 3:
        registers[left] += right

    elif operation == 4:
        registers[left] *= right

    elif operation == 5:
        registers[left] = registers[right]

    elif operation == 6:
        registers[left] += registers[right]

    elif operation == 7:
        registers[left] *= registers[right]

    elif operation == 8:
        registers[left] = memory[right]

    elif operation == 9:
        memory[right] = registers[left]

    elif operation == 0:
        if registers[right]:
            return registers[left]

    registers[left] %= len(memory)
    memory[right % len(memory)] %= len(memory)

    return program_counter + 1


def simulate(instructions, num_registers=10, num_ram=1000):
    registers = [0] * num_registers
    memory = [0] * num_ram
    memory[:len(instructions)] = instructions

    program_counter = 0
    for num_steps in itertools.count():
        try:
            program_counter = operate(program_counter, registers, memory)
        except StopIteration:
            break
    return num_steps + 1 # add one since we break out of the loop


if __name__ == '__main__':
    lines = fileinput.input()
    num_cases = int(next(lines))
    instructions = []

    for line in lines:
        line = line.strip()
        if not line and instructions:
            num_steps = simulate(instructions)
            print(num_steps)
            print # separate cases with a blank line
            instructions = []
        try:
            instructions.append(int(line))
        except ValueError:
            continue
    
    if instructions:
        print(simulate(instructions))
