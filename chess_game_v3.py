# -------------------------------------------------------------------------------
# Name:         Chess Game v3
# Author:       Joseph Nguyen

# Created:      20/1/2020
# Last Update:  29/1/2020
# -------------------------------------------------------------------------------

# -----------------------------------------------
# ----------------INITIAL LOADUPS----------------
# -----------------------------------------------
import pygame

pygame.init()

# -----------------------------------------------
# -------------PYGAME BASIC DISPLAY--------------
# -----------------------------------------------

# screen
screen = pygame.display.set_mode((825,600))

# title and icon
pygame.display.set_caption('Classic Chess')
icon = pygame.image.load('chess_icon.png')
pygame.display.set_icon(icon)

# board image
board_image = pygame.image.load('board_image.png')
board_dim = (500,500)
board_loc = (50,50) 
left_len = 50
right_len = 50
top_len = 50
bottom_len = 50
square_vert = 50
square_hori = 50

# text locations
turn_num_loc = (575,50)
turn_loc = (575, 100)
check_loc = (575, 175)
upgrade_loc = (575,300)
checkmate_loc = (400-100,300-16)
draw_loc = (400-50,300-16)

# images of pieces (50 x 50)
bp_image = pygame.image.load('bp.png')
bq_image = pygame.image.load('bq.png')
bk_image = pygame.image.load('bk.png')
br_image = pygame.image.load('br.png')
bb_image = pygame.image.load('bb.png')
bn_image = pygame.image.load('bn.png')
wp_image = pygame.image.load('wp.png')
wq_image = pygame.image.load('wq.png')
wk_image = pygame.image.load('wk.png')
wr_image = pygame.image.load('wr.png')
wb_image = pygame.image.load('wb.png')
wn_image = pygame.image.load('wn.png')

# Misc.
font = pygame.font.Font('freesansbold.ttf', 32)

