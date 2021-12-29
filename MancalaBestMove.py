from Tree.Node import *
import copy

# Simulates a choice in a game of Mancala.  You pick the beads you'd like to sow, and pickProgression plays through
# until you stop sowing beads
def pickProgression(node, pick):

    # nextNode = copy.deepcopy(node)    # Causes a cascade of deeper and deeper tree's being copied.  Very inefficient
    nextNode = node.copy()              # Much better :)

    # Add game state details
    nextNode.sequence = nextNode.sequence + str(pick) + "-"  # Sequence of all the picks to date, used for convenience
    nextNode.position = pick                                 # Latest pick in the sequence
    nextNode.turn = 1

    progressing = True
    pRow = 1            # position of the row on the board (opponent's row, is 0)
    pColumn = pick-1    # position of the column on the board (1 is leftmost)

    position = pick-1   # position on the board as spots snake through all available spots.
                        # 1 is bottom left, 7 is your own scoring area, 13 is top left

    while (progressing == True):
        numPieces = nextNode.board[pRow][pColumn]
        nextNode.board[pRow][pColumn] = 0

        while (numPieces > 0):
            nextPosition = (position + 1)
            if (nextPosition > 12):
                nextPosition = 0

            if (nextPosition != 6):
                if (nextPosition > 6):
                    pRow = 0
                    pColumn = 12 - nextPosition
                else:
                    pRow = 1
                    pColumn = nextPosition

                nextNode.board[pRow][pColumn] += 1
            else:
                nextNode.score += 1

            position = nextPosition
            numPieces = numPieces - 1

            # print(nextNode)

        if (position == 6):
            progressing = False

            print("Ended in scoring area! Your Score = " + str(nextNode.score) + " [sequence = '" + str(nextNode.sequence) + "']")
        else:
            if (nextNode.board[pRow][pColumn] == 1):
                progressing = False
                nextNode.endOfPicks = True

                print("Ended with sadness! Your Score = " + str(nextNode.score) + " [sequence = '" + str(nextNode.sequence) + "']")

    return nextNode

# Does an exhaustive search of all permutations of choices in a turn of Mancala
def makeTree(node, bestNode, numIter):

    # Try to play through all of your spaces
    for i in range(1,7):

        # Can't play a space with no pieces
        if (node.board[1][i - 1] > 0):

            numIter = numIter + 1

            # Add tree details
            childNode = pickProgression(node, i)
            childNode.parent = node
            node.children[i - 1] = childNode

            # Save the best results
            if (childNode.score > bestNode.score):
                bestNode = childNode.copy()

            # If you ended in a scoring area, keep picking
            if (childNode.endOfPicks == False):
                (bestNode, numIter) = makeTree(childNode, bestNode, numIter)

    return (bestNode, numIter)

# Test pick progression code
# rootNode = Node()
# pickProgression(rootNode,3) # Score is 1, ending in a scoring area
# pickProgression(rootNode,4) # Ends with a score of 6 on an empty space

# Tree search to find the best move
rootNode = Node()
(bestNode, numIter) = makeTree(rootNode, rootNode, 1)

# Print out the optimal move
print()
print("Analysis Complete - " + str(numIter) + " iterations")
print()
print(bestNode)
print("SWEET VICTORY!! Your Score = " + str(bestNode.score) + " [sequence = '" + str(bestNode.sequence) + "']")