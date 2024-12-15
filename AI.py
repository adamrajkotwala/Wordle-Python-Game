import random # to generate random numbers
import sys
from word_list import * # access to word_list file that contains list of different 5 letter words
import pygame # pygame library for game development
import pdb

pygame.init() # initialize pygame

#DEFINING CONSTANTS

WIDTH, HEIGHT = 750, 1000 # dimensions of the display

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT)) # define screen with desired dimensions
BACKGROUND = pygame.image.load("design/Starting Tiles.png") # define background, load image with background tiles found online
BACKGROUND_RECTANGLE = BACKGROUND.get_rect(center=(375, 300)) # define background rectangle and center it
ICON = pygame.image.load("design/Icon.png") # define icon with character square image found online

pygame.display.set_caption("Wordle") # set header of pygame to wordle
pygame.display.set_icon(ICON) # set icon of pygame to icon image

# set colors with custom color tags

GREEN = "#6aaa64"
YELLOW = "#c9b458"
GREY = "#787c7e"
OUTLINE = "#d3d6da"
FILLED_OUTLINE = "#878a8c"

# set correct word

# CORRECT_WORD = random.choice(WORDS)
CORRECT_WORD = "games"

ALPHABET = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]

LETTER_FONT = pygame.font.Font("design/BrontidevpDemoStyle2-ZV8E3.otf", 50) # define a letter font variable with font file

# Restart Button
window = (750, 1000) # size of window
screen = pygame.display.set_mode(window) #screen to be used with button functionality

color = (255, 255, 255) #Font color of button
color_static = (170, 170, 170) #color of button when not hovering over (light grey)
color_dynamic = (140, 140, 140) #color of button when hovered (dark grey)

font = pygame.font.Font(None, 30) #font of button

button_width = 150 #Dimensions and relative position of the button
button_height = 50
button_x = (window[0] - button_width) / 2
button_y = window[1] - button_height - 40

button_surface = pygame.Surface((button_width, button_height)) #Creates button surface
button_surface.fill(color_static) #Makes the interior of the button light grey

text = font.render('Restart', True, color) #Creates text for the button
text_rect = text.get_rect(center=(button_width / 2, button_height / 2))
text_rect.center = (button_x + button_width / 2, button_y + button_height / 2) #Places text in the center of the button

boundaries = pygame.Rect(button_x, button_y, button_width, button_height) #Creates the clickable boundaries of the button

# setup display screen and display the background in the boundaries of "background rectangle"

SCREEN.fill("white")
SCREEN.blit(BACKGROUND, BACKGROUND_RECTANGLE)
pygame.display.update()

# define variables for spacing and size

LETTER_HORIZONTAL_SPACING = 85
LETTER_VERTICAL_SPACING = 12
LETTER_SIZE = 75

# define variables for guess count, 2D list to contain all guesses, a list for current guess, string for this guess, current letter spacing

guesses_count = 0
guesses = [[]] * 6
current_guess = []
current_guess_string = ""
current_letter_background_horizontal = 167.5
game_result = "" # string to represent the result of the game 
keyboard = []

# define a letter class for each individual "letter" block

class Letter:
    
    # function to initialize the letter with color, position, spacing
    
    def __init__(self, text, background_position):
        self.background_color = "white"
        self.text_color = "black"
        self.background_position = background_position
        self.background_position_horizontal = background_position[0]
        self.background_position_vertical = background_position[1]
        self.background_rectangle = (background_position[0], self.background_position_vertical, LETTER_SIZE, LETTER_SIZE)
        self.text = text
        self.text_position = (self.background_position_horizontal+36, self.background_position[1]+34)
        self.text_render = LETTER_FONT.render(self.text, True, self.text_color)
        self.text_rectangle = self.text_render.get_rect(center=self.text_position)
        
    # function to draw(show) the letter on screen

    def draw(self):
        pygame.draw.rect(SCREEN, self.background_color, self.background_rectangle)
        if self.background_color == "white":
            pygame.draw.rect(SCREEN, FILLED_OUTLINE, self.background_rectangle, 3)
        self.text_render = LETTER_FONT.render(self.text, True, self.text_color)
        SCREEN.blit(self.text_render, self.text_rectangle)
        pygame.display.update()
        
    # function to delete(remove) the letter on screen

    def delete(self):
        pygame.draw.rect(SCREEN, "white", self.background_rectangle)
        pygame.draw.rect(SCREEN, OUTLINE, self.background_rectangle, 3)
        pygame.display.update()

