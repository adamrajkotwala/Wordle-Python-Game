import array
import pygame # pygame library for game development
import sys
import random # to generate random numbers
from word_list import * # access to word_list file that contains list of different 5 letter words

pygame.init() # initialize pygame

#DEFINING CONSTANTS

WIDTH, HEIGHT = 650, 900 # dimensions of the display

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT)) # define screen with desired dimensions
BACKGROUND = pygame.image.load("design/Starting Tiles.png") # define background, load image with background tiles found online
BACKGROUND_RECTANGLE = BACKGROUND.get_rect(center=(317, 300)) # define background rectangle and center it
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

CORRECT_WORD = "paper"

ALPHABET = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]

LETTER_FONT = pygame.font.Font("design/BrontidevpDemoStyle2-ZV8E3.otf", 50) # define a letter font variable with font file

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
current_letter_background_horizontal = 110
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

alphabet_horizontal, alphabet_vertical = 20, 600

for i in range(3):
    for letter in ALPHABET[i]:
        new_letter = Alphabet(alphabet_horizontal, alphabet_vertical, letter)
        keyboard.append(new_letter)
        new_letter.draw()
        alphabet_horizontal += 60
    alphabet_horizontal += 20
    alphabet_vertical += 100
    if i == 0:
        alphabet_horizontal = 50
    elif i == 1:
        alphabet_horizontal = 105
    
# function to check the current guess
def check_guess(guess_to_check):
    global current_guess, current_guess_string, guesses_count, current_letter_background_horizontal, game_result
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
    current_letter_background_horizontal = 110 # set letter spacing

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

# main driver code of the program

while True:
    
    #for all events in pygame
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        # if event is a key pressed   
            
        if event.type == pygame.KEYDOWN:
            # if key pressed is return
            if event.key == pygame.K_RETURN: 
                if game_result != "":
                    pygame.quit()
                    sys.exit()
                else:
                    if len(current_guess_string) == 5 and current_guess_string.lower() in WORDS: # if guess length is 5 and a valid word (from list)
                        check_guess(current_guess) # check the guess
            # else if key pressed is backspace
            elif event.key == pygame.K_BACKSPACE: # if key is backspace delete the last letter
                if len(current_guess_string) > 0:
                    delete_letter()
            # else (any other key is pressed)
            else:
                key_pressed = event.unicode.upper()
                if key_pressed in "QWERTYUIOPASDFGHJKLZXCVBNM" and key_pressed != "": # if key pressed is a letter, create new letter
                    if len(current_guess_string) < 5:
                        create_new_letter()
            pygame.display.update()