import interpreter

test_code = '++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>.'

bf = interpreter.BrainFuck(test_code)
bf.run_code()