# function to check the current guess

class Alphabet:
    
    def __init__(self, horizontal, vertical, letter):
        self.horizontal = horizontal
        self.vertical = vertical
        self.text = letter
        self.rect = (self.horizontal, self.vertical, 57, 75)
        self.background_color = OUTLINE
        
    def draw(self):
        pygame.draw.rect(SCREEN, self.background_color, self.rect)
        self.text_display = LETTER_FONT.render(self.text, True, "white")
        self.text_rect = self.text_display.get_rect(center = (self.horizontal+27, self.vertical+30))
        SCREEN.blit(self.text_display, self.text_rect)
        pygame.display.update()
        
# draw the alphabet on screen

alphabet_horizontal, alphabet_vertical = 55, 600

for i in range(3):
    for letter in ALPHABET[i]:
        new_letter = Alphabet(alphabet_horizontal, alphabet_vertical, letter)
        keyboard.append(new_letter)
        new_letter.draw()
        alphabet_horizontal += 65
    alphabet_horizontal += 20
    alphabet_vertical += 100
    if i == 0:
        alphabet_horizontal = 110
    elif i == 1:
        alphabet_horizontal = 170
    

def check_guess(guess_to_check):
    global current_guess, current_guess_string, guesses_count, current_letter_background_horizontal, game_result, two_to_six_horizontal
    game_over = False
    for i in range(5):
        lowercase_letter = guess_to_check[i].text.lower() # first letter in current guess
        
        # if letter is in the correct word
        
        if lowercase_letter in CORRECT_WORD: 
            if lowercase_letter == CORRECT_WORD[i]: # if letter is equal to letter at this position in the correct word
                guess_to_check[i].background_color = GREEN # letter is correct, make green
                for keyboard_i in keyboard:
                    if keyboard_i.text == lowercase_letter.upper():
                        keyboard_i.background_color = GREEN
                        keyboard_i.draw()
                guess_to_check[i].text_color = "white"
                if not game_over:
                    game_result = "W"
                    
            else:
                guess_to_check[i].background_color = YELLOW # if letter is in but not at correct position, make yellow
                for keyboard_i in keyboard:
                    if keyboard_i.text == lowercase_letter.upper():
                        keyboard_i.background_color = YELLOW
                        keyboard_i.draw()
                guess_to_check[i].text_color = "white"
                game_result = ""
                game_over = True
                
        # if letter is not in the correct word
            
        else:
            guess_to_check[i].background_color = GREY # otherwise, the letter is grey
            for keyboard_i in keyboard:
                    if keyboard_i.text == lowercase_letter.upper():
                        keyboard_i.background_color = GREY
                        keyboard_i.draw()
            guess_to_check[i].text_color = "white"
            game_result = ""
            game_over = True
        guess_to_check[i].draw()
        pygame.display.update()
            
    
    guesses_count += 1 # increase guess count 
    current_guess = [] # clear current guess
    current_guess_string = "" # clear current guess string
    current_letter_background_horizontal = 167.5 # set letter spacing

    if guesses_count == 6 and game_result == "": # if guesses = 6 and game is not won, result is a loss
            game_result = "L"

# define a function to create a new letter for display

def create_new_letter():
    global current_guess_string, current_letter_background_horizontal
    current_guess_string += key_pressed # add key to current string
    new_letter = Letter(key_pressed, (current_letter_background_horizontal, guesses_count*100+LETTER_VERTICAL_SPACING)) # set spacing for letter
    current_letter_background_horizontal += LETTER_HORIZONTAL_SPACING
    guesses[guesses_count].append(new_letter) # add new letter to the end guesses list
    current_guess.append(new_letter) # add new letter to the end of current_guess list
    for guess in guesses:
        for letter in guess:
            letter.draw() # iterate through and display all letters
            