# -----------------------------------------------
# -------------------FUNCTIONS-------------------
# -----------------------------------------------
def display_board():
    """Updates the PyGame screen based on User interactions."""

    def coord_to_display(coord):
        """Converts the coordinate int into the tuple corresponding with its position on the display."""
        squares_right = (coord % 10) - 1
        squares_down = 8 - (coord // 10)

        x_loc = board_loc[0] + left_len + square_hori*(squares_right)
        y_loc = board_loc[1] + top_len + square_vert*(squares_down)

        return (x_loc, y_loc)

    #draw background
    screen.fill((0,128,0))

    #display turn and turn number
    turn_num_display = font.render('Turn ' + str(turn_num), True, (255,255,255))
    screen.blit(turn_num_display, turn_num_loc)
    turn_display = font.render(board[turn] + ' Move', True, (255,255,255))
    screen.blit(turn_display, turn_loc)

    #draw empty board
    screen.blit(board_image, board_loc)

    #highlight move space if needed
    if select == True:
        for coord in move_space:
            loc = coord_to_display(coord)
            pygame.draw.rect(screen,(30,144,255),[loc[0],loc[1],square_vert,square_hori])

    #add pieces
    coord_list = generate_coord()
    for coord in coord_list:
        if board[coord] != '[]':
            if board[coord] == 'bp':
                loc = coord_to_display(coord)
                screen.blit(bp_image, loc)
            elif board[coord] == 'bq':
                loc = coord_to_display(coord)
                screen.blit(bq_image, loc)
            elif board[coord] == 'bk':
                loc = coord_to_display(coord)
                screen.blit(bk_image, loc)
            elif board[coord] == 'br':
                loc = coord_to_display(coord)
                screen.blit(br_image, loc)
            elif board[coord] == 'bb':
                loc = coord_to_display(coord)
                screen.blit(bb_image, loc)
            elif board[coord] == 'bn':
                loc = coord_to_display(coord)
                screen.blit(bn_image, loc)
            elif board[coord] == 'wp':
                loc = coord_to_display(coord)
                screen.blit(wp_image, loc)
            elif board[coord] == 'wq':
                loc = coord_to_display(coord)
                screen.blit(wq_image, loc)
            elif board[coord] == 'wk':
                loc = coord_to_display(coord)
                screen.blit(wk_image, loc)
            elif board[coord] == 'wr':
                loc = coord_to_display(coord)
                screen.blit(wr_image, loc)
            elif board[coord] == 'wb':
                loc = coord_to_display(coord)
                screen.blit(wb_image, loc)
            elif board[coord] == 'wn':
                loc = coord_to_display(coord)
                screen.blit(wn_image, loc)

    #display checkmate or draw or check
    if board['checkmate']:
        checkmate_display = font.render('CHECKMATE!!!', True, (255,0,0))
        pygame.draw.rect(screen,(255,255,255),[checkmate_loc[0],checkmate_loc[1],250,32])
        screen.blit(checkmate_display, checkmate_loc)
    elif board['draw']:
        draw_display = font.render('DRAW!!', True, (0,0,0))
        pygame.draw.rect(screen,(255,255,255),[draw_loc[0]-15,draw_loc[1],150,32])
        screen.blit(draw_display, draw_loc)
    elif board['check']:
        check_display = font.render('CHECK!', True, (255,0,0))
        screen.blit(check_display, check_loc)

    #update board after all changes
    pygame.display.update()

    return


def pygame_to_coord(location):
    """Converts x by y pixel coordinate to coordinate used in board."""
    coord = 0
    left_edge = board_loc[0] + left_len
    right_edge = board_loc[0] + board_dim[0] - right_len
    top_edge = board_loc[1] + top_len
    bottom_edge = board_loc[1] + board_dim[1] - bottom_len

    if (left_edge < location[0] < right_edge) and (top_edge < location[1] < bottom_edge):
        ones = ((location[0] - left_edge) // square_hori) + 1
        tens = (8 - ((location[1] - top_edge) // square_vert)) * 10
        coord = int(ones + tens)
    else:
        pass

    return coord


def create_board():
    """Generates a new chess board dictionary and populates the board with pieces."""

    # generate all 64 coordinates on board
    coord_list = generate_coord()

    # make board dictionary
    board = {}
    for coord in coord_list:
        board[coord] = '[]'

    # populate board
    for coord in board:
        if (20 < coord < 29) or (70 < coord < 79):  # pawns p
            board[coord] = 'p'
        elif coord in (11, 18, 81, 88):  # rooks r
            board[coord] = 'r'
        elif coord in (12, 17, 82, 87):  # knights n
            board[coord] = 'n'
        elif coord in (13, 16, 83, 86):  # bishops b
            board[coord] = 'b'
        elif coord in (14, 84):  # queens q
            board[coord] = 'q'
        elif coord in (15, 85):  # kings k
            board[coord] = 'k'
        else:
            pass

    # specify color of each piece
    for coord in board:
        if (10 < coord < 29):
            board[coord] = 'w' + board[coord]
        elif (70 < coord < 89):
            board[coord] = 'b' + board[coord]
        else:
            pass

    # add castling
    board['wqc'] = False
    board['wkc'] = False
    board['bqc'] = False
    board['bkc'] = False
    board['wk_moved'] = False
    board['wqr_moved'] = False
    board['wkr_moved'] = False
    board['bk_moved'] = False
    board['bqr_moved'] = False
    board['bkr_moved'] = False

    #add en passant
    board['epwb'] = 0
    board['epbw'] = 0

    # add statuses
    board['check'] = False
    board['checkmate'] = False
    board['draw'] = False

    # name to declare turn/winner
    board['bw'] = 'Black'
    board['wb'] = 'White'

    return board


def generate_coord():
    """Generates all 64 coordinates on the board."""
    coord_list = []
    for i in range(10, 90, 10):
        for j in range(1, 9):
            coord_list.append(i + j)

    return coord_list


def castle_scan():
    """Updates the global board state on potential castling opportunities."""
    global board
    
    def runway_open(board, enemy_move_space, region):
        """Returns True if the runway is open for castling."""
        status = True
        runway_dict = {'wqc':[12, 13, 14],
                       'wkc':[16, 17],
                       'bqc':[82, 83, 84],
                       'bkc':[86, 87]}
        king_runway_dict = {'wqc':[13, 14],
                            'wkc':[16, 17],
                            'bqc':[83, 84],
                            'bkc':[86, 87]}

        for coord in runway_dict[region]:
            if board[coord] != '[]':
                status = False
        for coord in king_runway_dict[region]:
            if coord in enemy_move_space:
                status = False

        return status

        """Returns True if the path is open for black king-side castling."""
        status = True
        runway = [86, 87]

        for coord in runway:
            if board[coord] != '[]':
                status = False
            elif coord in white_move_space:
                status = False

        return status

    def moved(status, piece, coord):
        """Changes moved status of moved pieces in can_castle to True."""
        global board
        

        if board[status] == True:
            pass
        else:
            if board[coord] != piece:
                board[status] = True

        return

    # find move spaces to check if runways are clear
    white_move_space = find_enemy_move_space(board, 'bw')
    black_move_space = find_enemy_move_space(board, 'wb')

    # Bool on whether runway is clear
    wqc_free = runway_open(board, black_move_space,'wqc')
    wkc_free = runway_open(board, black_move_space,'wkc')
    bqc_free = runway_open(board, white_move_space,'bqc')
    bkc_free = runway_open(board, white_move_space,'bkc')

    # check if pieces have moved
    moved('wk_moved', 'wk', 15)
    moved('bk_moved', 'bk', 85)

    moved('wqr_moved', 'wr', 11)
    moved('wkr_moved', 'wr', 18)
    moved('bqr_moved', 'br', 81)
    moved('bkr_moved', 'br', 88)

    # check if kings are in check
    w_check = False
    b_check = False

    if (not board['wk_moved']):
        if 15 in black_move_space:
            w_check = True

    if (not board['bk_moved']):
        if 85 in white_move_space:
            b_check = True

    # change castling status
    if (wqc_free) and (not board['wk_moved']) and (not board['wqr_moved']) and (not w_check):
        board['wqc'] = True
    else:
        board['wqc'] = False

    if (wkc_free) and (not board['wk_moved']) and (not board['wkr_moved']) and (not w_check):
        board['wkc'] = True
    else:
        board['wkc'] = False

    if (bqc_free) and (not board['bk_moved']) and (not board['bqr_moved']) and (not b_check):
        board['bqc'] = True
    else:
        board['bqc'] = False

    if (bkc_free) and (not board['bk_moved']) and (not board['bkr_moved']) and (not b_check):
        board['bkc'] = True
    else:
        board['bkc'] = False

    return


def move_piece(start, end): 
    """Moves a chess piece on the board within legal moves."""
    global board
    global draw

    def exec_ep(start, end):
        """Records potential en passants and executes en passant kill."""
        global board

        # en passant recorded
        if (board[start] == 'wp') and (20 < start < 29) and (40 < end < 49):
            board['epwb'] = start
        elif (board[start] == 'bp') and (70 < start < 79) and (50 < end < 59):
            board['epbw'] = start

        # execute en passant
        if (board[start] == 'wp') and (board[end] == '[]') and ((end + 10) == board['epbw']):
            board = del_piece(board, end - 10)
        elif (board[start] == 'bp') and (board[end] == '[]') and ((end - 10) == board['epwb']):
            board = del_piece(board, end + 10)

        return


    def exec_castle(start, end):
        """Moves the rook if castling as occurred."""
        global board

        if (board['wqc'] == True) and (start == 15) and (end == 13):
            board = move(board, 11, 14)
        elif (board['wkc'] == True) and (start == 15) and (end == 17):
            board = move(board, 18, 16)
        elif (board['bqc'] == True) and (start == 85) and (end == 83):
            board = move(board, 81, 84)
        elif (board['bkc'] == True) and (start == 85) and (end == 87):
            board = move(board, 88, 86)

        return


    # draw "pawn or kill" counter
    if (board[start][1] == 'p') or (board[end] != '[]'):
        draw['pork'] = 0
    else:
        draw['pork'] += 1

    # execute move
    if board['draw'] == False:
        # en passant
        exec_ep(start, end)
        #castling
        exec_castle(start, end)
        # general move
        board = move(board, start, end)

    return


def find_move_space(board, turn, start, kills_only):
    """Returns a set of all basic moves for a piece on the board."""

    move_space = set()
    piece = board[start][1]

    # generate all 64 coordinates on board
    coord_list = generate_coord()

    # assign moves to move space
    if piece == 'p':
        if board[start][0] == 'w':
            if (kills_only):
                pass
            else:
                if board[start + 10] == '[]':
                    move_space.add(start + 10)
                if start < 30:
                    if (board[start + 10] == '[]') and (board[start + 20] == '[]'):
                        move_space.add(start + 20)
            # normal attack
            for attack in [9, 11]:
                new_spot = start + attack
                if new_spot not in coord_list:
                    continue
                elif board[new_spot][0] == 'b':
                    move_space.add(new_spot)
            # en passant
            for potential_ep in [-1, 1]:
                new_spot = start + potential_ep
                if new_spot not in coord_list:
                    continue
                elif (50 < start < 59) and (board[new_spot] == 'bp') and (board['epbw'] == (new_spot + 20)):
                    move_space.add(new_spot + 10)
        elif board[start][0] == 'b':
            if (kills_only):
                pass
            else:
                if board[start - 10] == '[]':
                    move_space.add(start - 10)
                if start > 70:
                    if (board[start - 10] == '[]') and (board[start - 20] == '[]'):
                        move_space.add(start - 20)
            for attack in [-9, -11]:
                new_spot = start + attack
                if new_spot not in coord_list:
                    continue
                elif board[new_spot][0] == 'w':
                    move_space.add(new_spot)
            for potential_ep in [-1, 1]:
                new_spot = start + potential_ep
                if new_spot not in coord_list:
                    continue
                elif (40 < start < 49) and (board[new_spot] == 'wp') and (board['epwb'] == (new_spot - 20)):
                    move_space.add(new_spot - 10)
    elif piece == 'r':
        rook_moves = [1, -1, 10, -10]
        for rook_move in rook_moves:
            for x in range(1, 9):
                new_spot = start + rook_move * x
                if (new_spot not in coord_list) or (board[new_spot][0] == turn[0]):
                    break
                elif board[new_spot][0] == turn[1]:
                    move_space.add(new_spot)
                    break
                else:
                    move_space.add(new_spot)
    elif piece == 'n':
        knight_moves = [21, 12, -21, -12, 8, 19, -8, -19]
        for knight_move in knight_moves:
            new_spot = start + knight_move
            if (new_spot in coord_list) and (board[new_spot][0] != turn[0]):
                move_space.add(new_spot)
            else:
                continue
    elif piece == 'b':
        bishop_moves = [11, -11, 9, -9]
        for bishop_move in bishop_moves:
            for x in range(1, 9):
                new_spot = start + bishop_move * x
                if (new_spot not in coord_list) or (board[new_spot][0] == turn[0]):
                    break
                elif board[new_spot][0] == turn[1]:
                    move_space.add(new_spot)
                    break
                else:
                    move_space.add(new_spot)
    elif piece == 'q':
        queen_moves = [1, -1, 10, -10, 11, -11, 9, -9]
        for queen_move in queen_moves:
            for x in range(1, 9):
                new_spot = start + queen_move * x
                if (new_spot not in coord_list) or (board[new_spot][0] == turn[0]):
                    break
                elif board[new_spot][0] == turn[1]:
                    move_space.add(new_spot)
                    break
                else:
                    move_space.add(new_spot)
    elif piece == 'k':
        king_moves = [10, -10, 1, -1, 11, -11, 9, -9]
        for king_move in king_moves:
            new_spot = start + king_move
            if (new_spot in coord_list) and (board[new_spot][0] != turn[0]):
                move_space.add(new_spot)
            else:
                continue
        # castling
        for possible_castle in ['wqc', 'wkc', 'bqc', 'bkc']:
            if (board[possible_castle] == True) and (possible_castle[0] == turn[0]) and (not kills_only):
                if possible_castle == 'wqc':
                    move_space.add(13)
                elif possible_castle == 'wkc':
                    move_space.add(17)
                elif possible_castle == 'bqc':
                    move_space.add(83)
                elif possible_castle == 'bkc':
                    move_space.add(87)
    else:
        pass

    return move_space


def possible_start(board, turn, start):
    """Returns True if moving the starting piece will not result in checkmate."""
    status = True
    move_space = find_move_space(board, turn, start, False)

    if move_space == set():
        status = False
    else:
        # test all possible moves for a counter move
        counter_exists = False
        for possible_move in move_space:
            temp_board = move(board, start, possible_move)
            enemy_move_space = find_enemy_move_space(temp_board, turn)
            # find coordinate of ally king
            for coord in temp_board:
                if temp_board[coord] == turn[0] + 'k':
                    king_coord = coord
            # check if king is in enemy move space
            if king_coord not in enemy_move_space:
                counter_exists = True
        # return False if no counter moves exist
        if not counter_exists:
            status = False

    return status


def viable_move(board, turn, start, end):
    """Returns True if the move will not result in checkmate."""
    status = True
    temp_board = move(board, start, end)
    enemy_move_space = find_enemy_move_space(temp_board, turn)

    # find coordinate of ally king
    coord_list = generate_coord()
    for coord in coord_list:
        if temp_board[coord] == turn[0] + 'k':
            king_coord = coord

    # check if move is in move space
    starting_move_space = find_move_space(board, turn, start, False)
    if end not in starting_move_space:
        status = False
    # check if king is in enemy move space
    elif king_coord in enemy_move_space:
        status = False

    return status


def find_enemy_move_space(board, turn):
    """Returns a set of all possible moves by the enemy."""
    enemy_move_space = set()
    enemy_coord = []

    # generate all 64 coordinates on board
    coord_list = generate_coord()

    # find location of all enemy pieces
    for coord in coord_list:
        if board[coord][0] == turn[1]:
            enemy_coord.append(coord)

    # find union of move spaces of all enemy pieces
    for enemy_piece in enemy_coord:
        enemy_move_space = enemy_move_space.union(find_move_space(
            board, turn[1] + turn[0], enemy_piece, True))

    return enemy_move_space


def move(board, start, end):
    """Returns board after a move has been made."""
    new_board = board.copy()
    new_board[end] = new_board[start]
    new_board[start] = '[]'
    return new_board


def del_piece(board, coord):
    """Turns a selected coordinate on the board into an empty square."""
    new_board = board.copy()
    new_board[coord] = '[]'
    return new_board


def pawn_scan():
    """Promotes pawn that reach other side of board."""
    global board

    def display_upgrades(upgrades_list):
        """Displays the choice of upgrades for a pawn."""
        
        #add text
        upgrade_text_1 = font.render('Choose an',True,(255,255,255))
        upgrade_text_2 = font.render('upgrade:',True,(255,255,255))
        screen.blit(upgrade_text_1, upgrade_loc)
        screen.blit(upgrade_text_2, (upgrade_loc[0],upgrade_loc[1]+32))

        #add images of pieces
        for n in [0,1,2,3]:
            loc = (upgrade_loc[0] + square_hori*n, upgrade_loc[1] + 80)
            screen.blit(upgrades_list[n], loc)

        pygame.display.update()

        return

    def pygame_to_choice(location):
        """Converts x by y pixel coordinate to choice of upgrade."""
        choice = 0
        left_edge = upgrade_loc[0]
        right_edge = upgrade_loc[0] + 4*square_hori
        top_edge = upgrade_loc[1] + 80
        bottom_edge = upgrade_loc[1] + 80 + square_vert

        if not(left_edge < location[0] < right_edge) or not(top_edge < location[1] < bottom_edge):
            pass
        else:
            choice = ((location[0] - upgrade_loc[0]) // square_hori) + 1

        return choice

    white_upgrades = [wq_image,wr_image,wb_image,wn_image]
    black_upgrades = [bq_image,br_image,bb_image,bn_image]

    for coord in range(81, 89):
        if board[coord] == 'wp':
            asking = True
            while asking:
                display_upgrades(white_upgrades)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_press = pygame.mouse.get_pos()
                        choice = pygame_to_choice(mouse_press)
                        #upgrade pawn
                        if 0 < choice < 5:
                            if choice == 1:
                                board[coord] = 'wq'
                            elif choice == 2:
                                board[coord] = 'wr'
                            elif choice == 3:
                                board[coord] = 'wb'
                            elif choice == 4:
                                board[coord] = 'wn'
                            asking = False



    for coord in range(11, 19):
        if board[coord] == 'bp':
            asking = True
            while asking:
                display_upgrades(black_upgrades)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_press = pygame.mouse.get_pos()
                        choice = pygame_to_choice(mouse_press)
                        #upgrade pawn
                        if 0 < choice < 5:
                            if choice == 1:
                                board[coord] = 'bq'
                            elif choice == 2:
                                board[coord] = 'br'
                            elif choice == 3:
                                board[coord] = 'bb'
                            elif choice == 4:
                                board[coord] = 'bn'
                            asking = False

    return


def checkmate_scan(): 
    """Declares the winner and ends the game if checkmate has been achieved."""
    global board
    global turn

    checkmate = True
    enemy_coord = []

    # generate all 64 coordinates on board
    coord_list = generate_coord()

    # find location of all enemy pieces
    for coord in coord_list:
        if board[coord][0] == turn[1]:
            enemy_coord.append(coord)

    # turn off checkmate status if possible
    for enemy_piece in enemy_coord:
        if possible_start(board, (turn[1] + turn[0]), enemy_piece):
            checkmate = False
        elif (board[enemy_piece] == turn[1] + 'k'):
            ally_move_space = find_enemy_move_space(board, (turn[1] + turn[0]))
            if enemy_piece not in ally_move_space:
                checkmate = False
        else:
            continue

    # if checkmate still stands, change board state
    if checkmate == True:
        board['checkmate'] = True

    return


def draw_scan():
    """Declares a draw and ends the game if one of the draw conditions has been achieved."""
    global board
    global draw

    draw['board_list'].append(board.copy())

    # 50 move rule draw
    if draw['pork'] == 100:
        board['draw'] = True

    # insufficient material draw
    def insuff_scan(board):
        """Returns True if there is insufficient material to achieve checkmate."""
        status = False

        coord_list = generate_coord()

        # list all black squares
        black_squares = []
        for tens in range(10, 81, 10):
            if tens % 20 == 10:
                for ones in range(1, 9, 2):
                    black_squares.append(tens + ones)
            elif tens % 20 == 0:
                for ones in range(2, 9, 2):
                    black_squares.append(tens + ones)

        # list all white squares
        white_squares = []
        for tens in range(10, 81, 10):
            if tens % 20 == 0:
                for ones in range(1, 9, 2):
                    white_squares.append(tens + ones)
            elif tens % 20 == 10:
                for ones in range(2, 9, 2):
                    white_squares.append(tens + ones)

        # list remaining pieces
        white_pieces = []
        black_pieces = []
        for coord in coord_list:
            if board[coord][0] == 'w':
                white_pieces.append(board[coord][1])
            elif board[coord][0] == 'b':
                black_pieces.append(board[coord][1])
        white_pieces.sort()
        black_pieces.sort()

        # insufficient material cases
        if black_pieces == ['k']:
            if (white_pieces == ['k']) or (white_pieces == ['b', 'k']) or (white_pieces == ['k', 'n']):
                status = True
            elif white_pieces == ['b', 'b', 'k']:
                bishop_coords = set()
                for coord in coord_list:
                    if board[coord][1] == 'b':
                        bishop_coords.add(coord)
                # if both pieces on black or on white, then True
                if (len(bishop_coords.intersection(black_squares)) == 2) or (
                        len(bishop_coords.intersection(white_squares)) == 2):
                    status = True
        elif black_pieces == ['b', 'k']:
            if white_pieces == ['b', 'b', 'k']:
                bishop_coords = set()
                for coord in coord_list:
                    if board[coord][1] == 'b':
                        bishop_coords.add(coord)
                # if all pieces on black or on white, then True
                if (len(bishop_coords.intersection(black_squares)) == 3) or (
                        len(bishop_coords.intersection(white_squares)) == 3):
                    status = True
        elif white_pieces == ['k']:
            if (black_pieces == ['k']) or (black_pieces == ['b', 'k']) or (black_pieces == ['k', 'n']):
                status = True
            elif black_pieces == ['b', 'b', 'k']:
                bishop_coords = set()
                for coord in coord_list:
                    if board[coord][1] == 'b':
                        bishop_coords.add(coord)
                # if both pieces on black or on white, then True
                if (len(bishop_coords.intersection(black_squares)) == 2) or (
                        len(bishop_coords.intersection(white_squares)) == 2):
                    status = True
        elif white_pieces == ['b', 'k']:
            if black_pieces == ['b', 'b', 'k']:
                bishop_coords = set()
                for coord in coord_list:
                    if board[coord][1] == 'b':
                        bishop_coords.add(coord)
                # if all pieces on black or on white, then True
                if (len(bishop_coords.intersection(black_squares)) == 3) or (
                        len(bishop_coords.intersection(white_squares)) == 3):
                    status = True

        return status

    if insuff_scan(board):
        board['draw'] = True

    # stalemate draw
    def stalemate_scan():
        """Changes the draw status if a stalemate has occured."""
        global board
        global turn
        global draw

        enemy_coord = []
        can_move = False

        # generate all 64 coordinates on board
        coord_list = generate_coord()

        # find location of all enemy pieces
        for coord in coord_list:
            if board[coord][0] == turn[1]:
                enemy_coord.append(coord)

        # if an enemy piece can move, prevent stalemate from being True
        for enemy_piece in enemy_coord:
            if possible_start(board, turn[1]+turn[0], enemy_piece):
                can_move = True
            else:
                continue

        # if no piece can move, declare stalemate
        if can_move:
            pass
        else:
            board['draw'] = True

        return
    
    stalemate_scan()

    # threefold repetition draw
    for board_state in draw['board_list']:
        repeat = 0
        other_boards = draw['board_list'].copy()
        other_boards.remove(board_state)
        for other_board_state in other_boards:
            if board_state == other_board_state:
                repeat += 1
        if repeat == 2:
            board['draw'] = True

    return


def check_scan(): 
    """Changes check status to True if a king has been "checked"."""
    global board
    global turn

    board['check'] = False
    enemy_move_space = find_enemy_move_space(board, turn)

    # find coordinate of ally king
    for coord in board:
        if board[coord] == turn[0] + 'k':
            king_coord = coord

    # check if king is in enemy move space
    if king_coord in enemy_move_space:
        board['check'] = True

    return


def change_turn():
    """Changes the turn from black to white and white to black, and counts the turns elapsed."""
    global board
    global turn
    global turn_num

    # proceed to next turn number if it was black move
    if turn == 'wb':
        turn_num = turn_num
    else:
        turn_num += 1

    # change move from white to black or black to white
    turn = turn[1] + turn[0]

    # remove en passant of previous move
    board['ep' + turn] = 0  # note turn was changed upstream

    return

# -----------------------------------------------
# -------------------GAME CODE-------------------
# -----------------------------------------------
global board
global turn
global turn_num
global draw

# initial state
board = create_board()
turn = 'wb'
turn_num = 1
draw = {'pork': 0, 'board_list': [board.copy()]}
select = False

# Game Loop
running = True
while running:
    
    check_scan()
    castle_scan()
    
    # User Interaction Loop
    deciding = True
    while deciding:
        for event in pygame.event.get():
            # QUIT button
            if event.type == pygame.QUIT:
                deciding = False
                running = False
            # pauses board when game ends
            elif board['draw'] or board['checkmate']:
                display_board()
                pass
            #normal turn loop
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_press = pygame.mouse.get_pos()
                mouse_coord = pygame_to_coord(mouse_press)
                # find and highlight move space
                if (select == False) and (10 < mouse_coord < 89):
                    if (board[mouse_coord][0] == turn[0]) and possible_start(board,turn,mouse_coord):
                        select = True
                        start = mouse_coord
                        move_space = set()
                        for possible_move in find_move_space(board,turn,start,False):
                            if viable_move(board,turn,start,possible_move):
                                move_space.add(possible_move)
                # choose movement
                elif (select == True) and (mouse_coord in move_space):
                        end = mouse_coord
                        move_piece(start, end)
                        select = False
                        deciding = False
                # unhighlight move space
                elif (select == True) and (mouse_coord not in move_space):
                    select = False
        
        # update screen
        display_board()

    #upgrade any pawns
    pawn_scan()

    # endgame scans
    checkmate_scan()
    draw_scan()

    change_turn()


pygame.quit()
