import interpreter

test_code = '++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>.'
parsed_code = interpreter.parse_code(test_code)
print(parsed_code)

blocks = interpreter.parse_blocks_in_code(parsed_code)
for i, j in blocks.items():
    print(i," ",j)

f = open('output.txt', 'w')
interpreter.run_code(test_code)