# define a function to delete a letter from the display

def delete_letter():
    global current_guess_string, current_letter_background_horizontal
    guesses[guesses_count][-1].delete() # delete last element from guesses list
    guesses[guesses_count].pop() 
    current_guess_string = current_guess_string[:-1] # remove letter from current_guess_string
    current_guess.pop()
    current_letter_background_horizontal -= LETTER_HORIZONTAL_SPACING # reset spacing
    
# define a function to display the play again screen

def play_again():
    pygame.draw.rect(SCREEN, "white", (10, 600, 1000, 600))
    FUNCTION_FONT = pygame.font.Font("design/BrontidevpDemoStyle2-ZV8E3.otf", 35)
    play_again_font = FUNCTION_FONT
    correct_word_font = LETTER_FONT
    play_again_text = play_again_font.render("Press ENTER to Play Again", True, "black")
    play_again_rect = play_again_text.get_rect(center=(WIDTH/2, 775))
    correct_word_text = correct_word_font.render(f"The word was {CORRECT_WORD}", True, "black")
    correct_word_rect = correct_word_text.get_rect(center=(WIDTH/2, 675))
    SCREEN.blit(correct_word_text, correct_word_rect)
    SCREEN.blit(play_again_text, play_again_rect)
    pygame.display.update()
    
# define a function to reset the game, called when a new game is started

def wordle_reset():
    global guesses_count, CORRECT_WORD, guesses, current_guess, current_guess_string, game_result, LETTER_HORIZONTAL_SPACING, LETTER_VERTICAL_SPACING, LETTER_SIZE, current_letter_background_horizontal
    LETTER_HORIZONTAL_SPACING = 85
    LETTER_VERTICAL_SPACING = 12
    LETTER_SIZE = 75
    current_letter_background_horizontal = 167.5
    SCREEN.fill("white")
    SCREEN.blit(BACKGROUND, BACKGROUND_RECTANGLE)
    guesses_count = 0
    CORRECT_WORD = random.choice(ANSWERS)
    guesses = [[]] * 6
    current_guess = []
    current_guess_string = ""
    game_result = ""
    pygame.display.update()
    for letter in keyboard:
        letter.background_color = OUTLINE
        letter.draw()
        
#function for the AI to make guesses

def ai_guess():
    global current_guess_string, current_guess, guesses_count, CORRECT_WORD
    previous_guess = None
<<<<<<< HEAD
    pg_1, pg_2, pg_3, pg_4, pg_5 = None, None, None, None, None
    previous_bool = False
    correct_letter = [False] * 5
    valid_guess = False
    letter1, letter2, letter3, letter4, letter5 = None, None, None, None, None
    test1, test2, test3, test4, test5 = False, False, False, False, False
    pass1, pass2, pass3, pass4, pass5 = True, True, True, True, True
=======
    correct_positions = [False] * 5
>>>>>>> 430a4e8c320d8837e09dad998f3351d1d22b2879
    
    # If this is not the first guess, extract the previous guess
    if guesses_count > 0:
