'''
Source code from: https://2018.galacticpuzzlehunt.com/static/puzzle_resources/adventure/adventure.py
'''

import string

DEBUG = False

ROOMS = 'QWERTYUIOPASDFGHJKLZXCVBNM'

DIRECTIONS = {'nw': 0,
              'ne': 1,
              'e' : 2,
              'se': 3,
              'sw': 4,
              'w' : 5}

DIRECTION_NAMES = {0: 'northwest (nw)',
                   1: 'northeast (ne)',
                   2: 'east (e)',
                   3: 'southeast (se)',
                   4: 'southwest (sw)',
                   5: 'west (w)'}

NEIGHBORS = {
    'Q': [None, None, 'W', 'A', None, None],
    'W': [None, None, 'E', 'S', 'A', 'Q'],
    'E': [None, None, 'R', 'D', 'S', 'W'],
    'R': [None, None, 'T', 'F', 'D', 'E'],
    'T': [None, None, 'Y', 'G', 'F', 'R'],
    'Y': [None, None, 'U', 'H', 'G', 'T'],
    'U': [None, None, 'I', 'J', 'H', 'Y'],
    'I': [None, None, 'O', 'K', 'J', 'U'],
    'O': [None, None, 'P', 'L', 'K', 'I'],
    'P': [None, None, None, None, 'L', 'O'],
    'A': ['Q', 'W', 'S', 'Z', None, None],
    'S': ['W', 'E', 'D', 'X', 'Z', 'A'],
    'D': ['E', 'R', 'F', 'C', 'X', 'S'],
    'F': ['R', 'T', 'G', 'V', 'C', 'D'],
    'G': ['T', 'Y', 'H', 'B', 'V', 'F'],
    'H': ['Y', 'U', 'J', 'N', 'B', 'G'],
    'J': ['U', 'I', 'K', 'M', 'N', 'H'],
    'K': ['I', 'O', 'L', None, 'M', 'J'],
    'L': ['O', 'P', None, None, None, 'K'],
    'Z': ['A', 'S', 'X', None, None, None],
    'X': ['S', 'D', 'C', None, None, 'Z'],
    'C': ['D', 'F', 'V', None, None, 'X'],
    'V': ['F', 'G', 'B', None, None, 'C'],
    'B': ['G', 'H', 'N', None, None, 'V'],
    'N': ['H', 'J', 'M', None, None, 'B'],
    'M': ['J', 'K', None, None, None, 'N']
}

ADVICE = {
    'Q': "By default any actions you might take while reading from a blackboard are "
         "not displayed to you. You can turn these on by typing 'v'.",
    'W': "You can type 'q' to reset the current game.",
    'E': "",
    'R': "Including 'i' in your command will cause the remainder of your command to execute only if "
         "the blackboard in the current room is empty.",
    'T': "",
    'Y': "Space is irrelevant; typing 'pes' and 'p e s' will have the same result.",
    'U': "",
    'I': "Including 'j' in your command will cause the remainder of your command to execute only if "
         "the blackboard in the current room is not empty.",
    'O': "",
    'P': "Be efficient! Rumor has it a terrible fate awaits those who take more than 1000000 steps in this dungeon. "
         "Similar tragedies are said to befall those who try to write more than 50000 characters on a blackboard or "
         "get stuck more than 1000 layers deep in their own head.",
    'A': "The blackboards here are cursed. Actively reading from one forces you to follow whatever "
         "is written on it (as if you entered the contents of the blackboard as a single line).",
    'S': "You can read the contents of a blackboard by typing 'r'.",
    'D': "",
    'F': "",
    'G': "You can chain commands together by typing them next to each other in the same line. "
         "For example, typing 'e ne' moves east then moves northeast.",
    'H': "Welcome to this puzzle. To navigate around the dungeon, simply type the direction (e.g. 'ne') you wish "
         "to move in. More commands will be explained as you progress through this puzzle.",
    'J': "You can press a button in a room by typing 'p'.",
    'K': "",
    'L': "Type 'l' to see a log of what you've typed during your current play through the game.",
    'Z': "By typing 'd' you can erase the last character on a blackboard.",
    'X': "Type 'k' to see a log of what you've typed during your current play through the game.",
    'C': "Pressing buttons sometimes causes reality to destabilize. Why is that? Who knows?",
    'V': "Typing 't' lets you write on a blackboard. You will write the remainder of your line to "
         "this blackboard; for example, 't hello there' writes \"hellothere\" on the blackboard.",
    'B': "",
    'N': "",
    'M': "Using 't' will erase what is currently on the blackboard before writing. To append to a blackboard instead, use 'a'."
}

