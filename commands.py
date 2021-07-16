from typing import List


def increment_ptr(instructions: str, mem: List[int], ptr: int, bracket_stack: List[int], instructions_ptr: int):
    """
    Increments the memory pointer by one.
    """
    return ptr + 1, instructions_ptr + 1


def decrement_ptr(instructions: str, mem: List[int], ptr: int, bracket_stack: List[int], instructions_ptr: int):
    """
    Decrements the memory pointer by one.
    """
    return ptr - 1, instructions_ptr + 1


def increment_val(instructions: str, mem: List[int], ptr: int, bracket_stack: List[int], instructions_ptr: int):
    """
    Increment the value of the current cell by one.
    """
    mem[ptr] += 1
    return ptr, instructions_ptr + 1


def decrement_val(instructions: str, mem: List[int], ptr: int, bracket_stack: List[int], instructions_ptr: int):
    """
    Decrement the value of the current cell by one.
    """
    mem[ptr] -= 1
    return ptr, instructions_ptr + 1


def output_val(instructions: str, mem: List[int], ptr: int, bracket_stack: List[int], instructions_ptr: int):
    """
    Output the value of the current cell.
    """
    try:
        if (val := bytes([mem[ptr]]).decode().__repr__()[1:-1]) == "\\n":
            val = "\n"
        elif val == "\\t":
            val = "\t"
    except ValueError:
        val = mem[ptr]
    print(val, end="")
    return ptr, instructions_ptr + 1


def input_val(instructions: str, mem: List[int], ptr: int, bracket_stack: List[int], instructions_ptr: int):
    """
    Get integer and store in current cell. If the input value is an empty string,
    the intended value is assumed to be a new-line and a 10 is stored. If the input
    value is convertable to a decimal number, the value is converted to an integer
    before being pushed to the current cell. In all other cases, the first byte of
    the input value is converted to an integer before being pushed to the current cell.
    """
    if not (val := input()):
        mem[ptr] = 10
    elif val.isdecimal():
        mem[ptr] = int(val)
    else:
        mem[ptr] = val[0].encode()[0]
    return ptr, instructions_ptr + 1


def left_bracket(instructions: str, mem: List[int], ptr: int, bracket_stack: List[int], instructions_ptr: int):
    """
    If the value of the current cell is zero, the instructions pointer is moved to
    the command immediately proceeding the matching bracket. Otherwise, the instructions
    pointer is simply moved to the next command.
    """
    if mem[ptr] == 0:
        bracket_stack.append(instructions_ptr)
        for i, instruction in list(enumerate(instructions))[instructions_ptr: ]:
            if instruction == "[":
                bracket_stack.append(i)
            elif instruction == "]":
                if bracket_stack.pop() == instructions_ptr:
                    instructions_ptr = i + 1
    else:
        bracket_stack.append(instructions_ptr)
        instructions_ptr += 1
    return ptr, instructions_ptr


def right_bracket(instructions: str, mem: List[int], ptr: int, bracket_stack: List[int], instructions_ptr: int):
    """
    If the value of the current cell is non-zero, the instructions pointer is moved to
    the matching bracket. Otherwise, the instructiosn pointer is simply moved to the next
    command.
    """
    l_bracket = bracket_stack.pop()
    if mem[ptr]:
        instructions_ptr = l_bracket
    else:
        instructions_ptr += 1
    return ptr, instructions_ptr