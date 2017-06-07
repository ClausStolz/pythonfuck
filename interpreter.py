
class BrainFuck:
    def __init__(self, aCode = ''):
        self.code = aCode
        self.x = 0
        self.i = 0

    def run_code(self, aCode = ''):
        if (not aCode == ''):
            self.code = aCode

        self.code = BrainFuck.parse_code(self)
        blocks = BrainFuck.parse_blocks_in_code(self)
        char_buffer = {0: 0}
        while self.i < len(self.code):
            char_value = self.code[self.i]
            if (char_value == '>'):
                self.x += 1
                char_buffer.setdefault(self.x, 0)
            elif (char_value == '<'):
                self.x -= 1
            elif (char_value == '+'):
                char_buffer[self.x] += 1
            elif (char_value == '-'):
                char_buffer[self.x] -= 1
            elif (char_value == '.'):
                print(chr(char_buffer[self.x]), end = '')
            elif (char_value == ','):
                char_buffer[self.x] = int(input('Input: '))
            elif (char_value == '['):
                if (not char_buffer[self.x]):
                    self.i = blocks[self.i]
            elif (char_value == ']'):
                if (char_buffer[self.x]):
                    self.i = blocks[self.i]
            self.i += 1

    def parse_code(self):
        return ''.join(c for c in self.code if c in '><+-.,[]')

    def parse_blocks_in_code(self):
        blocks = {}
        block_start_array = []
        for i in range(len(self.code)):
            if (self.code[i] == '['):
                block_start_array.append(i)
            elif (self.code[i] == ']'):
                blocks[i] = block_start_array[-1]
                blocks[block_start_array.pop()] = i
        return blocks
