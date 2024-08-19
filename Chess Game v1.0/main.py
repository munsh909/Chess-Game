import pygame as py
import operator

py.init()

WIDTH = 1000
HEIGHT = 900

screen = py.display.set_mode([WIDTH,HEIGHT])

font = py.font.Font('freesansbold.ttf',20)
bigfont = py.font.Font('freesansbold.ttf',40)

clock = py.time.Clock() #Sets up timer

fps = 60

#all variables

#game variables and images

white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
white_locations = [(0,0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
black_locations = [(0,7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]

all_locations = white_locations + black_locations

piece_move_list = {
        'pawn' : [(0,1),(0,2),(1,1),(-1,1)],
        'rook': [(0,1),(0,-1),(1,0),(-1,0)],
        'bishop': [(1,1),(-1,1),(-1,-1),(1,-1)],
        'queen' : [(1,1),(-1,1),(-1,-1),(1,-1),(0,1),(0,-1),(1,0),(-1,0)],
        'king' : [(1,1),(-1,1),(-1,-1),(1,-1),(0,1),(0,-1),(1,0),(-1,0)],
        'knight': [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
    }


captured_pieces_white = []
captured_pieces_black = []

turn_step = 0 #0 = whites turn no selection. 1 = whites turn, selected. 2 = black, no selection. 3 = black, selected
selection = 100 #Holds which piece has been selected
valid_moves = [] #holds valid moves of a seleted pieces

# load in game piece images (queen, king, rook, bishop, knight, pawn) x 2
black_queen = py.image.load('assets/images/black queen.png')
black_queen = py.transform.scale(black_queen, (80, 80))
black_queen_small = py.transform.scale(black_queen, (45, 45))
black_king = py.image.load('assets/images/black king.png')
black_king = py.transform.scale(black_king, (80, 80))
black_king_small = py.transform.scale(black_king, (45, 45))
black_rook = py.image.load('assets/images/black rook.png')
black_rook = py.transform.scale(black_rook, (80, 80))
black_rook_small = py.transform.scale(black_rook, (45, 45))
black_bishop = py.image.load('assets/images/black bishop.png')
black_bishop = py.transform.scale(black_bishop, (80, 80))
black_bishop_small = py.transform.scale(black_bishop, (45, 45))
black_knight = py.image.load('assets/images/black knight.png')
black_knight = py.transform.scale(black_knight, (80, 80))
black_knight_small = py.transform.scale(black_knight, (45, 45))
black_pawn = py.image.load('assets/images/black pawn.png')
black_pawn = py.transform.scale(black_pawn, (65, 65))
black_pawn_small = py.transform.scale(black_pawn, (45, 45))
white_queen = py.image.load('assets/images/white queen.png')
white_queen = py.transform.scale(white_queen, (80, 80))
white_queen_small = py.transform.scale(white_queen, (45, 45))
white_king = py.image.load('assets/images/white king.png')
white_king = py.transform.scale(white_king, (80, 80))
white_king_small = py.transform.scale(white_king, (45, 45))
white_rook = py.image.load('assets/images/white rook.png')
white_rook = py.transform.scale(white_rook, (80, 80))
white_rook_small = py.transform.scale(white_rook, (45, 45))
white_bishop = py.image.load('assets/images/white bishop.png')
white_bishop = py.transform.scale(white_bishop, (80, 80))
white_bishop_small = py.transform.scale(white_bishop, (45, 45))
white_knight = py.image.load('assets/images/white knight.png')
white_knight = py.transform.scale(white_knight, (80, 80))
white_knight_small = py.transform.scale(white_knight, (45, 45))
white_pawn = py.image.load('assets/images/white pawn.png')
white_pawn = py.transform.scale(white_pawn, (65, 65))
white_pawn_small = py.transform.scale(white_pawn, (45, 45))
white_images = [white_pawn, white_queen, white_king, white_knight, white_rook, white_bishop] #Loads up the images more easily
small_white_images = [white_pawn_small, white_queen_small, white_king_small, white_knight_small,
                      white_rook_small, white_bishop_small]
black_images = [black_pawn, black_queen, black_king, black_knight, black_rook, black_bishop]
small_black_images = [black_pawn_small, black_queen_small, black_king_small, black_knight_small,
                      black_rook_small, black_bishop_small]
piece_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']

#Unified variable list


#draw board

def drawboard():
    for i in range(32): #Only 32 as we only need the off colour squares
        row = i // 4 
        col = i % 4 # so 3 columns as it iterates, but 8 rows, only need the columns with grey squares
        
        if row % 2 == 0:
            py.draw.rect(screen, 'light gray', [600 - (col * 200), row * 100, 100, 100])#last 2 args are square size
        else:
            py.draw.rect(screen, 'light gray', [700 - (col * 200), row * 100, 100, 100])
        
            
        py.draw.rect(screen, 'gold',[0,800,WIDTH,100])
        py.draw.rect(screen, 'black',[0,800,WIDTH,100],5)    
        py.draw.rect(screen, 'gold', [800, 0, 200, HEIGHT], 5) #border going up
        
        status_text = ['White: Select a Piece to Move!', 'White: Select a Destination!',
                       'Black: Select a Piece to Move!', 'Black: Select a Destination!']
        screen.blit(bigfont.render(status_text[turn_step], True, 'black'), (20, 820)) # renders the text
        
        for i in range(9):
            py.draw.line(screen, 'black', (0, 100 * i), (800, 100 * i), 2) #from 0 to 800 in increments of i
            py.draw.line(screen, 'black', (100 * i, 0), (100 * i, 800), 2)
               
# Various functions to help calculate valid moves

def addcoords(coord1,coord2):
    ans = tuple(map(operator.add, coord1, coord2))
    return ans

def add_multiple_coords(loc, array):
    answer = [addcoords(loc,i) for i in array]
    return answer

def update_locations(location):
    whiteloc = white_locations.copy()
    blackloc = black_locations.copy()
    all_locations = whiteloc + blackloc
    if location not in all_locations:
        return
    
    if location in whiteloc:
        ally_locs = whiteloc
        enemy_locs = blackloc
    else:
        ally_locs = blackloc
        enemy_locs = whiteloc
        
    ally_locs.remove(location)
    all_locations.remove(location)
    
    return ally_locs, enemy_locs, all_locations

def return_valid_moves(diff, loc):
    ally_locs, enemy_locs, all_locations = update_locations(loc)
    
    x = loc
    
    answer = []
    
    while (-1 < x[0] < 8) and (-1 < x[1] < 8):
        if x in ally_locs:
            break
        if x in enemy_locs:
            answer.append(x)
            break
        
        answer.append(x)
        x = addcoords(x, diff)
        
    if loc in answer:
        answer.remove(loc)
        
    a, b = diff
        
    neg_diff = (-a, -b)
    
    x = loc
    
    while (-1 < x[0] < 8) and (-1 < x[1] < 8):
        if x in ally_locs:
            break
        if x in enemy_locs:
            answer.append(x)
            break
        
        answer.append(x)
        x = addcoords(x, neg_diff)
        
    if loc in answer:
        answer.remove(loc)
    
    return answer
    
def is_move_valid(loc, array):
    if array is None:
        return
    
    ally_locs, enemy_locs, all_locations = update_locations(loc)
    
    
    
    arr = []
    
    for i in array:
        if i in ally_locs:
            continue
        if (-1 < i[0] < 8):
            continue
        if (-1 < i[1] < 8):
            continue
        arr.append(i)
        
    return arr
        
        
    
    
    
    



#Methods to check valid moves based on move type
def validpawnmoves(loc):
    ally_locs, enemy_locs, all_locations = update_locations(loc)
    
    if loc in white_locations:
        up_right = (1,1)
        up_left = (-1,1)
        up_one = (0,1)
        up_two = (0,2)
        if loc[1] == 1:
            initial_state = True
        else:
            initial_state = False
    else:
        up_right = (-1,-1)
        up_left = (1,-1)
        up_one = (0,-1)
        up_two = (0,-2)   
        if loc[1] == 6:
            initial_state = True
        else:
            initial_state = False
    upright = addcoords(loc, up_right)
    upleft = addcoords(loc,up_left)
    
    valmoves = []
    
    if upright in enemy_locs:
        valmoves.append(upright)
        
    if upleft in enemy_locs:
        valmoves.append(upleft)
        
    upone = addcoords(loc,up_one)
    
    uptwo = addcoords(loc, up_two)
    
    if initial_state:
        possible_moves = [upone,uptwo]
    else:
        possible_moves = [upone]
    
    verticalmoves = [i for i in possible_moves if i not in all_locations]
    
    valid_moves = valmoves + verticalmoves
    
    return valid_moves
    
def validknightmoves(loc):
    
    arrayofmoves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
    
    possiblemoves = add_multiple_coords(loc, arrayofmoves)
    
    ally_locs, enemy_locs, all_locations = update_locations(loc)
    
    good_possible_moves = [i for i in possiblemoves if i not in ally_locs]
    
    final_possible_moves = [i for i in good_possible_moves if ((-1 < i[0] < 8) & (-1 < i[1] < 8))]
    
    return final_possible_moves 

def validbishopmoves(loc):
    arr = return_valid_moves((1,1), loc) + return_valid_moves((-1,1), loc)
    return arr

def validrookmoves(loc):
    arr =  return_valid_moves((0,1), loc) + return_valid_moves((1,0), loc)
    return arr
    
def validqueenmoves(loc):
    arr = validrookmoves(loc) + validbishopmoves(loc)
    return arr

def validkingmoves(loc):
    possiblemoves = [(1,1),(-1,1),(-1,-1),(1,-1),(0,1),(0,-1),(1,0),(-1,0)]
    totalmoves = add_multiple_coords(loc, possiblemoves)
    checked_moves = is_move_valid(loc, totalmoves)
    if loc in white_locations:
        answer = [i for i in checked_moves if i not in option_list('black')]
    else:
        answer = [i for i in checked_moves if i not in option_list('white')]
    return checked_moves

def valid_piece_moves(loc):
    if loc in white_locations:
        location_index = white_locations.index(loc)
        piece = white_pieces[location_index]
    
    if loc in black_locations:
        location_index = black_locations.index(loc)
        piece = black_pieces[location_index]
    
    if piece == 'rook':
        arr =  validrookmoves(loc)
        
    if piece == 'king':
        arr =  validkingmoves(loc)
    
    if piece == 'pawn':
        arr = validpawnmoves(loc)
    
    if piece == 'knight':
        arr = validknightmoves(loc)
    
    if piece == 'bishop':
        arr = validbishopmoves(loc)
    
    if piece == 'queen':
        arr = validqueenmoves(loc)
    
    if loc in arr:
        arr.pop(loc)
        
    return arr

def drawpieces():
    for i in range(len(white_pieces)):
        index = piece_list.index(white_pieces[i])
        if white_pieces[i] == 'pawn':
            screen.blit(white_pawn, (white_locations[i][0] * 100 + 22, white_locations[i][1] * 100 + 30))
        else:
            screen.blit(white_images[index], (white_locations[i][0] * 100 + 10, white_locations[i][1] * 100 + 10))
        if turn_step < 2:
            if selection == i:
                py.draw.rect(screen, 'red', [white_locations[i][0] * 100 + 1, white_locations[i][1] * 100 + 1,
                                                 100, 100], 2)

    for i in range(len(black_pieces)):
        index = piece_list.index(black_pieces[i])
        if black_pieces[i] == 'pawn':
            screen.blit(black_pawn, (black_locations[i][0] * 100 + 22, black_locations[i][1] * 100 + 30))
        else:
            screen.blit(black_images[index], (black_locations[i][0] * 100 + 10, black_locations[i][1] * 100 + 10))
        if turn_step >= 2:
            if selection == i:
                py.draw.rect(screen, 'blue', [black_locations[i][0] * 100 + 1, black_locations[i][1] * 100 + 1,
                                                  100, 100], 2)

def check_king():
    if turn_step <= 1:  # White's turn
        king_loc = white_locations[white_pieces.index('king')]
        enemy_color = 'black'
    else:  # Black's turn
        king_loc = black_locations[black_pieces.index('king')]
        enemy_color = 'white'

    if king_loc in option_list(enemy_color):
        py.draw.rect(screen, 'dark red', [king_loc[0] * 100 + 1, king_loc[1] * 100 + 1, 100, 100], 5)
        return True

    return False

        

    
def highlight_piece_moves(loc, array):
    if turn_step < 2:
        color = 'red'
    else:
        color = 'blue'
    
    possiblemoves = array
    
    for i in range(len(possiblemoves)):
        py.draw.circle(screen, color, (possiblemoves[i][0] * 100 + 50, possiblemoves[i][1] * 100 + 50), 5)
    


# All possible moves white and black
def option_list(color):
    possmoves = []
    if color == 'white':
        pieces = white_pieces
        locations = white_locations
    if color == 'black':
        pieces = black_pieces
        locations = black_locations
    for i in range(len(pieces)):
        piecemoves = valid_piece_moves(locations[i])
        if piecemoves is not None:
            possmoves = possmoves + piecemoves
    return list(set(possmoves))
    
    


#main game loop



run = True

while run:
    clock.tick(fps)
    screen.fill('dark green')
        
    
    drawboard()
    drawpieces()
    check_king()
    
    
    
    if selection != 100: # So if a piece has been selected...
        if turn_step <=1:
            selected_loc = white_locations[selection]
            valid_moves = valid_piece_moves(selected_loc)
            highlight_piece_moves(selected_loc, valid_moves)
        if turn_step > 1:
            selected_loc = black_locations[selection]
            valid_moves = valid_piece_moves(selected_loc)
            highlight_piece_moves(selected_loc, valid_moves)

            
            
        
    
    #event handling
    # pawn works
    # rook does not work
    # knight works
    # bishop works
    
    for event in py.event.get():
        if event.type == py.QUIT:
            run = False # exits game loop if quit
    if event.type == py.MOUSEBUTTONDOWN and event.button == 1:
            x_coord = event.pos[0] // 100
            y_coord = event.pos[1] // 100
            click_coords = (x_coord, y_coord)  # finds coordinates of x and y
            
            #Check which piece is moving
            
            
            if turn_step <= 1: #so if it is a white piece moving
                
                if click_coords in white_locations:
                    selection = white_locations.index(click_coords)
                    
                if turn_step == 0:
                    turn_step = 1
                    
                #First select the piece you wish to move
                
                if (click_coords in valid_moves) and selection != 100:
                    # If capturing another piece...
                    if (click_coords in black_locations):
                        captured_black_selection = black_locations.index(click_coords)
                        #Add to captured pieces for white
                        captured_pieces_white.append(black_pieces[captured_black_selection])
                        #Remove from black pieces and black locations
                        black_pieces.pop(captured_black_selection)
                        black_locations.pop(captured_black_selection)
                        #update white pieces
                        white_locations[selection] = click_coords
                    white_locations[selection] = click_coords
                    selection = 100
                    turn_step = 2
                    
                        
            if turn_step > 1: #so if it is a black piece moving
                if click_coords in black_locations:
                    selection = black_locations.index(click_coords)
                    
                if turn_step == 2:
                    turn_step = 3
                if (click_coords in valid_moves) and selection != 100:
                    # If capturing another piece...
                    if (click_coords in white_locations):
                        capwhiteselected = white_locations.index(click_coords)
                        #Add to captured pieces for black
                        captured_pieces_black.append(white_pieces[capwhiteselected])
                        #Remove from white pieces and white locations
                        white_pieces.pop(capwhiteselected)
                        white_locations.pop(capwhiteselected)
                        #update black pieces
                        black_locations[selection] = click_coords
                    black_locations[selection] = click_coords
                    turn_step = 0
                    selection = 100
                
                        
    py.display.flip()
    
py.quit()