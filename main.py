import interpreter

test_code = '++-ads.,a2r>da<[da++-.]>.'
parsed_code = interpreter.parse_code(test_code)
print(parsed_code)
