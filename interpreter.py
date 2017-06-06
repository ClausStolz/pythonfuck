
def parse_code(code):
    return ''.join(c for c in code if c in '><+-.,[]')

def parse_blocks_in_code(code):
    blocks = {}
    block_start_array = []
    for i in range(len(code)):
        if (code[i] == '['):
            block_start_array.append(i)
        elif (code[i] == ']'):
            blocks[i] = block_start_array[-1]
            blocks[block_start_array.pop()] = i
    return blocks

def run_code(code):
    code = parse_code(code)
    blocks = parse_blocks_in_code(code)
    x = 0
    i = 0
    char_buffer = {0: 0}
    while i < len(code):
        char_value = code[i]
        if (char_value == '>'):
            x += 1
            char_buffer.setdefault(x, 0)
        elif (char_value == '<'):
            x -= 1
        elif (char_value == '+'):
            char_buffer[x] += 1
        elif (char_value == '-'):
            char_buffer[x] -= 1
        elif (char_value == '.'):
            print(chr(char_buffer[x]), end = '')
        elif (char_value == ','):
            char_buffer[x] = int(input('Input: '))
        elif (char_value == '['):
            if (not char_buffer[x]):
                i = blocks[i]
        elif (char_value == ']'):
            if (char_buffer[x]):
                i = blocks[i]
        i += 1