<<<<<<< HEAD
        # Extract the previous guess letters
        previous_guess = ''.join(guess.text.lower() for guess in guesses[guesses_count - 1]) 
        previous_bool = True
        if guesses_count == 1:
            pg_1 = previous_guess
            print(pg_1)
            print(CORRECT_WORD)
        if guesses_count == 2:
            pg_2 = previous_guess[5:]
            print(pg_2)
            print(CORRECT_WORD)
        if guesses_count == 3:
            pg_3 = previous_guess[10:]
            print(pg_3)
            print(CORRECT_WORD)
        if guesses_count == 4:
            pg_4 = previous_guess[15:]
            print(pg_4)
            print(CORRECT_WORD)
        if guesses_count == 5:
            pg_5 = previous_guess[20:]
            print(pg_5)
            print(CORRECT_WORD)
    
    # If there is a previous guess
    if previous_bool:
        for i in range(5):
            if guesses_count == 1:
                if pg_1[i] == CORRECT_WORD[i]:
                    test1 = True
            if guesses_count == 2:
                if pg_2[i] == CORRECT_WORD[i]:
                    test2 = True
            if guesses_count == 3:
                if pg_3[i] == CORRECT_WORD[i]:
                    test1 = True
            if guesses_count == 4:
                if pg_4[i] == CORRECT_WORD[i]:
                    test4 = True
            if guesses_count == 5:
                if pg_5[i] == CORRECT_WORD[i]:
                    test5 = True
                
    guessed_word = random.choice(ANSWERS) 
    
    # # While the guess is not valid and it is not the first guess
    # while not valid_guess and guesses_count > 0:
    #     if test1:
    #         if guessed_word[0] != letter1:
    #             pass1 = False
    #     if test2:
    #         if guessed_word[1] != letter2:
    #             pass2 = False
    #     if test3:
    #         if guessed_word[2] != letter3:
    #             pass3 = False
    #     if test4:
    #         if guessed_word[3] != letter4:
    #             pass4 = False
    #     if test5:
    #         if guessed_word[4] != letter5:
    #             pass5 = False
    #     if pass1 and pass2 and pass3 and pass4 and pass5:
    #         valid_guess = True
    #         break
    #     else:
    #         guessed_word = random.choice(WORDS)
                
=======
        previous_guess = ''.join(guess.text.lower() for guess in guesses[guesses_count - 1])
    
    # Check correct positions in the previous guess
    if previous_guess:
        for i in range(5):
            if previous_guess[i] == CORRECT_WORD[i]:
                correct_positions[i] = True
    
    # Filter words based on correct positions
    possible_words = [word for word in WORDS if all(word[i] == previous_guess[i] for i in range(5) if correct_positions[i])]
    
    # Choose a word randomly from the filtered list
    if possible_words:
        guessed_word = random.choice(possible_words)
    else:
        guessed_word = random.choice(WORDS)
    
    # Update the current guess string and display the letters
>>>>>>> 430a4e8c320d8837e09dad998f3351d1d22b2879
    current_guess_string = guessed_word
    current_letter_background_horizontal = 167.5
    for i in range(len(guessed_word)):
        new_letter = Letter(guessed_word[i].upper(), (current_letter_background_horizontal, guesses_count * 100 + LETTER_VERTICAL_SPACING))
        current_letter_background_horizontal += LETTER_HORIZONTAL_SPACING
        guesses[guesses_count].append(new_letter)
        current_guess.append(new_letter)
        for guess in guesses:
            for letter in guess:
                letter.draw()
    
    # Check the guess
    check_guess(current_guess)
    previous_guess = ""




# main driver code of the program

while True:
    if game_result != "":
        play_again()
    for action in pygame.event.get():
        if action.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if action.type == pygame.KEYDOWN:
            if action.key == pygame.K_RETURN:
                if game_result != "":
                    wordle_reset()
                else:
                    ai_guess()
            elif action.key == pygame.K_BACKSPACE:
                if len(current_guess_string) > 0:
                    delete_letter()
            else:
                key_pressed = action.unicode.upper()
                if key_pressed in "QWERTYUIOPASDFGHJKLZXCVBNM" and key_pressed != "":
                    if len(current_guess_string) < 5:
                        create_new_letter()
        if action.type == pygame.MOUSEBUTTONDOWN and action.button == 1:
            if boundaries.collidepoint(action.pos): #if mouse is clicked over the button
                wordle_reset()
        if boundaries.collidepoint(pygame.mouse.get_pos()): #if mouse is over button, change color
            button_surface.fill(color_dynamic)
        else:
            button_surface.fill(color_static) #else do nothing to button color
 
        screen.blit(button_surface, (button_x, button_y)) #Initializes the button on the screen
        screen.blit(text, text_rect.topleft) #Initializes text on the button
        pygame.display.flip()