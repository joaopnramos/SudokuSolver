import sys

"""
is_different
checks if two cells are the same
"""
def is_different(cell_i, cell_j):
    result = cell_i != cell_j
    return result


"""
fetch sudokus
fetches sudokus based on user's input
"""
def fetch_sudokus(input):

        DEFAULT_SIZE = 81

        # if the input is an multiple of DEFAULT_SIZE=81
        if (len(input) % DEFAULT_SIZE) != 0:
                print("Error : the string must be a multiple of {}".format(DEFAULT_SIZE))
                sys.exit()
        
        else:
                formatted_input = input.replace("X", "0").replace("#", "0").replace("@", "0")

                if not formatted_input.isdigit():

                        print("Error : only the following characters are allowed: [1,9], 'X', '#' and '@'")
                        sys.exit()
                
                else:
                        return [formatted_input[i:i+DEFAULT_SIZE] for i in range(0, len(formatted_input), DEFAULT_SIZE)]

def print_grid(grid):

        output = ""
        count = 1
        
        # for each cell, print its value
        for cell in grid:

            value = cell
            output += "[" + value + "]"

            # if we reach the end of the line,
            # make a new line on display
            if count >= 9:
                count = 0
                output += "\n"
            
            count += 1
        
        return output