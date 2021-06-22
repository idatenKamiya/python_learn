#3x3morm3 by 3 array or list

#      column  0    1    2      

tictactoe = [['X', 'O', 'X'],   #0
             ['X', 'X', 'O'],   #1  Row
             ['O', 'O', 'O']]   #2

for row in range(0, len(tictactoe)):
    for col in range(0, len(tictactoe)):
        print(tictactoe[row][col], end=" ")
    print("")
    

###################################################################
#Name the variable like in the example below. Its avoids confusion

'''
#      column  0    1    2      

tictactoe = [['X', 'O', 'X'],   #0
             ['X', 'X', 'O'],   #1  Row
             ['O', 'O', 'O'],   #2
             ['O', 'X', 'X']]   #3

for row in range(0, len(tictactoe)):
    for col in range(0, len(tictactoe[row])):
        print(tictactoe[row][col], end=" ")
    print("")

'''