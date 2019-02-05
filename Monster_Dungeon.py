class MonsterDungeon():
    def __init__(self, rows, cols, lives, level):
        self.rows = rows
        self.cols = cols
        self.lives = lives
        self.level = level

    def showLevel(self):
        print('LEVEL {}'.format(self.level))

    def showGrid(self, player, monster, door, power_up):
        # make sure you have access to coordinates in player and monster classes
        print('Player Coords: {}'.format(player.coords))
        print('Monster Coords: {}'.format(monster.coords))
        print('Lives Left: {}'.format(self.lives))

        for i in range(self.rows):
            # print top border for each row
            print(' ---' * self.cols)
            for j in range(self.cols):
                if i == power_up.coords[1] and j == power_up.coords[0] and power_up.received == False:
                    print('| + ', end='')
                elif i == player.coords[1] and j == player.coords[0] and j == self.cols - 1:
                    print('| p ', end='|')
                elif i == player.coords[1] and j == player.coords[0]:
                    print('| p ', end='')
                elif i == door.coords[1] and j == door.coords[0] and j == self.cols - 1:
                    print('| d ', end='|')
                elif i == door.coords[1] and j == door.coords[0]:
                    print('| d ', end='')
                elif i == monster.coords[1] and j == monster.coords[0] and j == self.cols - 1:
                    print('| m ', end='|')
                elif i == monster.coords[1] and j == monster.coords[0]:
                    print('| m ', end='')
                elif j == self.cols - 1:
                    print('|   ', end='|')
                else:
                    print('|   ', end='')
            # start new row here
            print('')

            if i == self.rows - 1:
                # print bottom border for only the last row
                print(' ---' *self.cols)

    def checkCollision(self, player, monster):
        if player.coords == monster.coords:
            self.lives -= 1
            print('You just got eaten! You have {} lives left.'.format(self.lives))

    def checkLoseCondition(self):
        if self.lives <= 0:
            return True

    def checkWinCondition(self, player, door):
        if player.coords == door.coords:
            self.level += 1
            return True

    def checkPowerUp(self, player, power_up):
        if player.coords == power_up.coords and power_up.received == False:
            self.lives += 1
            # using setter method to change value, as is good practice not to change directly
            # sending in the value of True to the method
            power_up.setReceived(True)

class Player():
    def __init__(self, name):
        self.name = name
        self.coords = [0,0] #x,y

    def movePlayer(self, cols, rows):
        while True:
            print('Type quit if you would like to stop playing!')
            ans = input('Move left/right/up/down? ')

            # move player based on ans taken in
            if ans.lower() == 'quit':
                return True
            elif ans.lower() == 'up'and self.coords[1] > 0:
                self.coords[1] -= 1
                break
            elif ans.lower() == 'up':
                self.coords[1] = rows - 1
                break
            elif ans.lower() == 'down' and self.coords[1] < rows - 1:
                self.coords[1] += 1
                break
            elif ans.lower() == 'down':
                self.coords[1] = 0
                break
            elif ans.lower() == 'left' and self.coords[0] > 0:
                self.coords[0] -= 1
                break
            elif ans.lower() == 'left':
                self.coords[0] = cols - 1
                break
            elif ans.lower() == 'right' and self.coords[0] < cols - 1:
                self.coords[0] += 1
                break
            elif ans.lower() == 'right':
                self.coords[0] = 0
                break
            else:
                print('Incorrect input, try again...')

                # clear output after asking question
                clear_output()
    def resetPlayer(self, player):
        self.coords = [0,0]

class Monster():
    def __init__(self):
        self.coords = [2,2] #x,y

    def moveMonster(self, cols, rows):
        while True:
            self.coords = [random.randint(0, cols - 1), random.randint(0, rows - 1)]
            if self.coords != door.coords:
                break

class Door():
    def __init__(self):
        self.coords = [0,1]

class PowerUp():
    def __init__(self):
        self.coords = [3,0]
        self.received = False

    def setReceived(self, value):
        self.received = value

from IPython.display import clear_output
import random

# START OF MAIN LOOP
while True:
    # define our global variables to be used
    rows = 5
    cols = 5
    lives = 3
    level = 1
    flag_plus = []
    game_over = False
    player = Player('Max')
    monster = Monster()
    door = Door()
    power_up = PowerUp()
    game = MonsterDungeon(rows, cols, lives, level)



    while game_over != True:
        # clear
        clear_output()

        game.showLevel()

        # show the grid
        game.showGrid(player, monster, door, power_up)

        # call player to move
        game_over = player.movePlayer(cols, rows)

        # call monster to move, send in rows and cols
        monster.moveMonster(cols, rows)

        # check to see if monster ate player
        game.checkCollision(player, monster)

        # check to see if player reached power up
        game.checkPowerUp(player, power_up)


        # check if lives are gone, then break
        # breaking because we don't want any other lines below this running
        if game.checkLoseCondition():
            print('You lost all your lives, better luck next time!')
            game_over = True
        elif game.checkWinCondition(player, door):
            print('Congratulations, you beat the monster!')
            ans = input('Play next level (yes/no)? ')
            if ans.lower() == 'no':
                break
            player.resetPlayer(player)
            continue

    # ask if they want to play again, if not break out oof while loop
    ans = input('Would you like to play again (yes/no)? ')

    if ans.lower() == 'no':
        print('Thanks for playing!')
        break
