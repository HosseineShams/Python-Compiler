# import the lexer and parser modules
import lexer
import parser

# Keep looping until the user enters an EOF (end-of-file) character
while True:
    try:
        # Read input from the user
        s = input('calc > ')
    except EOFError:
        # If an EOF is entered, break out of the loop
        break
    # If no input is entered, skip to the next iteration
    if not s:
        continue
    # Parse the input expression using the parser module
    result = parser.parser.parse(s)
    # Print the result to the screen
    print(result)
