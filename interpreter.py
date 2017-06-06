
def parse_code(code):
    return ''.join(c for c in code if c in '><+-.,[]')
