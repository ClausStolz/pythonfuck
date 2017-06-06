
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
