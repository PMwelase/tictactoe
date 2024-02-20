from prettytable import PrettyTable, ALL


# def table(grid):
#    for x in grid:
#       print(x)

def create_table(grid):
    table = PrettyTable([" ", "1", "2", "3"])
    table.title = "Tic Tac Toe"
    table.header = True
    table.hrules = ALL
    letters = ["A", "B", "C"]

    for row in range(3):
        table.add_row([letters[row], grid[row][0], grid[row][1], grid[row][2]])
    
    print(table)


def check_turns(turns) -> int:
    if turns % 2 == 0:
        return "X"
    else:
        return "O"


def get_input() -> str:
   coord = input("Please enter a coordinate: ").upper()
   if coord in ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]:
       if coord[0] == "A": idx = 0
       elif coord[0] == "B": idx = 1
       elif coord[0] == "C": idx = 2
       return idx, int(coord[1]) - 1
   else:
       print("Invalid input")
       return get_input()


def validate_input(grid, coord) -> bool:
    return grid[coord[0]][coord[1]] == " "


def check_win(grid, turns) -> bool:
    if turns < 5:
        return False
    elif turns < 9:
        for n in range(3):
            if grid[n][0] == grid[n][1] == grid[n][2] != " ":
                return True  #Horizontal Win
            elif grid[0][n] == grid[1][n] == grid[2][n] != " ":
                return True #Vertical Win
        if grid[0][0] == grid[1][1] == grid[2][2] != " ":
            return True #Diagonal Win
        elif grid[0][2] == grid[1][1] == grid[2][0] != " ":
            return True #Diagonal Win
    elif turns > 8:
        return True
    return False


def replay(grid) -> bool:
   prompt = input("Would you like to play again: [Y/N]: \n")
   try:
        if prompt.lower() == "y":
            grid = reset_grid(grid)
            return True
        elif prompt.lower() == "n":
            return False
        else:
            print("Please enter a valid input.")
            return replay(grid)
   except:
       print("Please enter a valid input.")
       return replay()


def reset_grid(grid):
    for n in range(3):
        for x in range(3):
            grid[n][x] = " "


def game(grid):
    turns = 0
    game_over = False

    while not game_over:
        coord = get_input()

        if validate_input(grid, coord):
            symbol = check_turns(turns)
            grid[coord[0]][coord[1]] = symbol
            create_table(grid)
            turns += 1
            game_over = check_win(grid, turns)
            
        else:
            print("Invalid input") 
    
  


if __name__ == "__main__":
    grid = [
      [" ", " ", " "],
      [" ", " ", " "],
      [" ", " ", " "]
    ]

    play = True
    while play:
        create_table(grid)
        game(grid)
        play = replay(grid)
        
    
    print("Thanks for playing!")