MESSAGE = 'TYPESAMETHINGBOTHKEYBOARDS'
LETTERS = {c: m for c, m in zip(string.ascii_uppercase, MESSAGE)}

MAX_COMMANDS = 1000000
MAX_BLACKBOARD_LENGTH = 50000
MAX_DEPTH = 1000

ROOM_DESCRIPTION = ("You are in a large square room with a giant letter {} engraved in the floor."
                    " In the middle of the room there is a blackboard."
                    " Next to the blackboard is a small button.")


class GameState:
    def __init__(self):
        self.location = 'H'
        self.log1 = ''
        self.log2 = ''
        self.blackboards = {key: '' for key in ROOMS}
        self.running = True
        self.won = False

        self.num_commands = 0
        self.depth = 0
        self.verbose = DEBUG

        self.current_output = ''

    def log(self, msg):
        if self.depth == 0 or self.verbose:
            self.print(msg)

    def print(self, message):
        self.current_output += message + '\n'

    def reset_current_output(self):
        self.current_output = ''

    def get_current_output(self):
        return self.current_output

    def describe_room(self):
        room = self.location
        if DEBUG:
            self.log("Room: " + room)

        self.log(ROOM_DESCRIPTION.format(LETTERS[room]))
        self.log('')

        if self.blackboards[room]:
            self.log('The blackboard has the following text written on it: {}'.format(self.blackboards[room]))
        else:
            self.log('The blackboard in this room is empty.')
        self.log('')

        if ADVICE[room]:
            self.log('A monkey pops out of the ceiling and says "{}"'.format(ADVICE[room]))
            self.log('')

        exits = [DIRECTION_NAMES[i] for i in range(6) if NEIGHBORS[room][i]]
        exits[-1] = 'and ' + exits[-1]
        self.log('There are exits to the {}.'.format(', '.join(exits)))

    def move(self, direction):
        next_loc = NEIGHBORS[self.location][direction]
        if next_loc is None:
            self.log("You cannot move in that direction.")
        else:
            self.location = next_loc

    def execute(self, line):
        if self.depth > MAX_DEPTH:
            self.print("You are in too deep! The air around you becomes difficult to breathe. You slowly fall unconscious...")
            self.running = False
            return

        while line:
            if not self.running:
                return

            self.num_commands += 1
            if self.num_commands > MAX_COMMANDS:
                self.print("You have been wandering around for too long. You die of starvation.")
                self.running = False
                return

            cmd = line[0]
            st = 1
            if cmd in 'news':
                # move
                try:
                    direction = cmd
                    if direction in 'ns':
                        direction += line[1]
                        st = 2

                    if direction not in DIRECTIONS:
                        self.log("{} is not a valid direction.".format(direction))
                        return

                    self.move(DIRECTIONS[direction])
                except Exception:
                    self.log("You must specify a valid direction to move in.")

            elif cmd == 'p':
                # press
                self.log("You press the button.")
                self.log2 += self.location.lower()

                if self.log1 == self.log2:
                    self.running = False
                    self.won = True
                    return

                if not self.log1.startswith(self.log2):
                    self.log("Uh oh. You feel like pressing that button was a mistake. Everything slowly fades out of existence...")

                    self.running = False
                    return
            elif cmd == 't':
                # write on blackboard
                self.blackboards[self.location] = line[1:]
                if len(self.blackboards[self.location]) >= MAX_BLACKBOARD_LENGTH:
                    self.print("While struggling to fit all this text on the blackboard, the blackboard topples over, flattening you.")
                    self.running = False
                    return

                self.log("You write on the blackboard. The blackboard now says: {}".format(self.blackboards[self.location]))
                st = len(line)
            elif cmd == 'r':
                # read from blackboard
                newcmd = self.blackboards[self.location]
                if newcmd == '':
                    self.log("The blackboard is empty.")
                else:
                    self.log("You read the text on the blackboard. You suddenly feel compelled to obey its instructions...")
                    self.depth += 1
                    self.execute(newcmd)
                    self.depth -= 1
            elif cmd == 'a':
                # append to blackboard
                self.blackboards[self.location] += line[1:]
                if len(self.blackboards[self.location]) >= MAX_BLACKBOARD_LENGTH:
                    self.print("While struggling to fit all this text on the blackboard, the blackboard topples over, flattening you.")
                    self.running = False
                    return
                self.log("You add some text to the blackboard. The blackboard now says: {}".format(self.blackboards[self.location]))
                st = len(line)
            elif cmd == 'd':
                if self.blackboards[self.location]:
                    self.blackboards[self.location] = self.blackboards[self.location][:-1]
                    self.log("You erase the last letter from the text on the blackboard. The blackboard now says: {}".format(self.blackboards[self.location]))
                else:
                    self.log("The blackboard is empty.")
            elif cmd == 'i':
                if self.blackboards[self.location]:
                    return
            elif cmd == 'j':
                if not self.blackboards[self.location]:
                    return
            elif cmd == 'l':
                self.log(self.log1)
            elif cmd == 'k':
                self.log(self.log2)
            elif cmd == 'q':
                self.running = False
                return
            elif cmd == 'v':
                if self.verbose:
                    self.log("You pay less attention to your actions.")
                    self.verbose = False
                else:
                    self.log("You pay closer attention to your actions.")
                    self.verbose = True
            else:
                self.print("Invalid command.")
                return

            line = line[st:]


