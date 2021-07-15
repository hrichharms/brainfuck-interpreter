if __name__ == "__main__":

    # get command line argument values
    from sys import argv

    # import brainfuck commands
    from commands import *

    # create command callable lookup table
    commands = {
        ">": increment_ptr,
        "<": decrement_ptr,
        "+": increment_val,
        "-": decrement_val,
        ".": output_val,
        ",": input_val,
        "[": left_bracket,
        "]": right_bracket
    }

    # read instructions from file
    with open(argv[1]) as instructions_file:
        instructions = instructions_file.read()

    # filter all non-command characters from loaded instructions
    instructions = "".join(c for c in instructions if c in commands)

    # initialize state variables
    mem = [0] * 3000
    ptr = 0
    bracket_stack = []
    instructions_ptr = 0

    # execute program
    while instructions_ptr != len(instructions):
        ptr, instructions_ptr = commands[instructions[instructions_ptr]](
            instructions,
            mem,
            ptr,
            bracket_stack,
            instructions_ptr
        )
