# Chess_project

Chess Program v3

This program executes a normal 2 player game of chess, starting with white move on the bottom side. The program uses PyGame to display its GUI.

When the user selects a piece, all possible moves will be highlighted on the board, persisting until the user either selects a space to move to or clicks anywhere outside of the highlighted squares. The calculation for finding the set of possible moves takes into account typical moves, castling, en passant, and checkmate.

The program has "en passant" moves built into standard pawn movements.

The program is capable of performing "castling".

The program promotes pawns that reach the other side of the board.

The program recognizes "check" situations and will alert the user whenever this occurs.

When a checkmate occurs, the program will declare "CHECKMATE!!!" and pause the game.

The program recognizes stalemate, threefold repetition, fifty-move rule, and insufficient material draws. When a draw occurs, the program will declare "DRAW!!" and pause the game.
