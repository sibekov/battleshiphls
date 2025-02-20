try:
    f=open('sample.txt','r')
    f.write("Test write to sample text!")
except IOError:
    print("ERROR:COULD NOT FIND FILE OR READ DATA!")
else:
    print("SUCCESS!")
    f.close()

print("Hello world!")

try:
    f=open('sample.txt','r')
    f.write("Test write to sample text!")
except IOError:
    print("ERROR:COULD NOT FIND FILE OR READ DATA!")
finally:       #works even if there is error
    print("I ALWAYS WORK NO MATTER WHAT")
    f.close()

print("Hello world!")

def valid_coordinates(x, y, board):
    """
    validate that the cordinates inputs that validates that not yet guessed.
    Validate that they are not outside our board.
    """
    listvar = [0, 1, 2, 3, 4]
    try:
        if x not in listvar:
            raise ValueError(f"Sorry you entered invalid input {x}!")
    except ValueError as e:
        print(f"Invalid guess: {e}, which is outside the range, please try any of the following numbers 0, 1, 2, 3, 4\n")
        return False
    try:
        if y not in listvar:
            raise ValueError(f"Sorry you entered invalid input {y}!")
    except ValueError as e:
        print(f"Invalid guess: {e}, which is outside the range, please try one of the following numbers 0, 1, 2, 3, 4\n")
        return False
    try:
        if (x, y) in board.guesses:
            raise ValueError(f"Sorry you have already guessed {(x,y)}!")
    except ValueError as e:
        print(f"Invalid guess:{e},please try again.\n")
        return False
    try:
        if type(x) is str:
            raise ValueError(f"Sorry you have supplied a string {x}!")
    except ValueError as e:
        print(f"Invalid guess: {e}, please try one of the following numbers 0, 1, 2, 3, 4\n")
        return False
    return True
    
try:
    if(2>3):
        raise ValueError(f"Sorry Trying to compare un equal numbers {x} and {y}")
    except Valueerror as e:
        print(f" invalid gues: {e}")

