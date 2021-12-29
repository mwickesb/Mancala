import numpy as np
import copy

class Node(object):

    def __init__(self):

        # Describe the game state
        self.board = np.array([[4,4,4,4,4,4], [4,4,4,4,4,4]])   # State of the board after you pick a position
        self.sequence = ""                          # Sequence of all the picks to date, used for convenience
        self.position = 1                           # Latest pick in the sequence
        self.turn = 0                               # Turn in the game
        self.endOfPicks = False                     # 'True' if there are no more picks open in the sequence
        self.score = 0                              # Number of beads in your scoring area

        # Describe the tree
        self.children = [None, None, None, None, None, None]
        self.parent = None

    def __str__(self):
        return np.array2string(self.board) + '\n'

    def copy(self):
        newNode = Node()

        # Copy the gamestate information
        newNode.board = copy.copy(self.board)
        newNode.sequence = copy.copy(self.sequence)
        newNode.position = copy.copy(self.position)
        newNode.turn = copy.copy(self.turn)
        newNode.endOfPicks = copy.copy(self.endOfPicks)
        newNode.score = copy.copy(self.score)

        # Pass references to tree details
        for i in range(6):
            newNode.children[i] = self.children[i]

        newNode.parent = self.parent

        return newNode