class AdventureGame:
    def __init__(self):
        self.state = GameState()
        self.old_location = None
        self.state.describe_room()

    def run_command(self, command):
        line = ''.join([c for c in command.lower() if c.islower()])

        self.state.reset_current_output()

        self.state.log1 += line
        self.old_location = self.state.location
        self.state.execute(line)

        if self.state.won:
            self.state.print("Congratulations, you played yourself. The answer to this puzzle is PASIPHAE.")
        elif self.state.location != self.old_location:
            self.state.describe_room()

    def get_current_output(self):
        return self.state.get_current_output()

'''
def main():
    game = AdventureGame()

    commands = [
        'a wrwwnwpep',
        'se',
        'a pnww a wwwpneppepsee',
        'enenee',
        'a pswwwww a seepnwnwwwwpppppepsee',
        'wwwwww',
        'a psee a seepnwnwwwwwppeepsee',
        'w',
        'a pseee a seepnwnwwwwwpppeepsee',
        'w',
        'a pseeee a seepnwnwwwwwppppeepsee',
        'sw',
        'a peeee a nwwwwppppeepsee',
        'e',
        'a peee a nwwwwpppeepsee',
        'eee',
        'wwwwrnwwwwrnwwrnwwwwrnwwwwrseernwwwwrneeeeernwwwrneeeeerwwwrnwwwrwwwwrneeeeerseernwwwwrnwwwwrwwwwrnwwwwrnwwwwrnwwwwrneeeeerseernwwwrneeeeerneeeeernwwwrneeeeerwwwrnwwwrnwwwrnwwwrseernwwwrseernwwwrnwwwrwwwwrneeeeerwwwrnwwwwrnwwwwrnwwwwrnwwwwrnwwwwrwwwwrwwwrnwwwrnwwwrneeeeerseernwwwwrseernwwwwrnwwwwrnwwwwrnwwwwrneeeeerneeeeerneeeeerneeeeerneeeeernwwwrneeeeerwwwrnwwwrnwwwrnwwwwrnwwwwrnwwwwrnwwwwrnwwwwrnwwwwrwwwwrneeeeerwwwrnwwwrnwwwrwwwwrwwwrnwwwrnwwwrneeeeerseernwwwwrseernwwwwrnwwwwrnwwwwrnwwwwrnwwwwrneeeeerneeeeernwwwrnwwwrneeeeerwwwrnwwwrnwwwrnwwwwrwwwwrneeeeerwwwrnwwwrnwwwrnwwwrwwwwrwwwrnwwwrnwwwrneeeeerseernwwwwrseernwwwwrnwwwwrnwwwwrnwwwwrnwwwwrneeeeerneeeeerneeeeernwwwrnwwwrneeeeerwwwrnwwwrnwwwrnwwwwrwwwwrneeeeerwwwrnwwwrnwwwrnwwwrnwwwrwwwwrwwwrnwwwrnwwwrneeeeerseernwwwwrseernwwwwrnwwwwrnwwwwrnwwwwrnwwwwrneeeeerneeeeerneeeeerneeeeernwwwrnwwwrneeeeerwwwrnwwwrnwwwrwwwrnwwwwrwwwwrneeeeernwwwrnwwwrnwwwrnwwwrwwwwrseernwwwwrnwwwwrnwwwwrnwwwwrneeeeerneeeeerneeeeerneeeeernwwwrnwwwrneeeeerwwwrnwwwrnwwwrnwwwrwwwwrneeeeernwwwrnwwwrnwwwrwwwwrseernwwwwrnwwwwrnwwwwrnwwwwrneeeeerneeeeerneeeeernwwwrnwwwrneeeeerwwwrnwwwrnwwwrnwwwrnwwwrnwwwr',
        'er',
    ]

    for command in commands:
        print(game.get_current_output())
        print('> ' + command)
        game.run_command(command)

    print(game.get_current_output())

if __name__ == "__main__":
    main()
'''
