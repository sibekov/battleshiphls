# while True:
#     try:
#         x = int(input('Enter a number.'))
#         print(f'Number is {x}')
#     except ValueError:
#         print('Not a number')

##########################################################

# cars={'ford':10,'opel':5}

# def get_val(key):
#     try:
#         #for key in cars:
#         return cars[key]
#     except:
#         return None

# ford=get_val("ford")
# print(ford)

# hyundai=get_val("hyundai")
# print(hyundai)

# while True:
#     try:
#         x = int(input('Enter a number:'))
#         print(f'Number is {x}')
#     except ValueError:
#         print('Not a number')

# while True:
#     try:
#         a = int(input('Please enter an nteger as the numerator:'))
#         b = int(input('Please enter an integer as the denominator:'))
#         print(a/b)
#     except ZeroDivisionError:
#         print("Please enter a valid denominator.")
#     except ValueError:
#         print("Both values have to be integers.")
#     except Exception:
#         print('Another error has occurred')

# while True:
#     try:
#         a = int(input('Please enter an nteger as the numerator:'))
#         b = int(input('Please enter an integer as the denominator:'))
#         print(a/b)
#     except (ZeroDivisionError,ValueError):
#         print("An error has occurred")

# try:
#     print(non_existent_variable)
# except NameError:
#     print("variable not defined")

# def encode_name(name):
#     try:
#         name=name.encode('ascii')
#     except UnicodeError as e:
#         print(f'The name {e.object} has a character at position {e.start} that cannot be encoded in {e.ncoding} due to {e.reason}')
#         return name

# encode_name('St_fan')
# try:
#     f = open('book.txt')
#     s = f.readline()
# except OSError as e:
#     errno,strerror= e.args
#     print(f"There is an I/O error number, {errno}:{strerror}:'book.txt'")


############################################################################################
# values = (10,5)
# def append_to_list(ls,val):
#     try:
#         ls.append(val)
#     except AttributeError as e:
#         print(e.args[0])
#     return ls

# append_to_list(values,4)
#

# def linecount(filename):
#     try:
#         f = open(filename,'r')
#         s=f.readlines()
#     except OSError as e:
#         errno,strerror = e.args
#         print(f"There is an I/O error number,{errno}:{strerror}.")
#     else:
#         print(f'{filename} is {len(s)} line long')
#         print(f"The opening line of {filename} is '{s[0]}' ")
#         f.close()
#     finally:
#         print(f'Finished with {filename}.')

# linecount('gulliver.txt')
# print("\n")
# linecount('swift.txt')    


# f = open(filename)
# try:
#     #My Code
# finally: 
#     f.close()

# with open(filename) as f:
# #     # My Code
# cars = {'ford':5,'hyundai':6}

# def update_cars(data,key,val):
#     try:
#         data[key]
#     except KeyError as e:
#         print(f"No Key {e} in dictionary")
#     else:
#         data[key]=val
#     finally:
#         print(data)
#         return data

# update_cars(cars,"mazda",8)

##############################################################PROJECT#########################################################
from random import randint
import string
scores = {"computer":0,"player":0}

class Board():
    """
    Main board class. sets the voard size, the number of ships, the player's name and the board type (Player board or Computer board)
    Hass methods for adding ships and making guesses and then printing the boards.
    """

    def __init__(self,size,num_ships,name,type):
        self.size=size
        self.Theboard=[["." for x in range(size)] for y in range(size)]
        self.num_ships=num_ships
        self.name=name
        self.type=type
        self.guesses=[]
        self.ships=[]

    def print(self):
        for row in self.Theboard:
            print(" ".join(row))

    def guess(self,x,y):
        self.guesses.append((x,y))
        self.Theboard[x][y]="X"
        if (x,y) in self.ships:
            self.Theboard[x][y]="*"
            return "Hit"
        else:
            return "Miss"

    def add_ship(self,x,y,type="computer"):
        if len(self.ships)>=self.num_ships:
            print("Error:you cannot add any more ships!")
        else:
            self.ships.append((x,y))
        if self.type=="player":
            self.Theboard[x][y]="@"
            


####### HELPER FUNCTIONS ##########

def random_point(size):
    """
    Helper funtion to return a random integer between 0 and size
    """
    return randint(0,size-1)

def valid_coordinates(x,y,board):
    """
    validates coordinates guessed and coordinates if are out of scope.
    """
    pass


def populate_board(myboard):
    """
    insert a ship
    """
    myboard.print()
    s=myboard.num_ships
    x=random_point(s)
    print(f" x is equl to {x}")
    y=random_point(s)

    print(f" y is equl to {y}")

    myboard[x][y] ="@"
    myboard.ships.append((x,y))
    print(myboard.ships)


    return 

#print(Board.add_ship(board,random_point(board.size),random_point(board.size),board.type))
    
def make_guess(board):
    """
    processes for computer it popolates automatically.
    """
    return board.guesses()

def play_game(computer_board,player_board):
    """
    Play game.
    """
    pass

def new_game():
    """
    Starts a new game. Sets the board size and number of ships, resets the scores and initialises the boards.
    """
    size=5
    num_ships=4
    scores["computer"]=0
    scores["player"]=0
    print("_"*35)
    print("Welcome to ULTIMATE BATTLESHIPS!!")
    print(f"Board size:{size},Number of ships:{num_ships}")
    print("Top left Corner is row:0,col:0")
    print(" "*35)
    player_name = input("Please enter your name:\n")
    print("_"*35)
    computer_board = Board(size,num_ships,"computer",type="computer")
    player_board = Board(size,num_ships,player_name,type="player")

   
    populate_board(player_board)
    
#for _ in range(num_ships):
        
#         populate_board(player_board)
#         populate_board(computer_board)
#     play_game(computer_board,player_board)


new_game()